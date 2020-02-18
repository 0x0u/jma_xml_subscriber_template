import os
import hmac
import hashlib
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
            return Response('Bad request!', 404)
    else:
        return Response('Bad request!', 404)


@app.route('/sub', methods=['POST'])
def post():
    sha1 = request.headers.get('X-Hub-Signature')
    if sha1:
        data = request.get_data(as_text=True)
        sig = 'sha1=' + hmac.new(bytes(VERIFY_TOKEN, 'UTF-8'), bytes(data, 'UTF-8'), hashlib.sha1).hexdigest()
        if sig == sha1:

            # 処理を書く
            # POSTされたAtomはdataに入っているのでBeautifulSoupなどでXMLをパースして遊ぶ

            return Response(response='ok', status=200)
        else:
            return Response(response='Bad request!', status=404)
    else:
        return Response(response='Bad request!', status=404)


if __name__ == '__main__':
    app.run(threaded=True)
