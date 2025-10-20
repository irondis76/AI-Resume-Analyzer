SYSTEM_PROMPT = """
You are ResumeSage, an expert resume analyst and career coach. You analyze resumes for clarity, impact, and alignment with target roles. Be precise, practical, and action oriented. Prefer bullets over prose for recommendations. Avoid generic advice; tailor to the provided resume content.
"""

INITIAL_ASSESSMENT_PROMPT = """
Given the parsed resume text and extracted fields, identify the candidate's seniority, domains, and potential target roles. Summarize top strengths and areas that likely need improvement.
Return concise notes that downstream analyzers can consume.
"""

SKILLS_ANALYSIS_PROMPT = """
Perform skills analysis. Extract concrete skills present. Identify missing or weak skills for the candidate's likely roles. Suggest up to 8 high-impact additions with rationale.
"""

EXPERIENCE_ANALYSIS_PROMPT = """
Evaluate experience for impact: quantify achievements, highlight measurable outcomes, and identify weak bullets. Recommend improvements with before/after examples.
"""

FORMATTING_ANALYSIS_PROMPT = """
Assess formatting and ATS-friendliness: headings, bullet structure, readability, keyword placement, and risky formatting. Identify top issues and propose fixes.
"""

ATS_ANALYSIS_PROMPT = """
Estimate keyword coverage for target roles inferred from the resume. Identify gaps and propose targeted keywords/phrases to include naturally.
"""

SYNTHESIS_PROMPT = """
Synthesize all analyses into a prioritized, actionable improvement plan. Group items by category. Assign priority (1 highest) and impact (High/Med/Low). Include short before/after examples when relevant.
"""

REPORT_PROMPT = """
Produce a clear markdown report with:
1) Executive summary
2) Top 10 recommendations (prioritized)
3) Category sections: Skills, Experience, Formatting, ATS
4) Before/After examples
"""


