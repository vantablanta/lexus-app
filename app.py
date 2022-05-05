from flask import Flask, render_template, request
from config import config_options
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config_options['dev'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    """"""
    __tablename__='feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, rating, comments) :
        self.customer = customer
        self.dealer = dealer
        self.comments = comments
        self.rating = rating


#  viewws 
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

    if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
        data = Feedback(customer, dealer, rating, comments)
        db.session.add(data)
        db.session.commit()
        return render_template('success.html')
    return render_template('index.html', message="You have already submitted feedback")


if __name__ == '__main__':
    app.run()