from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mydb.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


class User1(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProductName = db.Column(db.String(200))
    ProductPrice = db.Column(db.String(200))
    ProductWeight = db.Column(db.String(200))
    ProductOrigin = db.Column(db.String(200))


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = User1.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>',methods=["GET","POST"])
def update(id):
    user = User1.query.get_or_404(id)
    if request.method == 'POST':
        user.ProductName = request.form['ProductName']
        user.ProductPrice = request.form['ProductPrice']
        user.ProductWeight = request.form['ProductWeight']
        user.ProductOrigin = request.form['ProductOrigin']
        db.session.commit()
        return redirect('/')
    else:
        user1s = User1.query.all()
        page = 'updatehome'
        return render_template('home.html', page=page, user1s=user1s, user=user)
   


@app.route('/', methods=['GET', 'POST'])
def get():
    if request.method == "GET":
        user1s = User1.query.all()
        page ='home'
        user = User1(ProductName='',ProductPrice='',ProductWeight='', ProductOrigin='')
        return render_template('home.html', user1s=user1s, page=page, user=user)
    else:
        ProductName = request.form['ProductName']
        ProductPrice = request.form['ProductPrice']
        ProductWeight = request.form['ProductWeight']
        ProductOrigin = request.form['ProductOrigin']
        newUser1 = User1(ProductName=ProductName,ProductPrice=ProductPrice,ProductWeight=ProductWeight,ProductOrigin=ProductOrigin)
        db.session.add(newUser1)
        db.session.commit()
        return redirect('/')

import MongoDbConn


@app.route("/")
def index():
    cursor = MongoDbConn.read()
    product = []
    for item in cursor:
        product.append(item)
    print(product[1]["ProductName"])
    return render_template("main.html", datafortemplate = product[1])
    
if __name__ == "__main__":
    app.run(debug=True)