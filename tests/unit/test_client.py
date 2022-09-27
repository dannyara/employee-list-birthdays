import pytest
import json


def test_request_example(client):
    res = client.get("/marco")
    assert res.status_code == 200
    output = json.loads(res.data)

    assert "polo" in output['message']


def test_input(client):
    headers = {"Content-Type": "application/json"}
    data = {
        'employeeList': [
            {
                'name': 'Test User',
                'dob': '01-01-2011'
            },
            {
                'name': 'birthday boy',
                'dob': '09-02-1992'
            },
        ]
    }

    res = client.post("/birthday", headers=headers, json=data)
    output = json.loads(res.data)
    print(output)
    assert res.status_code == 200
    assert "Birthdays this month" in output
    assert output['Birthdays this month'] == ['birthday boy']


