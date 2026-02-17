from sentence_transformers import SentenceTransformer, util

ROLE_SKILLS = {

    "frontend": [
        "html","css","javascript","react","git","github",
        "bootstrap","api","responsive design"
    ],

    "backend": [
        "python","java","node","express","sql",
        "mongodb","rest api","fastapi","django"
    ],

    "data": [
        "python","pandas","numpy","matplotlib",
        "machine learning","statistics","sql"
    ],

    "ai": [
        "python","machine learning","deep learning",
        "tensorflow","pytorch","nlp","cnn"
    ],

    "fullstack": [
        "html","css","javascript","react","node","express","sql","mongodb","api"
    ],

    "mobile": [
        "flutter","react native","android","ios","kotlin","swift","api"
    ],

    "devops": [
        "linux","docker","kubernetes","ci/cd","jenkins","aws","terraform"
    ],

    "cloud": [
        "aws","azure","gcp","cloud security","cloud networking","terraform"
    ],

    "cybersecurity": [
        "network security","ethical hacking","penetration testing",
        "cryptography","linux","firewalls"
    ],

    "blockchain": [
        "blockchain","solidity","smart contracts","web3","ethereum","cryptography"
    ],

    "game": [
        "unity","c#","game physics","3d graphics","blender","unreal engine"
    ],

    "embedded": [
        "c","c++","microcontrollers","rtos","embedded systems","arm"
    ],

    "iot": [
        "iot","mqtt","raspberry pi","arduino","embedded systems","cloud iot"
    ],

    "qa": [
        "manual testing","test cases","bug tracking","jira","software testing"
    ],

    "automation": [
        "selenium","python","java","test automation","cypress","api testing"
    ],

    "uiux": [
        "figma","wireframing","prototyping","user research","design systems"
    ],

    "product": [
        "product management","roadmaps","agile","scrum","user stories","analytics"
    ],

    "business_analyst": [
        "requirements gathering","stakeholder management",
        "process modeling","sql","documentation"
    ],

    "data_engineer": [
        "python","sql","spark","hadoop","etl","airflow","data pipelines"
    ],

    "mlops": [
        "mlflow","docker","kubernetes","model deployment","ci/cd","monitoring"
    ],

    "sre": [
        "linux","monitoring","prometheus","grafana",
        "incident management","cloud"
    ],

    "arvr": [
        "unity","c#","ar","vr","3d modeling","xr"
    ],

    "robotics": [
        "robotics","ros","python","c++","computer vision","control systems"
    ],

    "bioinformatics": [
        "python","r","genomics","biostatistics","machine learning","data analysis"
    ]
}


# -------------------------------------------------
# Generic one-line explanations (skill → reason)
# -------------------------------------------------

