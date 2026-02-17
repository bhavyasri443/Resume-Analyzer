from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from auth import signup_user, login_user
from resume_parser import extract_text
from analyzer import analyze_resume


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# serve frontend files (css)
app.mount("/static", StaticFiles(directory="frontend"), name="static")


# -------------------------
# Frontend page routes
# -------------------------

@app.get("/")
def home_page():
    return FileResponse("frontend/index.html")


@app.get("/signup-page")
def signup_page():
    return FileResponse("frontend/signup.html")


@app.get("/login-page")
def login_page():
    return FileResponse("frontend/login.html")


@app.get("/choice-page")
def choice_page():
    return FileResponse("frontend/choice.html")


@app.get("/analyze-page")
def analyze_page():
    return FileResponse("frontend/analyze.html")


# -------------------------
# Auth APIs
# -------------------------

@app.post("/signup")
def signup(username: str = Form(...), password: str = Form(...)):
    return signup_user(username, password)


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return login_user(username, password)


# -------------------------
# Resume analyze API
# -------------------------

@app.post("/analyze")
async def analyze(
    track: str = Form(...),
    resume: UploadFile = Form(...),
    job_description: str = Form("")
):
    path = "temp_resume.pdf"

    with open(path, "wb") as f:
        f.write(await resume.read())

    resume_text = extract_text(path)

    result = analyze_resume(resume_text, track, job_description)

    return result


# -------------------------
# Download PDF report API
# -------------------------

@app.post("/download-report")
async def download_report(
    track: str = Form(...),
    resume: UploadFile = Form(...),
    job_description: str = Form("")
):
    temp_path = "temp_resume.pdf"

    with open(temp_path, "wb") as f:
        f.write(await resume.read())

    resume_text = extract_text(temp_path)

    result = analyze_resume(resume_text, track, job_description)

    file_name = "resume_report.pdf"

    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            f"Resume Score : {result['resume_score']} / 100",
            styles["Heading2"]
        )
    )
    story.append(Spacer(1, 12))

    story.append(Paragraph("Missing skills and why they matter:", styles["Heading3"]))
    story.append(Spacer(1, 8))

    for item in result["skill_gap_explanation"]:
        line = f"{item['skill']} - {item['reason']}"
        story.append(Paragraph(line, styles["BodyText"]))

    story.append(Spacer(1, 12))

    story.append(Paragraph("Suggestions to improve:", styles["Heading3"]))
    story.append(Spacer(1, 8))

    for s in result["resume_suggestions"]:
        story.append(Paragraph(s, styles["BodyText"]))

    if result["job_match_score"] is not None:
        story.append(Spacer(1, 12))
        story.append(
            Paragraph(
                f"Job description match score : {result['job_match_score']} %",
                styles["BodyText"]
            )
        )

    doc.build(story)

    return FileResponse(
        file_name,
        media_type="application/pdf",
        filename=file_name
    )
