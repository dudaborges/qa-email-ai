import os
import json

from datetime import datetime, timezone
from dotenv import load_dotenv
from notion_client import Client


load_dotenv()

NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DATABASE_ID = os.getenv('DATABASE_ID')

notion = Client(auth=NOTION_TOKEN)

data_amadeus = []
def fetch_database_items():
  try:
    api_response = notion.databases.query(database_id=DATABASE_ID)

    api_results = api_response.get('results', [])
    for item in api_results:
      question = item['properties']['Pergunta']['title'][0]['text']['content']
      response_question = item['properties']['Resposta']['rich_text'][0]['text']['content']
      
      result = {
        'question': question,
        'response': response_question
      } 
      data_amadeus.append(result)
    
    return data_amadeus
  except Exception as e:
    print(f'[ERROR] Error fetching data from the database: {e}')


data_amadeus = fetch_database_items()
with open('data_amadeus.json', 'w', encoding='utf-8') as json_file:
  json.dump(data_amadeus, json_file, ensure_ascii=False, indent=4)