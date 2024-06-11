from requests import Session
from json import loads

session=Session()
def test_getWishList(getKeyShopperId):
    session.headers.update({"content-type":"application/json"})
    session.headers.update({"Authorization":f"Bearer {getKeyShopperId[0]}"})
    response=session.get(f"https://www.shoppersstack.com/shopping/shoppers/{getKeyShopperId[1]}/wishlist")
    assert response.status_code==200,f"this response got it from server {response.status_code}"
    assert response.elapsed.total_seconds()<=3,f"this response got it from server {response.elapsed.total_seconds()}"
    if response.ok==True:
        print("Ok")
    r=loads(response.text)
    print(r)
    assert r['statusCode']==200,f"this response got it from server {r['statusCode']}"
    assert r['message']=="Success",f"this response got it from server {r['message']}"