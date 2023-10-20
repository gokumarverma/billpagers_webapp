from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1> This is My first Webapp </h>"

@app.route("/puppy/<name>")
def puppy(name):
    return "<h1>Seems your puppy name is {} </h2>".format(name)


@app.route("/puppy_latin/<name>")
def puppy_latin(name):
    if name[-1]=="y":
        l_name=name.replace("y","iful")
    else:
        l_name=name+"y"
    return '<h1>hi {}!! Your latin name is {}</h1>'.format(name,l_name)
    
if __name__ == "__main__":
    app.run(debug=True)
