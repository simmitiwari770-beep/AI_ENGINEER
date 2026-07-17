import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    address:str
    issue:str
schema=Ticket.model_json_schema()
response_format={
    "type": "json_object"
}
system_prompt=f"""
Extract the personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""

message_system={
    "role": "system",
    "content": system_prompt
}


text="hello my name is virat .I have an iphone that is stop working at all . my adress is delhi.my email is simmi@example.con and my phone number is 1234567890. I want to know how to fix it. please help me"
prompt=f"""Extract all the personal information from the text and return it in json format. text is:
 {text}
 """


# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages,response_format=response_format)
answer=response.choices[0].message.content
print(answer)

import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.issue)