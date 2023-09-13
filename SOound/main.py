from flask import Flask, render_template, session, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/myform"
db = SQLAlchemy(app)

class Information(db.Model):
    email = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(40), unique=False, nullable=False, primary_key=True)


@app.route("/signup", methods= ['GET', 'POST'])
def signup():
    if (request.method=='POST'):
        email = request.form.get("email")
        password = request.form.get("password")

        detail = Information(email=email, password=password)
        db.session.add(detail)
        db.session.commit()
        
    return render_template("signup.html")

@app.route("/home")
def  home():
        return render_template("index.html")


app.run(debug=True)