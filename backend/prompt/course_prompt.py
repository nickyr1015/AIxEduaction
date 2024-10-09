def get_course_title(course_name):
    prompt = f"""
    I want to build a Course for the learner.
    Give me the course name for this learning topic: {course_name}.
    """
    return prompt

def get_course_description(course_name):
    prompt = f"""
    Give me a description of this course: {course_name}.
    Do not include the Course Name at the begining.
    Do not return in Markdown format.
    """
    return prompt



