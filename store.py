import requests
import pandas as pd
from fastapi import FastAPI

def request(URL : str):
    return requests.get(URL)

def get_status(URL : str):
    r = request(URL)
    return r.status_code

def read_request_json(URL : str):
    r = request(URL)
    return r.json()

def get_categories():
    r = request('https://api.escuelajs.co/api/v1/categories')
    if get_status('https://api.escuelajs.co/api/v1/categories') != 200:
        raise Exception("Conecction error")
    jsonr = read_request_json('https://api.escuelajs.co/api/v1/categories')
    for category in jsonr:
        print(category['name'])


def csv_to_pandas(csv):
    df = pd.read_csv(csv)
    return df

app = FastAPI()

@app.get("/")
def SayHello():
    return f'Hello World!!!'

@app.get("/game/RPS")
def initRPSGame():
    return f'Starting the game...'