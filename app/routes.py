from flask import json, jsonify
from app import app
from app import db
from app.models import Menu

@app.route('/')
def home():
    return jsonify({ 
        "status": "ok",
        "message": "🚀 Welcome to the CI/CD-powered Flask app using GitHub Actions and Railway!"
    })

@app.route('/menu')
def menu():
    today = Menu.query.first()
    if today:
        body = { "today_special": today.name }
        status = 200
    else:
        body = { "error": "Sorry, the service is not available today." }
        status = 404
    return jsonify(body), status

@app.route('/status-check')
def status_check():
    return jsonify({ 
        "status": "success",
        "info": "✅ This route was added to test the CI/CD deployment using GitHub Actions and Railway."
    })
