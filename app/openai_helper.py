import openai
import app.helper as helper


def classify_question(question):
  openai.api_key = helper.get_settings("openai_key")
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "I'm a cloud support engineer. My main job is to classify the question based on these types\n1. Utilisation\n2.Security\n3.Recommendation\n4.Billing\n5.None\nbased on the classification I'll be assigning to appropriate cloud assistance to work on. I will return single or multiple classification based on the question. Questions should be only relevant to cloud service else return 5.None"
      },   
      {
        "role": "user",
        "content": question
      }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  
  if response['choices'][0]['message']['content']:
    return response['choices'][0]['message']['content']
  else:
    return "Error occurred"