from . import app
from . import models , db
from flask import render_template , request , Response , redirect , url_for , make_response

@app.route('/')
def Home() : 
    return redirect("/menu-selection")


@app.route("/menu-selection")
def main() : 

        print("menu routes gets up")
        
        products = db.session.query(models.Product).all()
        
        print(products) 
        return render_template("menu-selection.html" , products = products)

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



@app.route("/add-product")
def add_product() : 
    return render_template("add_product.html")




@app.route("/delete-product")
def delete() : 
    print("up")
    products = db.session.query(models.Product).all()
    response = make_response(render_template("delete_product.html" , products = products ))
    return response
@app.route("/update-product")
def update_product() : 
    return render_template("update_product.html")


@app.route("/changed" , methods=['POST' , 'GET'])
def changed() : 
    if request.method == "POST" : 
        name = request.form.get("name")
        price = request.form.get("price")
        category = request.form.get("category")
        description = request.form.get("description")

        if name and price and category and description : 
            product = models.Product(_name=name , _price = price
                                 , _category = category , _description = description , 
                                 _stock = "ok" , _photo='img')
            db.session.add(product)
            db.session.commit()
        else : 
            pass
    else : 
            print("get method")
            current_product = request.form.get("product")
            print(current_product)
            
            db.session.delete(current_product)
            db.session.commit()
            print("deleted successfully")

    return redirect("/menu-selection")

