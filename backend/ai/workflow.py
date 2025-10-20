from __future__ import annotations

from typing import Any, Dict

from langgraph.graph import StateGraph, END
from openai import OpenAI

from ..core.config import settings
from ..core.models import (
    AnalysisResult,
    ATSAnalysis,
    ExperienceAnalysis,
    FormattingAnalysis,
    Recommendation,
    ResumeData,
    SkillAnalysis,
)
from .prompts import (
    SYSTEM_PROMPT,
    INITIAL_ASSESSMENT_PROMPT,
    SKILLS_ANALYSIS_PROMPT,
    EXPERIENCE_ANALYSIS_PROMPT,
    FORMATTING_ANALYSIS_PROMPT,
    ATS_ANALYSIS_PROMPT,
    SYNTHESIS_PROMPT,
    REPORT_PROMPT,
)


client = OpenAI(api_key=settings.openai_api_key)


class GraphState(dict):
    # Inputs
    resume: ResumeData

    # Intermediate
    notes: str
    skills: SkillAnalysis
    experience: ExperienceAnalysis
    formatting: FormattingAnalysis
    ats: ATSAnalysis

    # Output
    result: AnalysisResult


def _chat(prompt: str, extra: str = "") -> str:
    content = prompt.strip()
    if extra:
        content += "\n\n" + extra.strip()
    resp = client.chat.completions.create(
        model=settings.model_name,
        temperature=settings.temperature,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": content},
        ],
    )
    return resp.choices[0].message.content or ""


def initial_assessment(state: GraphState) -> GraphState:
    resume = state["resume"]
    extra = f"RAW TEXT:\n{resume.raw_text[:7000]}"
    notes = _chat(INITIAL_ASSESSMENT_PROMPT, extra)
    state["notes"] = notes
    return state


def skills_analysis(state: GraphState) -> GraphState:
    notes = state.get("notes", "")
    text = state["resume"].raw_text
    output = _chat(SKILLS_ANALYSIS_PROMPT, f"NOTES:\n{notes}\n\nTEXT:\n{text[:7000]}")
    # Minimal parsing; let downstream synthesis structure
    state["skills"] = SkillAnalysis(extracted_skills=[], missing_skills=[], recommendations=[])
    state["skills"].recommendations.append(
        Recommendation(category="Skills", title="Skills Analysis", description=output, impact="High", priority=2)
    )
    return state


def experience_analysis(state: GraphState) -> GraphState:
    notes = state.get("notes", "")
    text = state["resume"].raw_text
    output = _chat(EXPERIENCE_ANALYSIS_PROMPT, f"NOTES:\n{notes}\n\nTEXT:\n{text[:7000]}")
    state["experience"] = ExperienceAnalysis(recommendations=[
        Recommendation(category="Experience", title="Experience Analysis", description=output, impact="High", priority=2)
    ])
    return state


def formatting_analysis(state: GraphState) -> GraphState:
    text = state["resume"].raw_text
    output = _chat(FORMATTING_ANALYSIS_PROMPT, f"TEXT:\n{text[:7000]}")
    state["formatting"] = FormattingAnalysis(recommendations=[
        Recommendation(category="Formatting", title="Formatting & ATS", description=output, impact="Medium", priority=3)
    ])
    return state


def ats_analysis(state: GraphState) -> GraphState:
    notes = state.get("notes", "")
    text = state["resume"].raw_text
    output = _chat(ATS_ANALYSIS_PROMPT, f"NOTES:\n{notes}\n\nTEXT:\n{text[:7000]}")
    state["ats"] = ATSAnalysis(recommendations=[
        Recommendation(category="ATS", title="ATS Keyword Coverage", description=output, impact="Medium", priority=3)
    ])
    return state


def synthesis(state: GraphState) -> GraphState:
    text = state["resume"].raw_text
    collated = []
    for key in ["skills", "experience", "formatting", "ats"]:
        if key in state and getattr(state[key], "recommendations", None):
            for r in state[key].recommendations:
                collated.append(f"[{r.category}] {r.title}: {r.description}")
    plan = _chat(SYNTHESIS_PROMPT, "\n\n".join(collated)[:12000])
    report = _chat(REPORT_PROMPT, f"RESUME:\n{text[:6000]}\n\nPLAN:\n{plan[:6000]}")
    state["result"] = AnalysisResult(
        summary=plan.splitlines()[0] if plan else "",
        skills=state.get("skills"),
        experience=state.get("experience"),
        formatting=state.get("formatting"),
        ats=state.get("ats"),
        overall_recommendations=[
            Recommendation(category="Overall", title="Action Plan", description=plan, impact="High", priority=1)
        ],
        report_markdown=report,
    )
    return state


def build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("initial", initial_assessment)
    graph.add_node("skills", skills_analysis)
    graph.add_node("experience", experience_analysis)
    graph.add_node("formatting", formatting_analysis)
    graph.add_node("ats", ats_analysis)
    graph.add_node("synthesis", synthesis)

    graph.set_entry_point("initial")
    graph.add_edge("initial", "skills")
    graph.add_edge("initial", "experience")
    graph.add_edge("initial", "formatting")
    graph.add_edge("initial", "ats")

    # After parallel steps, go to synthesis.
    graph.add_edge("skills", "synthesis")
    graph.add_edge("experience", "synthesis")
    graph.add_edge("formatting", "synthesis")
    graph.add_edge("ats", "synthesis")

    graph.add_edge("synthesis", END)
    return graph.compile()


