import nltk

def check_if_below(upper_text_coord, lower_text_coord):
    upper_x1, upper_x2 = upper_text_coord[0][0], upper_text_coord[1][0]
    upper_y = upper_text_coord[0][1]
    lower_x = lower_text_coord[0][0] + 10
    lower_y = lower_text_coord[0][1]

    result = False
    if lower_x <= upper_x2 and lower_x >= upper_x1 and lower_y > upper_y:
        result = True
    return result

def join_texts(texts):
    output = list()
    spaces = list()
    flag = False

    y1 = texts[0][0][0][1]
    for text in texts[1:]:
        coordination = text[0]
        y2 = coordination[0][1]
        space = y2 - y1
        spaces.append(space)
        y1 = y2
    
    for i, space in enumerate(spaces):
        if not flag:
            if abs(max(spaces) - space) > 15:
                new_coordinations = [texts[i+1][0][0], texts[i+1][0][1], texts[i][0][1], texts[i][0][0]]
                new_content = f"{texts[i][1]} {texts[i+1][1]}"
                output.append([new_coordinations, new_content])
                flag = True
            else:
                output.append(texts[i])
        else:
            flag = False
    
    if not flag:
        output.append(texts[-1])
    return output


def retrive_skills(texts):
    skills_header = None
    below_headers = list()
    skills = list()

    # searching skills header in CV
    for text in texts:
        coordinations, content, _ = text
        content = [token.lower() for token in nltk.word_tokenize(content)]
        if 'skills' in content and len(content) == 1:
            skills_header = [coordinations, content]
            break

    # searching skills below header
    for text in texts:
        coordinations, content, _ = text

        if check_if_below(skills_header[0], coordinations):
            if content.upper() != content:
                skills.append([coordinations, content])
            else:
                below_headers.append([coordinations, content])

    skills = sorted(skills, key=lambda skill: skill[0][0][1])
    below_headers = sorted(below_headers, key=lambda header: header[0][0][1])

    max_y = below_headers[0][0][3][1]

    skills = [skill for skill in skills if skill[0][0][1] < max_y]
    skills = join_texts(skills)

    return skills
        

    

    
    



        
