import sys

from read_module import img_read
from ocr_module import parse_text
from skills_module import parse_skills
from summary_module import job_fit_by_skills


if __name__ == "__main__":
    path = str(sys.argv[1])
    path = "./examples/example1.png"
    img = img_read(path)
    texts = parse_text(img)
    skills = parse_skills(img, texts)
    position = 'Area Sales Manager'


    for skill in skills:
        print(f'{skill[0]}, grade: {skill[2]}, in percentage: {skill[1]}')
    print()
    print(f'Is the candidate suitable for the {position} position?')
    print(job_fit_by_skills(skills, position))