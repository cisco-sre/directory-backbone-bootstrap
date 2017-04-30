# This contains our directory directory; since it is a bit messy to use the @app.route
# decorator style when using application factories, all of our routes are
# inside blueprints.
#
# You can find out more about blueprints at
# http://flask.pocoo.org/docs/blueprints/
from flask import Blueprint, render_template, url_for, request, abort

from database import mongo, jsonify

# Create blueprint object
directory = Blueprint('directory', __name__)

@directory.route('/', methods=['GET','POST'])
def directory_index():
    return 

@directory.route('/employees/<int:manager_id>/reports', methods=['GET'])
def employees_by_manager(manager_id):
    managers_employees = mongo.db.employee.find({'managerId':manager_id})
    employees = []
    for employee in managers_employees:
        employees.append(employee)

    return jsonify(employees)


@directory.route('/employees/<int:employee_id>', methods=['GET'])
def employee_by_id(employee_id):
    employee = mongo.db.employee.find_one_or_404({'id':employee_id})
    return jsonify(employee)


@directory.route('/employees', methods=['GET'])
def employees_all():
    result = mongo.db.employee.find()

    if result.count() == 0:
        from database import init_db
        init_db()
        result = mongo.db.employee.find()

    employees = []
    for employee in result:
        employees.append(employee)

    return jsonify(employees)


