import requests
import json
from knowledge import get_info

def quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

def teachme(query, language=None):
  answer = get_info(query, language)
  return answer



