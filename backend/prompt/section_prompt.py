def get_section_description(section_name):
    prompt = f"""
    Write a description for this concept: {section_name}.
    Do not return in markdown format.
    """
    return prompt

def get_section_example(section_name, section_description):
    prompt = f"""
    Use an example to explain the following concept: {section_name}.
    The example should refer to the concept description: {section_description}
    Do not return in markdown format.
    """
    return prompt