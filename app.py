import flask as Flask

app= Flask(__name__)

@app.route("/wish")

def pleaseWish():
  return "Heloow, Jenkins"


if __name__ =="__main__":
  app.run(host="0.0.0.0",port="5000")
