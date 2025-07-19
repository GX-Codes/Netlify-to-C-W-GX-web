from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print("hello")  # this will also print in the Render logs
    return "Hello from Python on Render!"

if __name__ == "__main__":
    app.run()