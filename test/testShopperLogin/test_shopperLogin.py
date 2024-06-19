from requests import Session
from json import loads

def test_shopperLoginValidCredential001(getKeyShopperId): 
    
    session=Session()
    session.headers.update({"content-type":"application/json"})
    payload={
            "email":"alamsahdab786@gmail.com",
            "password": "Nagma@123",
            "role": "SHOPPER"
             }
    
    response=session.post(r"https://www.shoppersstack.com/shopping/users/login",json=payload)
    print(response.text)
    # assert response.status_code==200,f"found this status actual from the server {response.status_code}"
    r=loads(response.text)
    print(r)
    assert r['statusCode']==200,f"found this status actual from the server {response.status_code}"
    assert r['message']=="OK",f"found this status actual from the server {r['message']}"
#======================================================================================================

def test_shopperLoginInValidCredential002(getKeyShopperId): 
    
    session=Session()
    session.headers.update({"content-type":"application/json"})
    payload={
            "email":"1alamsahdab786@gmail.com",
            "password": "Nagma@123",
            "role": "SHOPPER"
             }
    
    response=session.post(r"https://www.shoppersstack.com/shopping/users/login",json=payload)
    print(response.text)
    r=loads(response.text)
    print(r)
    assert r['statusCode']==401,f"found this status actual from the server {response.status_code}"
    assert r['message']=="UNAUTHORIZED",f"found this status actual from the server {r['message']}"
    assert r['data']=="Given user ID or password is wrong",f"found this status actual from the server {r['data']}"
    
