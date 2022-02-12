from flask import Flask, request, make_response
from threading import Thread
import database
import os
import pandas as pd

app = Flask('')
@app.route('/')
def main():
    return "API DB IS LIVE!"

@app.route("/api/add_wallet", methods=['POST'])
def api_add_wallet():
    args = dict(request.args)
    response = database.add_wallet(args["wallet"], args["user_id"], args["user_name"], args["date"])
    if (response == 0):
        response = 400
    else:
        response = 200
    return make_response("ok", response)

@app.route("/api/get_wallet", methods=['GET'])
def api_get_wallet():
    args = dict(request.args)
    response = database.get_wallet(args["user_id"]).fetchall()
    result = {"user_id":args["user_id"], "wallet":response[0][0]}
    return make_response(result)

@app.route("/api/update_wallet", methods=['POST'])
def api_update_wallet():
    args = dict(request.args)
    response = database.update_wallet(args["wallet_address"], args["user_id"], args["date"])
    if (response == 0):
        return make_response(400)
    else:
        return make_response(200)


def db_export_excel():
        os.system("bash convert_to_csv.sh")
        read_file = pd.read_csv ("./whitelist.csv")
        read_file.to_excel ('./whitelist.xlsx', index = None, header=True)

app.run(host="0.0.0.0", port=5150)
