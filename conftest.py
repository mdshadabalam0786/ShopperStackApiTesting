import pytest
from requests import Session
from json import loads
session=Session()
@pytest.fixture(scope="function")
def getKeyShopperId():
    
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

'''getAllAddressId is a fixture to returnning the addressid whenever need..'''
@pytest.fixture(scope='function')
def getAllAddressId(getKeyShopperId):
    session.headers.update({"Authorization":f"Bearer {getKeyShopperId[0]}"})
    response=session.get(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/address")
    r=loads(response.text)
    allAddressId=[]
    
    for i in range(len(r['data'])):
        allAddressId.append(r['data'][i]['addressId'])
    yield allAddressId