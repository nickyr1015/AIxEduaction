from datetime import datetime
def get_textbook_title(textbook_name):
    prompt = f"""
    Write a textbook title for the following topic: {textbook_name}.
    Only return the textbook title in your response.
    """
    return prompt

def get_textbook_table(textbook_name):
    prompt = f"""
    Write a table of content of {textbook_name}, table of content should only include the chapters,
    only return a python list of string in your response."
    """
    return prompt

def get_textbook_preface(textbook_title, textbook_table_of_content):
    prompt = f"""
    Write a textbook preface for the following textbook: {textbook_title}
    Author's Name: Emory University CS Department
    Date: {datetime.now().date()}
    This textbook has the following table of content:
    {textbook_table_of_content}

    Only return the preface in your response. Do not use Markdown format.
    """
    return prompt





