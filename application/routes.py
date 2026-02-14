from . import app
from . import models
from flask import render_template , request , Response


@app.route("/")
def main() : 
    return "Main"


@app.route("/register")
def regiter() : 
    return "register"



@app.route("/login")
def login() : 
    return "log-in"




@app.route("/login")
def login() : 
    return "log-in"





