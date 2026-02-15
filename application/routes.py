from . import app
from . import models
from flask import render_template , request , Response , redirect , url_for

@app.route('/')
def Home() : 
    return redirect("/menu-selection")


@app.route("/menu-selection")
def main() : 
    try: 
         
        return render_template("menu-selection.html")
        
    except Exception as e : 
        return Response(e , status=404)



@app.route("/confirm")
def regiter() : 
    try: 
        return render_template("confirm.html")
    except Exception as e : 
        return Response(e , status=404)




@app.route("/done")
def done() : 
    try: 
        return render_template("done.html")
    except Exception as e : 
        return Response(e , status=404)

