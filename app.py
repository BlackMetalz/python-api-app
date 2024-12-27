import json
import os
from flask import Flask, jsonify, request
import configparser

app = Flask(__name__)

employees = [
 { 'id': 1, 'name': 'Ashley' },
 { 'id': 2, 'name': 'Kate' },
 { 'id': 3, 'name': 'Joe' }
]

nextEmployeeId = 4

# Hardcoded credentials (bad practice - for testing gitleaks)
DB_PASSWORD = "superSecretPass123!@#"
API_KEY = "sk_live_51HG7OkLPkHZV4VVHJVhVBc9DQE3"
GITHUB_TOKEN = "ghp_kj2h3k4j2h3k4jh23k4jh23k4jh23k4j"



@app.route('/secret', methods=['GET'])
def get_secret():
    # if not config.has_section('database'):
    #     return jsonify({'error': 'Configuration not found'}), 404
    
    # secret_data = {
    #     'database_host': config['database']['database_host'],
    #     'database_user': config['database']['database_user'],
    #     'database_pass': config['database']['database_pass']
    # }
    # return jsonify(secret_data)
    try:
        with open('config.ini', 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return 'Config file not found', 404

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World! From Version v0.0.5'

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist'}), 404
    return jsonify(employee)

def get_employee(id):
    return next((e for e in employees if e['id'] == id), None)

def employee_is_valid(employee):
    for key in employee.keys():
        if key != 'name':
            return False
    return True

@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId
    employee = json.loads(request.data)
    if not employee_is_valid(employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400

    employee['id'] = nextEmployeeId
    nextEmployeeId += 1
    employees.append(employee)

    return '', 201, { 'location': f'/employees/{employee["id"]}' }

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id: int):
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404

    updated_employee = json.loads(request.data)
    if not employee_is_valid(updated_employee):
        return jsonify({ 'error': 'Invalid employee properties.' }), 400

    employee.update(updated_employee)

    return jsonify(employee)

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
    global employees
    employee = get_employee(id)
    if employee is None:
        return jsonify({ 'error': 'Employee does not exist.' }), 404

    employees = [e for e in employees if e['id'] != id]
    return jsonify(employee), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
