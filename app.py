from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from mail import send_mail

# Configs 
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

ENV = 'prod'
if ENV  == "dev":
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://michelle:admin@localhost/lexus'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xzmoqaymzftpgf:7355ae2a45c9e4aaeb1d39c2205286706209f236164f30f4c8195d6207b93b86@ec2-3-229-11-55.compute-1.amazonaws.com:5432/d86g23t3tnnd05'

# database 
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
        send_mail(customer, rating, dealer, comments)
        return render_template('success.html')
    return render_template('index.html', message="You have already submitted feedback")

# running
if __name__ == '__main__':
    app.run()