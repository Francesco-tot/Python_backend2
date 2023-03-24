import requests
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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

@app.get("/game",response_class = HTMLResponse)
async def game_home_start():
    return """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to gamers place !!!</title>
</head>
<body>
    <h1>Enjoy here with the games you can find :D</h1>
</body>
</html>"""