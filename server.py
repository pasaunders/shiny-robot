from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'supersecret'


@app.route('/')
def index():
    if 'viewed' not in session:
        session['viewed'] = 0
    session['viewed'] += 1
    return render_template('index.html')


app.run(debug=True)
