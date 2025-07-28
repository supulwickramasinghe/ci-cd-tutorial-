from flask import Blueprint, render_template, request, jsonify
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({'message': 'Hello World!'})

@bp.route('/health')
def health():
    return jsonify({'status': 'healthy'})

# Add your other routes here
@bp.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        # Handle POST request
        data = request.get_json()
        # Your logic here
        return jsonify({'message': 'User created'})
    else:
        # Handle GET request
        return jsonify({'users': []})