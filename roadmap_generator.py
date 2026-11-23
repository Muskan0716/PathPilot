
ROADMAPS = {
    "python-developer": [
        "Learn Python fundamentals: variables, data types and operators.",
        "Practice conditional statements and loops.",
        "Learn functions, lists, tuples, sets and dictionaries.",
        "Understand object-oriented programming in Python.",
        "Learn SQL and database fundamentals.",
        "Study Flask and REST API development.",
        "Build projects such as an expense tracker and task manager.",
        "Practice Python programming problems on LeetCode."
    ],

    "ai-ml-engineer": [
        "Learn Python programming fundamentals.",
        "Study mathematics: linear algebra, probability and statistics.",
        "Learn NumPy, Pandas and Matplotlib.",
        "Understand machine learning algorithms.",
        "Practice supervised and unsupervised learning.",
        "Learn model evaluation and feature engineering.",
        "Explore deep learning and neural networks.",
        "Build projects such as house price prediction and image classification."
    ],

    "frontend-developer": [
        "Learn HTML fundamentals.",
        "Study CSS, layouts and responsive web design.",
        "Learn JavaScript fundamentals.",
        "Understand DOM manipulation and events.",
        "Learn React fundamentals.",
        "Understand APIs and frontend-backend integration.",
        "Build a portfolio website and weather application.",
        "Deploy your projects online."
    ],

    "data-analyst": [
        "Learn Python programming fundamentals.",
        "Study SQL queries and database concepts.",
        "Learn Excel and data cleaning.",
        "Practice data analysis using Pandas.",
        "Learn data visualization using Matplotlib.",
        "Explore Power BI or Tableau.",
        "Understand statistics and business analytics.",
        "Build sales analysis and visualization projects."
    ],

    "java-developer": [
        "Learn Java syntax and fundamentals.",
        "Understand arrays, strings and collections.",
        "Study object-oriented programming.",
        "Learn exception handling and file handling.",
        "Practice data structures and algorithms.",
        "Learn SQL and database connectivity.",
        "Explore Java backend development.",
        "Build projects such as a library management system."
    ]
}


def generate_roadmap(career_slug):
    """
    Returns a learning roadmap for the selected career.
    """
    return ROADMAPS.get(
        career_slug,
        [
            "Learn programming fundamentals.",
            "Practice data structures and algorithms.",
            "Build practical projects.",
            "Learn tools related to your career.",
            "Create a portfolio and prepare for interviews."
        ]
    )
