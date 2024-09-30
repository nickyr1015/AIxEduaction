from openai import OpenAI
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from util.extract_table_of_content import extract_table_of_content
config = get_config()
client = OpenAI(api_key=config['api_key'])

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a text book"},
    {"role": "user", "content": "Write a table of content of React (frontend framework), table of content should only include the chapters, only return in a python list of string"},
  ]
)

message = response.choices[0].message.content
table_of_content = extract_table_of_content(message)
for chapter in table_of_content:
    print(chapter)