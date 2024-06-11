import pytest
from requests import Session
from json import loads

session=Session()
session.headers.update({"content-type":"application/json"})
addressId=[]

    
def test_addNewAddress(getKeyShopperId):
    session.headers.update({"Authorization": f"Bearer {getKeyShopperId[0]}"})
    payload={
                "addressId": 0,
                "buildingInfo": "banshankari 3rg street,block a",
                "city": "koccin",
                "country": "india",
                "landmark": "near church",
                "name": "string",
                "phone": "7050327911",
                "pincode": "847121",
                "state": "kerala",
                "streetInfo": "Place: electronic City phase 1 , bettadasanpura near church",
                "type": "home"
                }
    response=session.post(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/address",json=payload)
    r=loads(response.text)
    addressId.append(r['data']['addressId'])
    print(addressId)

def test_getParticularAddress(getKeyShopperId):
    response=session.get(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/address/{int(addressId[0])}")
    print(response.text)
    print(response.status_code)
    print(response.elapsed.total_seconds())
    

def test_getAllAddress(getKeyShopperId):
    session.headers.update({"Authorization":f"Bearer {getKeyShopperId[0]}"})
    response=session.get(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/address")
    print(response.text)
    r=loads(response.text)
    assert r['statusCode']==200,f"accpecting this response which we got from server {r['statusCode']}"
    assert r['message']=='Success',f"accpecting this response which we got from server {r['statusCode']}"
    # validating the address got added or not
    assert r['data'][-1]['addressId']==int(addressId[0]),f"accpecting this response which we got from server {r['data'][-1]['addressId']}"

@pytest.mark.skip
def test_deleteAddress(getKeyShopperId):
    session.headers.update({"content-type":"application/json"})
    session.headers.update({"Authorization":f"Bearer {getKeyShopperId[0]}"})
    response=session.delete(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/address/{int(addressId[0])}")
    assert response.status_code==204,f"accpecting this response which we got from server {response.status_code}"
    assert response.elapsed.total_seconds()<=3,f"accpecting this response which we got from server {response.elapsed.total_seconds()}"
    if response.ok:
        print("OK")
    
def test_updateAddress(getKeyShopperId):
    session.headers.update({"content-type":"application/json"})
    payload={
                "addressId": f"{int(addressId[0])}",
                "buildingInfo": "banshankari 3rg street,block a",
                "city": "koccin",
                "country": "india",
                "landmark": "near church",
                "name": "string",
                "phone": "9430833661",
                "pincode": "847121",
                "state": "kerala",
                "streetInfo": "Place: electronic City phase 1 , bettadasanpura near church",
                "type": "home"
        }
    response=session.put(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/address/{int(addressId[0])}",json=payload)
    print(response)
    print(response.text)
