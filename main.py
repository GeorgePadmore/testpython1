from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Password is found here"




if __name__ == "__main__":
    app.run(debug=True)



