import json

# import requests


def lambda_handler(event, context):
    num1 = event["num1"]
    num2 = event["num2"]

    print(add(num1,num2))
    print(sub(num1,num2))
    print(mul(num1,num2))
    print(div(num1,num2))


def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

       
