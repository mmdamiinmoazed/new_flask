try : 
    from application import app

    if __name__ == "__main__" : 
        app.run(debug=True)


    else : 
        raise RuntimeError("got an error in application when it wanted to run")
except Exception as e  : 
    print(f"Error detail : {e}")
    