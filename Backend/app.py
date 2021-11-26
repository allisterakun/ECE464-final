import subprocess
from flask import Flask
# from subprocess import run # run script to load tables in
import pymysql
import os


app = Flask(__name__)

@app.route("/")
def index():
    print("Enter password:")
    password = input()
    os.system("mysql -u root -p"+ password +" < .\\b.sql ")

    # db = pymysql.connect("localhost", "user1", "PASSWORD", "ece464")

    os.system("mysql -u root -p" + password + " < .\\schema.sql")

    return "success"

if __name__ == "__main__":
    app.run()