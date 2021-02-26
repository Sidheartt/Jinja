from flask import Flask, render_template
from datetime import date
import requests

app = Flask(__name__)


@app.route('/')
def home():
    today = date.today()
    return render_template('index.html', dam=today)


@app.route("/guess/<name>")
def guess(name):
    gen_url = f"https://api.genderize.io?name={name}"
    gen_response = requests.get(gen_url)
    gen_data = gen_response.json()
    gender = gen_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def blog(num):
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    blog_response = requests.get(blog_url)
    blog_data = blog_response.json()
    return render_template("blog.html", posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
