import requests as r
from utils import API_HOST
import json
import pandas as pd
import os

def add_wallet(wallet, user_id, user_name, date):
    response = r.post(
        url =  f"{API_HOST}/api/add_wallet", 
        params = {"wallet":wallet, "user_id":user_id,"user_name":user_name,"date":date}
        )
    if (response.ok):
        return (1)
    return (0)

def get_wallet(user_id):
    response = r.get(url =  f"{API_HOST}/api/get_wallet", params = {"user_id":user_id})
    if (response.ok):
            data = response.json()
            return(data["wallet"])
    return (0)

def update_wallet(wallet, user_id, user_name, date):
    response = r.post(url = f"{API_HOST}/api/update_wallet",
                                params = {"wallet":wallet, "user_id":user_id,"user_name":user_name,"date":date})
    if (response.ok):
        return (1)
    return (0)

def db_export_excel():
        response = r.get(url = f"{API_HOST}/api/csv")
        if (response.ok):
            try :
                csv_file = open("./whitelist.csv", "w")
                csv_file.write(response.text)
                csv_file.close()
                read_file = pd.read_csv("./whitelist.csv")
                read_file.to_excel("./whitelist.xlsx", index = None, header = True)
                return (1)
            except:
                return (0)
        else:
            return (0)

def db_cleanup_excel():
    os.system("rm ./whitelist.csv")
    os.system("rm ./whitelist.xlsx")

