from flask import Flask, jsonify, after_this_request,request
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData,select, insert
from sqlalchemy.orm import Session
import random, string
import sqlalchemy as db

app = Flask(__name__)
connection_string = "mysql+mysqlconnector://eqnt5ta63bdwrcz4:ypmx7xsa9cihwetv@vkh7buea61avxg07.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/qw2nna0so23shxp5"
engine = create_engine(connection_string)
metadata = MetaData()
conn = engine.connect() 
users = db.Table('users', metadata,
              db.Column('user_id', db.String(255),primary_key=True),
              db.Column('coupon_code', db.String(255), nullable=False)
              )

metadata.create_all(engine) 

@app.route('/')
def hello():
	@after_this_request
	def add_header(response):
		response.headers.add('Access-Control-Allow-Origin', '*')
		return response

	clientBalance = request.args.get('balance')
	clientAccount = request.args.get('account')
	balance = float(clientBalance) if clientBalance else 0
	account = clientAccount if clientAccount else 'invalid'
	users = metadata.tables['users']
	stmt = select((users.columns.coupon_code)).where( users.columns.user_id==account)
	dbCouponCode = conn.execute(stmt).fetchall()
	couponCode = ''
	if dbCouponCode:
		return {'couponCode':dbCouponCode[0][0]}
	else:
		if balance == 0:
			couponCode = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
			users = metadata.tables['users']
			values_list = [{'user_id':account, 'coupon_code':couponCode}]
			conn.execute(insert(users),values_list)		
		else:
			couponCode = 'Invalid Balance'
	args = request.args

	jsonResp = {'couponCode': couponCode}
	return jsonify(jsonResp)

if __name__ == "__main__":
    app.run()