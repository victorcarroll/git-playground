import requests
import os
from flask import Flask, render_template

trelloapp = Flask(__name__)

#Module2 project #
APP_KEY = os.environ.get('APP_KEY')
APP_TOKEN=os.environ.get('APP_TOKEN')
# APP_KEY= 'bb61abc465f91ddcefe71b425ff32869'
# APP_TOKEN= 'cb7c2516b552d93d890d7517775620bb9f9ef43b9cf93ed595ba420fd1e3ce56'
board_id= '5ef1186ddea5ff1b03e085e6'
list_id_ToDo = '5ef1186d26a8d939ea575069'
list_id_Pending = '5ef1186d2fd57d026f03add0'
list_id_Done = '5ef1186dcbda554f16c6d66f'
card_with_victor = '5ef8791423ec3b39c593b662'
card_tv = '5ef1186efc0b5b3a63063ecd'

def get_card():

    url = 'https://api.trello.com/1/cards/5ef1186e6521d1052350ceab'
    headers = {"Accept": "application/json"}
    query = {"key": APP_KEY, "token": APP_TOKEN}

    response=requests.request("GET", url, headers=headers, params=query)
    print(APP_KEY)
    print(APP_TOKEN)
    return response.text

#print(get_card())

def get_all_cards():
    url = f'https://api.trello.com/1/boards/{board_id}/cards/'
    headers = {"Accept": "application/json"}
    query = {"key": APP_KEY, "token": APP_TOKEN}

    response=requests.request("GET", url, headers=headers, params=query)
    return response.text  

#print(get_all_cards())

def create_new_card():
    url = f'https://api.trello.com/1/cards/'
    headers = {"Accept": "application/json"}
    query = {"key": APP_KEY, "token": APP_TOKEN, "idList": list_id_ToDo, "name": '2nd Pair coding with Victor'}
    
    response=requests.request("POST", url, headers=headers, params=query)
    return response.text

#print(create_new_card())

def move_card_to_done():
    url = f'https://api.trello.com/1/cards/{card_tv}'
    headers = {"Accept": "application/json"}
    query = {"key": APP_KEY, "token": APP_TOKEN, "idList": list_id_Done}
  
    response=requests.request("PUT", url, headers=headers, params=query)
    return response.text
  
# print(move_card_to_done())