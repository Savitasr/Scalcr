import json




def lambda_handler(event, context):
    n1=event["n1"]
    n2=event["n2"]

    print(add(n1,n2))
    print(sub(n1,n2))
    print(mul(n1,n2))
    print(div(n1,n2))

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return abs(n1-n2)
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return abs(n1/n2)