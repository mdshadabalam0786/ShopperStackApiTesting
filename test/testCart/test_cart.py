import pytest
from requests import Session
from json import loads

itemid=[]
productIdList=[]
url="https://www.shoppersstack.com/shopping"
session=Session()

def test_viewProduct(getKeyShopperId):
    session.headers.update({"content-type":"application/json"})
    response=session.get(f"{url}/products/alpha")
    print(response)
    #=================================================================================================================
    assert response.status_code==200,f"found this status actual from the server {response.status_code}"
    assert response.elapsed.total_seconds()<=3,f"found this status actual from the server {response.elapsed.total_seconds()}"
    assert response.ok==True,f"found this status actual from the server {response.ok}"
    #=================================================================================================================
    r1=loads(response.text)
    for i in range(len(r1['data'][0])):
       productIdList.append(r1['data'][i]['productId'])
    print(productIdList)
    
    
    
    
def test_addCart(getKeyShopperId):
    session.headers.update({"Authorization": f"Bearer {getKeyShopperId[0]}"})
    session.headers.update({"content-type":"application/json"})
    
    payload={
                "productId": f"{productIdList[3]}",
                "quantity": 5
                }
    response=session.post(f"{url}/shoppers/{getKeyShopperId[1]}/carts",json=payload)
    assert response.status_code==201,f"found this status actual from the server {response.status_code}"
    assert response.elapsed.total_seconds()<=3,f"found this status actual from the server {response.elapsed.total_seconds()}"
    print(response)
    r=loads(response.text)
    print(len(r['data']))
    itemid.append(r['data']['itemId'])
    print(f"it is a item id:{itemid}")
    
    
  


def test_getCart(getKeyShopperId): 
    session.headers.update({"Authorization": f"Bearer {getKeyShopperId[0]}"})
    session.headers.update({"content-type":"application/json"})

    response=session.get(f"{url}/shoppers/{getKeyShopperId[1]}/carts")
    assert response.status_code==200,f"found this status actual from the server {response.status_code}"
    assert response.elapsed.total_seconds()<=3,f"found this status actual from the server {response.elapsed.total_seconds()}"
    assert response.ok==True,f"found this status actual from the server {response.ok}"
    r=loads(response.text)
    print(r)

@pytest.mark.skip
def test_updateCart(getKeyShopperId):
    session.headers.update({"content-type":"application/json"})
    
    
    payload={
            "productId": f"{productIdList[3]}",
            "quantity": 1
            }
    
    response=session.put(f"{url}/shoppers/{getKeyShopperId[1]}/carts/{itemid[0]}",json=payload)
    assert response.status_code==200,f"found this status actual from the server {response.status_code}"
    assert response.elapsed.total_seconds()<=3,f"found this status actual from the server {response.elapsed.total_seconds()}"
    assert response.ok==True,f"found this status actual from the server {response.ok}"
    print(response.text)

@pytest.mark.skip
def test_DeleteCart(getKeyShopperId):
    session.headers.update({"content-type":"application/json"})
    response=session.delete(f"{url}/shoppers/{getKeyShopperId[1]}/carts/{productIdList[3]}")
    assert response.status_code==200,f"found this status actual from the server {response.status_code}"
    assert response.elapsed.total_seconds()<=3,f"found this status actual from the server {response.elapsed.total_seconds()}"
    assert response.ok==True,f"found this status actual from the server {response.ok}"
    print(response.text)


