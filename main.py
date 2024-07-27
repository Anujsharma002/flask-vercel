from flask import Flask

app = Flask(__name__)

@app.route('/')
def first():
    return "first message"
@app.route('/intial/<string:slug>')
def sl(slug):
    return f"hello {slug}"
if __name__ == "__main__":
 app.run(debug=True)