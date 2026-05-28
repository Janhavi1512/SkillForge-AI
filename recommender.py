from data import skills_db

def get_gap(user_skills, role):
    required_skills = skills_db[role]

    missing = []
    for skill in required_skills:
        if skill.lower() not in [s.lower() for s in user_skills]:
            missing.append(skill)

    return missing