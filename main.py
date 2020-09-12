from flask import Flask
from flask_restful import  Api, Resource
app= Flask(__name__)
api= Api(app)

class addition(Resource):
    def add(self, a, b):
        return int(a)+int(b)

    def get(self,num1, num2):
        #return int(num1) + int(num2)
        return {"sum": addition.add(self, num1, num2)}

class subtraction(Resource):
    def subtract(self,a,b):
        return int(a)-int(b)

    def get(self, num1, num2):
        return {"diff": subtraction.subtract(self, num1, num2)}

class multiplication(Resource):
    def multiply(self,a,b):
        return int(a) * int(b)

    def get(self, num1, num2):
        return {"product": multiplication.multiply(self, num1, num2)}

class division(Resource):
    def divide(self,a,b):
        try:
            int(a) / int(b)
        except ZeroDivisionError:
            return "Can't divide by 0"

    def get(self, num1, num2):
        return {"division": division.divide(self, num1, num2)}

class factorial(Resource):
    def factorial(self,a):
        product=1
        for i in range(1, int(a)+1):
            product=product*i
        return product

    def get(self, num1):
        return {"factorial": factorial.factorial(self, num1)}

class percentage(Resource):
    def percent(self, a):
        return float(a)/100

    def get(self, num1):
        return {"percentage":percentage.percent(self, num1)}

api.add_resource(addition,"/addition/<num1>/<num2>")
api.add_resource(subtraction,"/subtraction/<num1>/<num2>")
api.add_resource(multiplication,"/multiplication/<num1>/<num2>")
api.add_resource(division,"/division/<num1>/<num2>")
api.add_resource(factorial,"/factorial/<num1>")
api.add_resource(percentage,"/percentage/<num1>")


if __name__ == '__main__':
    app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
