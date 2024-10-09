import os

def save_string_to_txt(directory, filename, content):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, filename)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"File saved to {file_path}")

def append_string_to_txt(directory, filename, content):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    file_path = os.path.join(directory, filename)
    
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Content appended to {file_path}")
