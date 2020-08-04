# render_template accesses HTML file stored somewhere in Python application
from flask import Flask, render_template

app = Flask(__name__)

"""
Python decorator that Flask provides to assign URLs in our app to functions easily.
@app that whenever a user visits app domain at the given .route(),
execute the home() function.
"""
@app.route('/')
# define what web will do
def home():
    return render_template("home.html")

@app.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run(debug=True)
