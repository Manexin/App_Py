from flask import Flask, render_template
import emoji

app = Flask(__name__)
print(emoji.emojize('Hello world 2 :tada:', use_aliases=True))

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
