
#!/usr/bin/env python
import sys
import warnings
import os
from datetime import datetime

from software_engineer.crew import SoftwareEngineer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
Build a self-contained Resume Analyzer module in Python that works with both PDF resumes and raw text input. 
No network calls. Pure Python with optional use of regex, scikit-learn, and pdfplumber for PDF parsing (fallback gracefully if not installed).

Core features
1) Input handling
   - Accept either: (a) uploaded PDF file, or (b) pasted resume text.
   - If PDF: extract text using pdfplumber (or PyPDF2 fallback).
   - If pasted: use the string directly.
   - Always require a job description (pasted as text).

2) Parsing
   - Normalize text (lowercasing, whitespace cleanup).
   - Keep an original copy for highlights.

3) Skills extraction
   - Internal skills dictionary (programming, ML, data, cloud, tools, NLP).
   - Match skills in resume and job description.
   - Simple stemming rules (e.g., "models" → "model").

4) Scoring
   - Keyword coverage score: % of JD skills present in resume.
   - Section balance: check for Education, Experience, Projects, Skills sections.
   - Readability: bullet length, use of active verbs, presence of numbers/metrics.
   - Final score: weighted average of components.

5) Suggestions
   - List missing skills.
   - Generate up to 3 tailored improvement bullet suggestions.
   - Flag missing metrics.
   - Flag long bullets > 30 words.

6) Output
   - Return dict with: final_score, keyword_score, readability_score, section_balance_score, present_skills, missing_skills, suggestions, highlights.
   - Provide plain-text report and JSON-friendly dict.

7) Public API
   - class {class_name}:
       parse_resume(self, text_or_file) -> dict
       parse_job_description(self, jd_text: str) -> dict
       analyze(self, resume_input, jd_text: str) -> dict
       export_report(self, analysis: dict, path: str | None = None) -> str

8) Unit Tests
   - Provide small sample JD and resume (both text and PDF).
   - Test PDF parsing, scoring, missing skills, suggestions, and error handling.

9) Gradio UI
   - Input options:
       a) File uploader for PDF resume (`gr.File`, with type="filepath" and file_types=[".pdf"])
       b) Textbox for resume text
       c) Textbox for job description
   - Button "Analyze"
   - Outputs:
       - Final score
       - Present vs missing skills
       - Suggestions
       - Plain-text summary
   - Optional "Download Report" (write to temp file, return link/path).
   - Important: Ensure the File component uses type="filepath" (not "file").

10) Non-functional
   - Single backend file {module_name}, single UI file app.py, single test file test_{module_name}.
   - Deterministic results with same inputs.
   - No internet access.
"""


module_name = "resume_analyzer.py"
class_name = "ResumeAnalyzer"



def run():
    """
    Run the research crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = SoftwareEngineer().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
