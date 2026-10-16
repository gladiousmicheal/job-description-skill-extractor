
def extract_skills(job_description):
    skills_list = [
        "Python",
        "SQL",
        "Excel",
        "Power BI",
        "Machine Learning",
        "Data Visualization",
        "Data Cleaning"
    ]

    found_skills = []

    for skill in skills_list:
        if skill.lower() in job_description.lower():
            found_skills.append(skill)

    return found_skills
