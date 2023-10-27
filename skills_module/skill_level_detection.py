import cv2

def find_rectangles(image, boundries=None):
    possible_rectangles = list()

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray_image, 200, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        pbr = w*h
        pp = cv2.contourArea(cnt)
        s =  pp/pbr

        if s > 0.65:
            if boundries:
                max_x, min_x, max_y, min_y = boundries
                if x <= max_x and x >= min_x and y <= max_y and y >= min_y:
                    possible_rectangles.append([x,y,w,h])
            else:
                possible_rectangles.append([x,y,w,h])

    return possible_rectangles


def percentage_to_level(percentage):
    if percentage <= 20: return 1
    if percentage <= 40: return 2
    if percentage <= 60: return 3
    if percentage <= 80: return 4
    return 5


def match_skills_with_bars(image, skills):
    max_y = skills[-1][0][0][1] + 30
    min_y = skills[0][0][3][1] - 30
    min_x = max(skills, key=lambda skill: skill[0][2][0])[0][2][0]
    max_x = 10**5

    boundries = (max_x, min_x, max_y, min_y)
    rectangles = find_rectangles(image, boundries)
    rectangles = sorted(rectangles, key=lambda rec: rec[1])

    percentages = list()
    flag = False
    max_bar_len = max(rectangles, key= lambda rec: rec[2])[2]

    current_rec = rectangles[0]
    for rec in rectangles[1:]:
        rec_len = rec[2]
        if not flag:
            if abs(rec_len - max_bar_len) > 2:
                percentage = (current_rec[2] - rec[2]) / current_rec[2] * 100
                flag = True
            else:
                percentage = 100
            percentages.append(percentage)
        else:
            flag = False
        current_rec = rec

    skills = [(skill[1], percentages[i], percentage_to_level(percentages[i])) for i, skill in enumerate(skills)]

    return skills
 