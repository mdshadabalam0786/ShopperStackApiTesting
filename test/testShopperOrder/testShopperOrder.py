import pytest
from requests import Session
from json import loads
session=Session()
orderId=[]


def test_placeOrderFromCart(getKeyShopperId,getAllAddressId):
    session.headers.update({"Authorization":f"Bearer {getKeyShopperId[0]}"})
    session.headers.update({"content-type":"application/json"})
    payload={
            "address": {
                "addressId": f"{getAllAddressId[1]}",
                "buildingInfo": "kormangala",
                "city": "Bengaluru",
                "country": "India",
                "landmark": "near church",
                "name": "Moha shadab",
                "phone": "7050327920",
                "pincode": "560010",
                "state": "Karnataka",
                "streetInfo": "khairi Banka,ward no.03,Bisfi",
                "type": "home"
                        },
            "paymentMode": "COD"
            }
    response=session.post(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/orders",json=payload)
    print(response.text)
    assert response.status_code==201,f"response we got it from the server {response.status_code}"
    assert response.elapsed.seconds<=3, f"response we got it from the server {response.elapsed.seconds}"
    print(response.text)


def test_shopperOrderHistory(getKeyShopperId):
    
    session.headers.update({"Authorization":f"Bearer {getKeyShopperId[0]}"})
    session.headers.update({"content-type":"application/json"})
    response=session.get(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/orders")
    assert response.status_code==200,f"response we got it from the server {response.status_code}"
    assert response.elapsed.seconds<=3, f"response we got it from the server {response.elapsed.seconds}"
 
    r=loads(response.text)
    print(f"here the count of order list {len(r['data'])}")
    for i in range(len(r['data'])):
        if r['data'][i]['orderStatus']=="PLACED":
            orderId.append(r['data'][i]['orderId'])
        else:
            print(f"these list {r['data'][i]['orderId']} which already {r['data'][i]['orderStatus']}")
        
    print(f"this order id {orderId} need to change status..")




def test_updateOrderStatus(getKeyShopperId):
    session.headers.update({"content-type":"application/json"})
    session.headers.update({"Authorization":f"Bearer {getKeyShopperId[0]}"})
    a="CANCELLED"
    response=session.patch(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/orders/{int(orderId[0])}?status={a}")
    print(response.text)
    assert response.status_code==200,f"response we got it from the server {response.status_code}"
    assert response.elapsed.seconds<=3, f"response we got it from the server {response.elapsed.seconds}"
 

def test_generateInvoiceCopy(getKeyShopperId):
    session.headers.update({"content-type":"application/json"})
    session.headers.update({"Authorization":f"Bearer {getKeyShopperId[0]}"})
    response=session.get(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/orders/{int(orderId[0])}/invoice")
    print(response.status_code)
    assert response.status_code==200,f"response we got it from the server {response.status_code}"
    assert response.elapsed.seconds<=3, f"response we got it from the server {response.elapsed.seconds}"
 
