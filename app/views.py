from app import app
from flask import render_template, request

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # validation
        if customer == '' or dealer == '':
            return render_template('index.html', message="Please Enter Required Fields")
    return render_template('success.html')