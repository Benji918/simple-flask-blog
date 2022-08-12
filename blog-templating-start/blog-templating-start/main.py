import requests
from flask import Flask, render_template

app = Flask(__name__)
BLOG_URL = 'https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(url=BLOG_URL)
all_posts = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    return render_template('post.html', id=post_id, posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
