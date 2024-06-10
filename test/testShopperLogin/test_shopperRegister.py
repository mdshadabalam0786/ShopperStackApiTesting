import pytest
from requests import Session
import requests
from json import loads

session1=Session()
session1.headers.update({"content-type":"application/json"})
def test_shopperRegister001():
   
    print('''======================without giving the mobile number and try to validate======================''')
    payload={
                    "city": "bangalore",
                    "country": "india",
                    "email": "alamsahdab987@gmail.com",
                    "firstName": "shadab",
                    "gender": "MALE",
                    "lastName": "khan",
                    "password": "Khan@123",
                    "phone": 0,
                    "state": "string",
                    "zoneId": "ALPHA"
                    }
    response=session1.post(r"https://www.shoppersstack.com/shopping/shoppers",json=payload)
    r=loads(response.text)
    assert r['statusCode']==400,f"found this status actual from the server {r['statusCode']}"
    assert r['message']=='BAD_REQUEST',f"found this message actual from the server {r['message']}"
    assert r['data']['phone']=='The number is Not Valid',f"found this data actual from the server {r['data']['phone']}"




@pytest.mark.parametrize("value", [7, 2, 3, 4, 5, 6, 7])
def test_shopperRegister002(value):
    ''''handling the error using if elif condition.................'''
    session2 = requests.Session()
    print(f"==========checking the mobile number it should not start with {value}=====")
    
    payload = {
        "city": "bangalore",
        "country": "india",
        "email": "nagma123@gmail.com",
        "firstName": "shadab",
        "gender": "MALE",
        "lastName": "khan",
        "password": "Khan@123",
        "phone": int(str(value)+"150327916"),  # Ensure phone starts with value
        "state": "string",
        "zoneId": "ALPHA"
    }

    response = session2.post(r"https://www.shoppersstack.com/shopping/shoppers", json=payload)
    r = response.json()  # Parse the JSON response
    
    # Printing the response for debugging purposes
    print(response.text)
    if r['statusCode'] == 400:
    # Assertions to validate the response
        assert r['statusCode'] == 400, f"Expected status code 400, but found {r['statusCode']}"
        assert r['message'] == 'BAD_REQUEST', f"Expected message 'BAD_REQUEST', but found '{r['message']}'"
        assert r['data']['phone'] == 'The number is Not Valid', f"Expected phone validation message 'The number is Not Valid', but found '{r['data']['phone']}'"
    
    elif r['statusCode'] == 201:
    # Assertions to validate the response
        assert r['statusCode'] == 201, f"Expected status code 201, but found {r['statusCode']}"
        assert r['message'] == 'Created', f"Expected message 'Created', but found '{r['message']}'"
    elif r['statusCode'] == 409:
    # Assertions to validate the response
        assert r['statusCode'] == 409, f"Expected status code 409, but found {r['statusCode']}"
        assert r['message'] == 'CONFLICT', f"Expected message 'CONFLICT', but found '{r['message']}'"
        assert r['data'] == "Given Email ID or Phone number already used", f"Expected Given Email ID or Phone number already used, but found {r['data']}"
        
    








