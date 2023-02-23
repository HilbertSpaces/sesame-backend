# Getting Started the sesame-backend
The sesame-backend generates and serves the coupon_code to the sesame-coding-assignment if and only if the user balance is greater than 0. It stores this value to a coupon_code column on a MySQL db running as a service on Heroku.

# Running Locally

## (optional) setup virtualenv
python -m venv venv

## install all requirements
pip install -r requirements.txt

## run flask
export FLASK_APP=app
run flask