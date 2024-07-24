from flask import Flask, render_template
from flask_vercel import Vercel

app = Flask(__name__)
vercel = Vercel(app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
