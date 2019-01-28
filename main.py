import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, Response

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get('VERIFY_TOKEN')


@app.route('/sub', methods=['GET'])
def get():
    verify_token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    mode = request.args.get('hub.mode')
    if mode == 'subscribe' or mode == 'unsubscribe':
        if verify_token == VERIFY_TOKEN:
            result = None if challenge == None else challenge.replace('\n', '') if '\n' in challenge else challenge
            r = Response(response=result, status=200)
            r.headers['Content-Type'] = 'text/plain'
            return r
        else:
            return  Response('Bad request!', 404)
    else:
        return Response('Bad request!', 404)

@app.route('/sub', methods=['POST'])
def post():
    data = request.data
    soup = BeautifulSoup(data, 'lxml')
    urls = [i.find('link').get('href') for i in soup.find_all('entry')]
    return Response(response='ok', status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
