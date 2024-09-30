import ast

def extract_table_of_content(input_string):
    start_index = input_string.index('[')
    end_index = input_string.rindex(']')
    list_str = input_string[start_index:end_index + 1]
    contents_list = ast.literal_eval(list_str)
    
    return contents_list