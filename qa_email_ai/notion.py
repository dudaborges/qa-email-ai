import csv
import os

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
          question = item['properties']['Pergunta']['title'][0]['text'][
              'content'
          ]
          response_question = item['properties']['Resposta']['rich_text'][0][
              'text'
          ]['content']

          result = {'question': question, 'response': response_question}
          data_amadeus.append(result)

      return data_amadeus
  except Exception as e:
      print(f'[ERROR] Error fetching data from the database: {e}')


data_amadeus = fetch_database_items()
csv_file_path = './assets/data_amadeus.csv'
csv_headers = ['question', 'response']

try:
  with open(
      csv_file_path, mode='w', encoding='utf-8', newline=''
  ) as csv_file:
      writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
      writer.writeheader()
      writer.writerows(data_amadeus)
except Exception as e:
  print(f'[ERROR] Error writing to CSV: {e}')
