import requests
import os
from flask import Flask, render_template
import json
from dotenv import load_dotenv  #to invoke .env file
load_dotenv()

trelloapp = Flask(__name__)

#Module2 project #
#APP_KEY = os.environ.get('APP_KEY')  # take env variable from local system envor
#APP_TOKEN=os.environ.get('APP_TOKEN')

APP_KEY = os.getenv("APP_KEY")  # take .env from dotenv
APP_TOKEN = os.getenv("APP_TOKEN")

board_id= '5ef1186ddea5ff1b03e085e6'
list_id_ToDo = '5ef1186d26a8d939ea575069'
list_id_Pending = '5ef1186d2fd57d026f03add0'
list_id_Done = '5ef1186dcbda554f16c6d66f'
card_with_victor = '5ef8791423ec3b39c593b662'
card_tv = '5ef1186efc0b5b3a63063ecd'

def get_card():

    url = 'https://api.trello.com/1/cards/5ef1186efc0b5b3a63063ecd'
    headers = {"Accept": "application/json"}
    query = {"key": APP_KEY, "token": APP_TOKEN}

    response=requests.request("GET", url, headers=headers, params=query)
    print(APP_KEY)
    print(APP_TOKEN)
    return response.text

#print(get_card())

def get_all_cards_from_board():
    url = f'https://api.trello.com/1/boards/{board_id}/cards/'
    headers = {"Accept": "application/json"}
    query = {"key": APP_KEY, "token": APP_TOKEN}

    response=requests.request("GET", url, headers=headers, params=query)
    return response.text  

#print(get_all_cards_from_board())

def get_all_lists_from_board():
    url = f'https://api.trello.com/1/boards/{board_id}/lists/'
    headers = {"Accept": "application/json"}
    query = {"key": APP_KEY, "token": APP_TOKEN}

    response=requests.request("GET", url, headers=headers, params=query)
    return response.text  

#print(get_all_lists_from_board())

def create_new_card():
    url = f'https://api.trello.com/1/cards/'
    headers = {"Accept": "application/json"}
    query = {"key": APP_KEY, "token": APP_TOKEN, "idList": list_id_ToDo, "name": '2nd Pair coding with Victor'}
    
    response=requests.request("POST", url, headers=headers, params=query)
    return response.text

#print(create_new_card())

def move_card_to_done(card_id):
    url = f'https://api.trello.com/1/cards/{card_id}'
    headers = {"Accept": "application/json"}
    query = {"key": APP_KEY, "token": APP_TOKEN, "idList": list_id_Done}
  
    response=requests.request("PUT", url, headers=headers, params=query)
    return response.text

# print(move_card_to_done())

def change_card_status(card_name, new_list_status):
    print('HELLO')
    #print('DONE' + str(card_name) + ' : ' + str(new_list_status)) 


# app route that takes 2 params card_name and list_name (move from to do to done)
# through hyperlink click or box
# 2 methods, 1 to retrieve the card_id/card_name, 2nd to retrieve the list_id/list_name

def get_card_name_and_id():
    all_card_details = []
    all_card_details = json.loads(get_all_cards_from_board())
    for card in all_card_details:
        print(card['id'] + ' : ' + card['name'])

#get_card_name_and_id()

def get_list_name_and_id():
    all_list_details = []
    all_list_details = json.loads(get_all_lists_from_board())
    for list_status in all_list_details:
        print(list_status['id'] + ' : ' + list_status['name'])

#get_list_name_and_id()


