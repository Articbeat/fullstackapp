#crud app
#create
# - first_name, 
# - last_name,
# - email
from flask import Flask, request, jsonify
from config import app, db
from models import contact

if __name__ == '__main__':