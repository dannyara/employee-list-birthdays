from datetime import datetime
from flask import Flask, jsonify, request
from werkzeug.http import HTTP_STATUS_CODES

app = Flask(__name__)


def success_response(data):
    response = jsonify(data)
    response.status_code = 200
    return response


# based on https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis token requests section
def error_response(status_code, message=None):
    payload = {'error': str(status_code) + ': ' + HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response


@app.route("/marco", methods=['get'])
def marco():
    response = {
        "message": "polo"
    }
    return success_response(response)


@app.route("/birthday", methods=['post'])
def birthday():
    birthdays = []
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        employee_list = request.json.get('employeeList')
        if not employee_list:
            return error_response(400, 'Invalid birthday input')
        print(employee_list)
        month = datetime.now().strftime('%m')  # get month in "mm" format
        for employee in employee_list:
            dob = employee["dob"]
            birthday_month = dob[0:2]
            if int(birthday_month) > 12:
                return error_response(400, "Invalid Input, birthday should be entered in mm-dd-yyyy format")

            if dob[0: 2] == month:
                birthdays.append(employee['name'])
        response = {
            'Birthdays this month': birthdays
        }
        return success_response(response)
    return error_response(400, "Invalid Input, make sure headers are set to 'application/json'")


if __name__ == '__main__':
    app.run()
