from . import app
from . import models
from flask import render_template , request , Response , redirect , url_for
@app.route('/')
def Home() : 
    return redirect("/menu-selection")
@app.route("/menu-selection")
def main() : 
    try: 
        return render_template("menu.html")
    except Exception as e : 
        return Response(e , status=404)

@app.route("/confirm")
def regiter() : 
    try: 
        return render_template("confirm.html")
    except Exception as e : 
        return Response(e , status=404)


@app.route("/done")
def login() : 
    try: 
        return redirect("/menu-selection")
    except Exception as e : 
        return Response(e , status=404)
