from flask import Flask
from flask import request
from flask import render_template,jsonify,make_response
import json
import jwt
from functools import wraps
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash,check_password_hash
app=Flask(__name__)
auth=HTTPBasicAuth()
users={
    "********":generate_password_hash("*******")
}
@auth.verify_password
def verify_password(username,password):
    if username in users and \
            check_password_hash(users.get(username),password):
        return username
@app.route("/")
def main_page():
    data_tshirt = open("product.json")
    data_json_tshirt = json.load(data_tshirt)
    print(data_json_tshirt)
    l=list(reversed(list(data_json_tshirt.keys())))
    print(l)
    d={}
    for i in l:
        d[i]=data_json_tshirt[i]
    print(d)
    return render_template("Main_Page.html",product=d)
@app.route("/tshirts")
def tshirt_page():
    data_tshirt = open("tshirt.json")
    data_json_tshirt = json.load(data_tshirt)
    print(data_json_tshirt)
    l=list(reversed(list(data_json_tshirt.keys())))
    print(l)
    d={}
    for i in l:
        d[i]=data_json_tshirt[i]
    print(d)
    return render_template("tshirts.html",product=d)
@app.route("/watches")
def hoodies():
    data_tshirt = open("watches.json")
    data_json_tshirt = json.load(data_tshirt)
    print(data_json_tshirt)
    l=list(reversed(list(data_json_tshirt.keys())))
    print(l)
    d={}
    for i in l:
        d[i]=data_json_tshirt[i]
    print(d)
    return render_template("watches.html",product=d)
@app.route("/hoodie")
def hoodie():
    data_tshirt = open("hoodie.json")
    data_json_tshirt = json.load(data_tshirt)
    print(data_json_tshirt)
    l=list(reversed(list(data_json_tshirt.keys())))
    print(l)
    d={}
    for i in l:
        d[i]=data_json_tshirt[i]
    print(d)
    return render_template("hoodie.html",product=d)
@app.route("/product_main",methods=["GET","POST"])
@auth.login_required
def product_main():
    order_id=request.form.get("order_id")
    name=request.form.get("Name")
    price=request.form.get("Price")
    Image_link=request.form.get("Image_Link")
    type=request.form.get("Type")
    data=open("product.json")
    json_data=json.load(data)
    d=json_data
    if order_id==None:
        pass
    else:
        d[order_id]={'Name':name,'Price':price,'image_link':Image_link}
        writer=json.dumps(d,indent=5)
        with open("product.json","w") as f:
            f.write(writer)
    if type=="Tshirt":
        tshirt_data=open("tshirt.json")
        tshirt_json=json.load(tshirt_data)
        d=tshirt_json
        d[order_id]={'Name':name,"Price":price,"image_link":Image_link}
        writer=json.dumps(d,indent=5)
        with open("tshirt.json","w") as f:
            f.write(writer)
    if type=="Hoodie":
        print("Yes")
        tshirt_data=open("hoodie.json")
        tshirt_json=json.load(tshirt_data)
        d=tshirt_json
        d[order_id]={'Name':name,"Price":price,"image_link":Image_link}
        writer=json.dumps(d,indent=5)
        with open("hoodie.json","w") as f:
            f.write(writer)
    if type=="Watches":
        tshirt_data=open("watches.json")
        tshirt_json=json.load(tshirt_data)
        d=tshirt_json
        d[order_id]={'Name':name,"Price":price,"image_link":Image_link}
        writer=json.dumps(d,indent=5)
        with open("watches.json","w") as f:
            f.write(writer)
    return render_template("product_main.html")
@app.route("/product_detail",methods=["GET","POST"])
def product_detail():
    order_id=request.form.get("order")
    print(order_id)
    d={}
    print(order_id)
    if order_id=="" or order_id==None:
        pass
    else:
        data=open("product.json")
        json_data=json.load(data)
        d=json_data
    return render_template("test.html",product=d,t=order_id)
app.run(debug=True)
