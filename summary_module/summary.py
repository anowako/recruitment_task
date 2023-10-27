import os
import replicate

os.environ['REPLICATE_API_TOKEN'] = 'r8_7xHduGY2cOmTMQuLiSPesSrOojIebLU0CA2WX'

def job_fit_by_skills(skills, job_titte):
    skills_str = " "
    for skill in skills:
        skills_str += f'{skill[0]}'
    
    prompt = f'Answer me, yes or no in 2-3 sentences. Person with only these skills: {skills} is suitable for the position of {job_titte}?'

    output = replicate.run("meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3",
                       input = {'prompt': prompt,
                       'temperature': 0.1, 'top_p':0.9, 'max_length':128, 'repetition_penalty':1})
    
    response = ""
    for i in output:
        response += i

    return response