import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Where is the API key?")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

def llm_answer(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response = client.chat.completions.create(model=model, messages=messages)
    ans=response.choices[0].message.content
    return ans

bad_promt = """
   #Role:
   you are support assistant at a mobile/laptop company.

   #Task:
   You have to classify the issue in a category.

   #Constraints:
   you have to classify the issue in one of three categories namely billing, technical, return .

   #Output Format:
   Your answer should be in one word only. The one word should be one of the three categories mentioned in constraints.

   #Example:
   for instane if user complain says he wants to refund then the category is Return

   #Fallback:
   it the issue is unrelated to any of the categories mentioned in constraints then you have to say "Other"





  This is a user complaint:
  my friend left me.

"""





print(llm_answer(bad_promt))