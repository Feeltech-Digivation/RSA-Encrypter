import base64
import json

import rsa
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

cors = CORS()
cors.init_app(app)

public_key: rsa.PublicKey
with open('./public-key.pem','rb') as file:
    public_key = rsa.PublicKey.load_pkcs1(file.read())


def get_encrypted_message(message: str) -> str:
    return base64.b64encode(rsa.encrypt(message.encode(), public_key)).decode()


@app.route("/encrypt", methods=['POST'])
def encrypt():
    body = request.json
    return get_encrypted_message(json.dumps(body))
