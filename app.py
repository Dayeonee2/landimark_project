from flask import Flask, request, jsonify, url_for, redirect, flash, session
from flask import render_template
from flask_restful import Resource, Api
# import psycopg2 PostgreSQL 직접 연결시 필요
from credentials import DB
from itsdangerous import Signer, BadSignature
from supabase import create_client, Client


app = Flask(__name__)
app.secret_key='mysecretkey'

secret_key = 'mysecretkey'
signer = Signer(secret_key)

# def get_db_connection():
#     conn = psycopg2.connect(
#         host=DB['host'],
#         database=DB['database'],
#         user=DB['user'],
#         password=DB['password'],
#         port=DB['port']
#     )
#     return conn

@app.route('/logout')



@app.route('/', methods=['GET','POST'])


    
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/verify', methods=['POST'])
def verify():
    signed_data = request.form.get('signed_data')
    
    try:
        # 서명된 데이터를 검증
        original_data = signer.unsign(signed_data)
        return f"서명이 유효합니다. 원본 데이터: {original_data.decode('utf-8')}"
    except BadSignature:
        return "서명이 유효하지 않습니다!"





if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)