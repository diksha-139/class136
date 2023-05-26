from flask import Flask,jsonify

app = Flask(__name__)
@app.route("/")
def home():
    return "x"

 # @app.route("/yuppie") # def yahoo(): # name=request.args.get("thik") # return jsonify({ # "data":name # }),200 
 # 
app.run(debug=True)