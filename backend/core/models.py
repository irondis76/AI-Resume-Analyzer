from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class ContactInfo(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    location: Optional[str] = None


class Section(BaseModel):
    title: str
    content: str


class ResumeData(BaseModel):
    raw_text: str
    pages: Optional[int] = None
    file_size_bytes: Optional[int] = None
    word_count: Optional[int] = None
    contact: ContactInfo = ContactInfo()
    sections: List[Section] = []


class Recommendation(BaseModel):
    category: str
    title: str
    description: str
    impact: str
    priority: int
    examples: Optional[List[str]] = None


class SkillAnalysis(BaseModel):
    extracted_skills: List[str] = []
    missing_skills: List[str] = []
    recommendations: List[Recommendation] = []


class ExperienceAnalysis(BaseModel):
    seniority: Optional[str] = None
    themes: List[str] = []
    impact_quality: Optional[str] = None
    recommendations: List[Recommendation] = []


class FormattingAnalysis(BaseModel):
    ats_issues: List[str] = []
    readability_issues: List[str] = []
    recommendations: List[Recommendation] = []


class ATSAnalysis(BaseModel):
    keyword_coverage: List[str] = []
    gaps: List[str] = []
    recommendations: List[Recommendation] = []


class AnalysisResult(BaseModel):
    summary: str
    skills: SkillAnalysis
    experience: ExperienceAnalysis
    formatting: FormattingAnalysis
    ats: ATSAnalysis
    overall_recommendations: List[Recommendation]
    report_markdown: str


