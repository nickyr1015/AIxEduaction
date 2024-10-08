def get_chapter_objective(chapter_title):
    prompt = f"""
    Generate a learning objective for this chapter: {chapter_title}.
    """
    return prompt

def get_chapter_section(chapter_objective):
    prompt = f"""
    Based on the learning objective for this chapter: {chapter_objective}.
    Create a list of sections for the learner. Each section represents a specific concept or knowledge.
    Return in a python list.
    """
    return prompt

def get_chapter_summary(chapter_title, chapter_objective, chapter_section):
    prompt = f"""
    Create a review summary for this chapter: {chapter_title}
    The summary should be able to satisfy the leaning objective: {chapter_objective}
    You should refer to the following content: {chapter_section}
    """
    return prompt

