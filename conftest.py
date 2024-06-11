import pytest
from requests import Session
from json import loads

@pytest.fixture(scope="function")
def getKeyShopperId():
    session=Session()
    # session.headers.update({"content-type":"appliction/json"})
    session.headers.update({"Content-Type": "application/json"})
    payload={
            # "email":"syedmaheen687@gmail.com",
            "email":"alamsahdab786@gmail.com",
            # "password": "1Cd19ec14$",
            "password": "Nagma@123",
            "role": "SHOPPER"
             }

    response=session.post(r"https://www.shoppersstack.com/shopping/users/login",json=payload)
    r=loads(response.text)
    
    yield r['data']['jwtToken'],r['data']['userId']