from __future__ import annotations

import io
import re
from typing import List, Tuple

import pdfplumber
from docx import Document

from .models import ContactInfo, ResumeData, Section


EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"(?:(?:\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4})")
LINKEDIN_RE = re.compile(r"(?:https?://)?(?:www\.)?linkedin\.com/[^\s)]+", re.IGNORECASE)
GITHUB_RE = re.compile(r"(?:https?://)?(?:www\.)?github\.com/[^\s)]+", re.IGNORECASE)


def _extract_sections_from_text(text: str) -> List[Section]:
    # Heuristic section split by common headings
    headings = [
        "summary", "objective", "experience", "work experience", "employment",
        "projects", "education", "skills", "certifications", "achievements",
        "publications", "awards", "interests", "hobbies"
    ]
    pattern = re.compile(rf"^(?:{'|'.join(headings)})[:\s]*$", re.IGNORECASE | re.MULTILINE)

    sections: List[Section] = []
    last_idx = 0
    last_title = "Body"
    for match in pattern.finditer(text):
        title = match.group(0).strip().rstrip(":").title()
        content = text[last_idx:match.start()].strip()
        if content:
            sections.append(Section(title=last_title, content=content))
        last_idx = match.end()
        last_title = title
    tail = text[last_idx:].strip()
    if tail:
        sections.append(Section(title=last_title, content=tail))
    return sections


def _extract_contact_info(text: str) -> ContactInfo:
    email = EMAIL_RE.search(text)
    phone = PHONE_RE.search(text)
    linkedin = LINKEDIN_RE.search(text)
    github = GITHUB_RE.search(text)

    lines = [l.strip() for l in text.splitlines() if l.strip()]
    probable_name = None
    if lines:
        first_line = lines[0]
        # Basic name heuristic: few words, mostly letters
        if 1 <= len(first_line.split()) <= 5 and re.fullmatch(r"[A-Za-z ,.'-]+", first_line):
            probable_name = first_line

    return ContactInfo(
        name=probable_name,
        email=email.group(0) if email else None,
        phone=phone.group(0) if phone else None,
        linkedin=linkedin.group(0) if linkedin else None,
        github=github.group(0) if github else None,
    )


def parse_pdf(file_bytes: bytes) -> Tuple[str, int]:
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        pages_text = []
        for page in pdf.pages:
            pages_text.append(page.extract_text(x_tolerance=1.5, y_tolerance=1.5) or "")
        text = "\n".join(pages_text)
        return text, len(pdf.pages)


def parse_docx(file_bytes: bytes) -> str:
    document = Document(io.BytesIO(file_bytes))
    paragraphs = [p.text for p in document.paragraphs]
    return "\n".join(paragraphs)


def parse_resume(file_bytes: bytes, filename: str | None = None) -> ResumeData:
    name = (filename or "").lower()
    if name.endswith(".pdf"):
        text, pages = parse_pdf(file_bytes)
    elif name.endswith(".docx"):
        text = parse_docx(file_bytes)
        pages = None
    else:
        # Try both parsers; prefer text with more content
        try:
            text_pdf, pages = parse_pdf(file_bytes)
        except Exception:
            text_pdf, pages = "", None
        try:
            text_docx = parse_docx(file_bytes)
        except Exception:
            text_docx = ""
        text = text_pdf if len(text_pdf) >= len(text_docx) else text_docx

    word_count = len(re.findall(r"\w+", text))
    contact = _extract_contact_info(text)
    sections = _extract_sections_from_text(text)

    return ResumeData(
        raw_text=text,
        pages=pages,
        file_size_bytes=len(file_bytes),
        word_count=word_count,
        contact=contact,
        sections=sections,
    )


