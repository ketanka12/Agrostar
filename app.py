from flask import Flask,render_template,request,jsonify,session,redirect,url_for
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column 


app = Flask(__name__,template_folder="template",static_folder="static")
CORS(app)



DB_USERNAME="root"
DB_PASSWORD="root"
DB_NAME="agrostar1"
DB_HOST="localhost"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# app.config["SQLALCHEMY_DATABASE_URI"]=f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

db=SQLAlchemy(app)

class Result(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]= mapped_column(String(100))
    price:Mapped[str]=mapped_column(String(200),nullable=False)
    Category:Mapped[str]=mapped_column(String(20))
  

with app.app_context():
    db.create_all()

@app.route("/")
def add():
    return render_template("addpost.html")

@app.route("/post", methods=["POST"])
def addpost():
    data = request.get_json()
    Rname = data["name"]
    Rprice = data["price"]
    RCategory=data["Category"]
    

    try:
        defalt = Result (name=Rname,price=Rprice,Category=RCategory,)
        db.session.add(defalt)
        db.session.commit()
        return jsonify({"msg": "user created"}), 201

    except Exception as e:
        return jsonify({"msg": "not created"}), 400




        





if __name__ == "__main__":
    app.run(debug=True)