SKILL_REASON = {
    "html": "It is required to structure web pages correctly.",
    "css": "It is required to design and style user interfaces.",
    "javascript": "It is required to build interactive client-side features.",
    "react": "It is widely used to build modern front-end applications.",
    "git": "It is required for version control and team collaboration.",
    "github": "It is used to host and manage project repositories.",
    "bootstrap": "It helps in building responsive layouts faster.",
    "api": "It is required to integrate frontend and backend services.",
    "responsive design": "It ensures your application works on all screen sizes.",

    "python": "It is a core programming language used across many roles.",
    "java": "It is widely used for enterprise backend development.",
    "node": "It is used to build scalable backend services.",
    "express": "It is used to build APIs quickly in Node.js.",
    "sql": "It is required to store and retrieve structured data.",
    "mongodb": "It is used for handling unstructured and document data.",
    "rest api": "It allows systems to communicate with each other.",
    "fastapi": "It is used to build fast and modern Python APIs.",
    "django": "It is used to build secure backend web applications.",

    "pandas": "It is used for data cleaning and data analysis.",
    "numpy": "It is used for numerical and scientific computing.",
    "matplotlib": "It is used to visualize data insights.",
    "machine learning": "It is required to build predictive models.",
    "statistics": "It is needed to analyze and interpret data properly.",

    "deep learning": "It is used for complex problems like vision and NLP.",
    "tensorflow": "It is used to train and deploy deep learning models.",
    "pytorch": "It is widely used for research and deep learning projects.",
    "nlp": "It is required to work with text and language data.",
    "cnn": "It is required for image and vision based tasks.",

    "flutter": "It is used to build cross-platform mobile apps.",
    "react native": "It is used to build mobile apps using JavaScript.",
    "android": "It is required for native Android development.",
    "ios": "It is required for native iOS development.",
    "kotlin": "It is the preferred language for Android apps.",
    "swift": "It is the main language for iOS apps.",

    "linux": "It is required to manage servers and cloud systems.",
    "docker": "It is used to containerize applications.",
    "kubernetes": "It is used to manage containerized applications.",
    "ci/cd": "It automates testing and deployment.",
    "jenkins": "It is used for building CI pipelines.",
    "aws": "It is widely used cloud platform.",
    "terraform": "It is used to manage infrastructure as code.",

    "network security": "It protects systems from network attacks.",
    "ethical hacking": "It is required to identify security vulnerabilities.",
    "penetration testing": "It helps test system security.",
    "cryptography": "It secures data using encryption.",
    "firewalls": "They protect networks from unauthorized access.",

    "blockchain": "It is required to build decentralized systems.",
    "solidity": "It is used to write smart contracts.",
    "smart contracts": "They automate transactions on blockchain.",
    "web3": "It is used to build decentralized applications.",
    "ethereum": "It is a popular blockchain platform.",

    "unity": "It is used to build games and AR/VR apps.",
    "c#": "It is required for Unity development.",
    "game physics": "It improves realism in games.",
    "3d graphics": "It is required for 3D rendering.",
    "blender": "It is used to create 3D assets.",
    "unreal engine": "It is used for high quality game development.",

    "c": "It is required for low level programming.",
    "c++": "It is required for performance critical systems.",
    "microcontrollers": "They are core components of embedded systems.",
    "rtos": "It manages real-time embedded tasks.",
    "embedded systems": "It is required to build hardware-software solutions.",
    "arm": "It is widely used embedded processor architecture.",

    "iot": "It connects physical devices to the internet.",
    "mqtt": "It is a lightweight communication protocol for IoT.",
    "raspberry pi": "It is used for IoT and prototyping projects.",
    "arduino": "It is widely used in hardware prototyping.",
    "cloud iot": "It helps manage IoT devices at scale.",

    "manual testing": "It is required to validate software quality.",
    "test cases": "They define how software should be tested.",
    "bug tracking": "It helps manage defects efficiently.",
    "jira": "It is used to manage testing and development tasks.",
    "software testing": "It ensures product quality.",

    "selenium": "It is used to automate browser testing.",
    "test automation": "It reduces manual testing effort.",
    "cypress": "It is used for modern web testing.",
    "api testing": "It validates backend services.",

    "figma": "It is used to design UI layouts.",
    "wireframing": "It helps plan interface structure.",
    "prototyping": "It validates UI ideas quickly.",
    "user research": "It helps understand user needs.",
    "design systems": "They maintain UI consistency.",

    "product management": "It helps define product direction.",
    "roadmaps": "They guide product planning.",
    "agile": "It enables iterative product delivery.",
    "scrum": "It structures agile development.",
    "user stories": "They describe user requirements.",
    "analytics": "They help measure product performance.",

    "requirements gathering": "It helps understand business needs.",
    "stakeholder management": "It ensures alignment with business teams.",
    "process modeling": "It improves business workflows.",
    "documentation": "It helps communicate requirements clearly.",

    "spark": "It is used for big data processing.",
    "hadoop": "It is used to store and process big data.",
    "etl": "It prepares data for analytics.",
    "airflow": "It schedules data pipelines.",
    "data pipelines": "They move and transform data.",

    "mlflow": "It tracks ML experiments.",
    "model deployment": "It makes models usable in production.",
    "monitoring": "It tracks system and model health.",

    "prometheus": "It collects system metrics.",
    "grafana": "It visualizes system performance.",
    "incident management": "It handles production failures.",

    "ar": "It builds augmented reality apps.",
    "vr": "It builds virtual reality experiences.",
    "3d modeling": "It creates 3D assets.",
    "xr": "It supports mixed reality systems.",

    "robotics": "It enables intelligent robotic systems.",
    "ros": "It is a common robotics framework.",
    "computer vision": "It enables machines to see and understand images.",
    "control systems": "They control robot movement.",

    "r": "It is used for statistical computing.",
    "genomics": "It analyzes biological sequence data.",
    "biostatistics": "It analyzes biological datasets.",
    "data analysis": "It extracts insights from data."
}


model = SentenceTransformer("all-MiniLM-L6-v2")


def find_skills(resume_text, required):
    present = []
    missing = []

    for skill in required:
        if skill in resume_text:
            present.append(skill)
        else:
            missing.append(skill)

    return present, missing


def resume_score(present, total):
    if len(total) == 0:
        return 0
    return int((len(present) / len(total)) * 100)


def build_skill_gap(role, missing):
    gaps = []

    for s in missing:
        gaps.append({
            "skill": s,
            "reason": SKILL_REASON.get(
                s,
                "This skill is important for performing core responsibilities of this role."
            )
        })

    return gaps


def make_suggestions(missing):
    return [
        f"Learn {s} and build at least one project using {s} to strengthen your profile."
        for s in missing
    ]


def jd_match(resume, jd):
    if not jd.strip():
        return None

    emb = model.encode([resume, jd])
    sim = util.cos_sim(emb[0], emb[1])

    return round(float(sim) * 100, 2)


def analyze_resume(resume_text, role, job_description):

    required = ROLE_SKILLS.get(role, [])

    present, missing = find_skills(resume_text, required)

    return {
        "present_skills": present,
        "missing_skills": missing,
        "skill_gap_explanation": build_skill_gap(role, missing),
        "resume_suggestions": make_suggestions(missing),
        "resume_score": resume_score(present, required),
        "job_match_score": jd_match(resume_text, job_description)
    }
