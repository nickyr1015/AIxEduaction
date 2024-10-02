def get_course_description(course_name):
    prompt = f"""
{course_name}
"""
    return prompt

def get_course_syllabus(course_name):
    prompt = f"""
I want to get a textbook syllabus for the following course:
{course_name}
"""
    return prompt


