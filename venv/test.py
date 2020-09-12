import requests

BASE= "http://127.0.0.1:5000/"
sumresponse= requests.get(BASE + "addition/12/6")
print(sumresponse.json())
diffresponse= requests.get(BASE + "subtraction/12/6")
print(diffresponse.json())
prodresponse= requests.get(BASE + "multiplication/12/6")
print(prodresponse.json())
divresponse= requests.get(BASE + "division/12/0")
print(divresponse.json())
factorialresponse= requests.get(BASE + "factorial/5")
print(factorialresponse.json())
percentresponse= requests.get(BASE + "percentage/5")
print(percentresponse.json())




