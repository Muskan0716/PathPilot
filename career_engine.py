
CAREERS = [

    {
        "name": "Python Developer",
        "slug": "python-developer",
        "skills": ["python", "sql", "oop", "problem solving", "data structures"],
        "courses": [
            "programming fundamentals",
            "python programming",
            "data structures and algorithms",
            "database management systems",
            "software engineering"
        ],
        "interests": [
            "software development", "software",
            "backend development", "backend", "coding"
        ],
        "description": "Develop applications, software systems and backend solutions.",
        "projects": [
            "To-do application",
            "Expense tracker",
            "REST API"
        ]
    },

    {
        "name": "AI / ML Engineer",
        "slug": "ai-ml-engineer",
        "skills": [
            "python", "machine learning", "deep learning",
            "data analysis", "data science", "tensorflow", "pytorch"
        ],
        "courses": [
            "artificial intelligence",
            "machine learning",
            "deep learning",
            "data science",
            "python programming",
            "mathematics and statistics"
        ],
        "interests": [
            "artificial intelligence", "ai",
            "machine learning", "data and analytics",
            "data", "analytics"
        ],
        "description": "Build intelligent systems using artificial intelligence and machine learning.",
        "projects": [
            "House price prediction",
            "Image classification",
            "Recommendation system"
        ]
    },

    {
        "name": "Frontend Developer",
        "slug": "frontend-developer",
        "skills": ["html", "css", "javascript", "react", "bootstrap"],
        "courses": [
            "web development",
            "ui / ux design",
            "programming fundamentals"
        ],
        "interests": [
            "web development",
            "frontend development",
            "frontend",
            "design"
        ],
        "description": "Design and develop interactive and responsive websites.",
        "projects": [
            "Personal portfolio",
            "Weather application",
            "E-commerce website"
        ]
    },

    {
        "name": "Data Analyst",
        "slug": "data-analyst",
        "skills": [
            "python", "sql", "data analysis",
            "excel", "power bi", "tableau"
        ],
        "courses": [
            "data analytics",
            "data science",
            "database management systems",
            "mathematics and statistics",
            "business analytics"
        ],
        "interests": [
            "data and analytics", "data",
            "analytics", "business and technology",
            "business"
        ],
        "description": "Analyse data, identify patterns and generate useful business insights.",
        "projects": [
            "Sales dashboard",
            "Customer analysis",
            "Data visualization"
        ]
    },

    {
        "name": "Java Developer",
        "slug": "java-developer",
        "skills": [
            "java", "sql", "oop",
            "problem solving", "data structures"
        ],
        "courses": [
            "programming fundamentals",
            "java programming",
            "data structures and algorithms",
            "database management systems",
            "software engineering"
        ],
        "interests": [
            "software development", "software",
            "backend development", "backend", "coding"
        ],
        "description": "Build software applications and backend systems using Java.",
        "projects": [
            "Library management system",
            "Banking application",
            "Java web application"
        ]
    }

]


def normalize_list(text):

    if not text:
        return []

    if isinstance(text, list):
        return [
            str(item).strip().lower()
            for item in text
            if str(item).strip()
        ]

    return [
        item.strip().lower()
        for item in text.split(",")
        if item.strip()
    ]


def contains_match(selected_items, required_items):

    matched = []

    for required in required_items:

        for selected in selected_items:

            if required == selected:
                matched.append(required)
                break

    return matched


def recommend_careers(skills_text="", interests_text="", courses_text=""):

    skills = normalize_list(skills_text)
    interests = normalize_list(interests_text)
    courses = normalize_list(courses_text)

    results = []

    for career in CAREERS:

        matched_skills = contains_match(
            skills,
            career["skills"]
        )

        matched_courses = contains_match(
            courses,
            career["courses"]
        )

        matched_interests = contains_match(
            interests,
            career["interests"]
        )

        skill_score = len(matched_skills) * 2
        course_score = len(matched_courses) * 2
        interest_score = len(matched_interests) * 2

        score = skill_score + course_score + interest_score

        maximum_score = (
            len(career["skills"]) * 2
            + len(career["courses"]) * 2
            + len(career["interests"]) * 2
        )

        percentage = round(
            (score / maximum_score) * 100
        ) if maximum_score else 0

        reasons = []

        if matched_skills:
            reasons.append("Your skills match this career.")

        if matched_courses:
            reasons.append("Your selected courses are relevant to this career.")

        if matched_interests:
            reasons.append("Your career interests match this field.")

        results.append({
            **career,
            "score": score,
            "match_percentage": percentage,
            "matched_skills": matched_skills,
            "matched_courses": matched_courses,
            "matched_interests": matched_interests,
            "reasons": reasons
        })

    return sorted(
        results,
        key=lambda item: item["score"],
        reverse=True
    )
