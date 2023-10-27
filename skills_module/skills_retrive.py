from .skill_level_detection import match_skills_with_bars
from .skills_detection import retrive_skills

def parse_skills(img, texts):
    skills = retrive_skills(texts)
    skills = match_skills_with_bars(img, skills)
    return skills