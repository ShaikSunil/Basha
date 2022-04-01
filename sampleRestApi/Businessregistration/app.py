import json
from dbconnection import *

def adduser(details):
    l = [{'name':'basha','email':'basha@gmail.com'}, {'name':'kiran','email':'baha@gmail.com'}]

    for i in l:
        print(i)
        
    try:
        name = details(i['name'])
        email = details(i['email'])
        phoneNumber = details(i['phoneNumber'])
        address = details(i['address'])
        sql_insert_query = (""" INSERT INTO business_registration
        (name, email, phoneNumber, address) VALUES (%s,%s,%s,%s)""")
        tuple1 = (name, email, phoneNumber, address)
        result = execute_qry_v2(sql_insert_query, tuple1)
        result = {"message":"user created successfully"}
    
    except Exception as e:
        result = {"message":"exception occured"}
    return result

def getuser(details):
    try:
        id = details["id"]
        sql_get_query = '''SELECT * FROM business_registration WHERE id = %(id)'''
        
        result = execute_qry_v2(sql_get_query)
        
        result = {"message":"retrived data successfully"}
    except Exception as e:
        result = {"message":"exception occured"}
    return result
    
def updateuser(details):
    try:
        regId = details['regid']
        sql = '''UPDATE Business_registration SET regId = "456" WHERE id ='''%(id)
    except Exception as e:
        result = {"message":"exception occured"}
    return result
    
def deleteuser(details):
    try:
        regId = details("regId")
        sql = '''Delete from Business_registration where regId = '''%(regId)
    except Exception as e:
        result = {"message":"exception occured"}
    return result
        

def lambda_handler(event, context):

    method = event['httpMethod']
    if method == "POST":
        details = json.loads(event['body'])
        result = adduser(details)
        
        
    elif method == "GET":
         details = event['queryStringParameters']
         result = getuser(details)
         message = {"message":"get user"}

    elif method == 'PUT':
        details = json.loads(event['body'])
        result = updateuser(details)
        message = {'message': 'update user'}

    elif method == 'DELETE':
        details = json.loads(event['body'])
        result = deleteuser(details)
        message = {'message':'delete user'}    
    
    return {
        "statusCode": 200,
        "body": json.dumps(result),
    }