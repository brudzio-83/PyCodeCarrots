from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/agnieszka")
def agnieszka():
	return "Hej Agnieszka"

@app.route("/potega/<int:a>")
def potega(a):
	return str(a*a)

if __name__ == "__main__":
    app.run()

