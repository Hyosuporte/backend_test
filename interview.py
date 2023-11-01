import json
import boto3

"""
#########################
# Roles table           #
#########################
# Id    # Name          #
#########################
# 0     # ADMIN         #
# 1     # CLIENT        #
# 2     # TECHNICIAN    #
# 3     # REPLENISHER   #
#########################
"""

def get_user_on_dynamoDB(id):
    invokeLambda = boto3.client('lambda', region_name='us-east-2')
    lambda_response = invokeLambda.invoke(FunctionName = 'DA_DynamoDB_Read', InvocationType = 'RequestResponse', 
        Payload = json.dumps({
            "table":"user",
            "key_name":"id",
            "key_value":id
        }))
    resp_str = lambda_response['Payload'].read()
    resp = json.loads(resp_str)
    return resp[0], resp[1]

def get_iot_device_on_dynamoDB(id):
    invokeLambda = boto3.client('lambda', region_name='us-east-2')
    lambda_response = invokeLambda.invoke(FunctionName = 'DA_DynamoDB_Read', InvocationType = 'RequestResponse', 
        Payload = json.dumps({
            "table":"iotDevice",
            "key_name":"id",
            "key_value":id
        }))
    resp_str = lambda_response['Payload'].read()
    resp = json.loads(resp_str)
    return resp[0], resp[1]
    
def get_iot_device_on_dynamoDB(id):
    invokeLambda = boto3.client('lambda', region_name='us-east-2')
    lambda_response = invokeLambda.invoke(FunctionName = 'DA_DynamoDB_Read', InvocationType = 'RequestResponse', 
        Payload = json.dumps({
            "table":"iotDevice",
            "key_name":"id",
            "key_value":id
        }))
    resp_str = lambda_response['Payload'].read()
    resp = json.loads(resp_str)
    return resp[0], resp[1]

def get_iot_device_products_on_dynamoDB(deviceId):
    invokeLambda = boto3.client('lambda', region_name='us-east-2')
    lambda_response = invokeLambda.invoke(FunctionName = 'DA_DynamoDB_Read', InvocationType = 'RequestResponse', 
        Payload = json.dumps({
            "table":"iotDeviceProducts",
            "key_name":"deviceId",
            "key_value":deviceId
        }))
    resp_str = lambda_response['Payload'].read()
    resp = json.loads(resp_str)
    return resp[0], resp[1]

def get_product_on_dynamoDB(id):
    invokeLambda = boto3.client('lambda', region_name='us-east-2')
    lambda_response = invokeLambda.invoke(FunctionName = 'DA_DynamoDB_Read', InvocationType = 'RequestResponse', 
        Payload = json.dumps({
            "table":"product",
            "key_name":"id",
            "key_value":id
        }))
    resp_str = lambda_response['Payload'].read()
    resp = json.loads(resp_str)
    return resp[0], resp[1]

def lambda_handler(event, context):
    flag, user_entity = get_user_on_dynamoDB(event["userId"])
    if flag and user_entity:
        flag = False
        for role in user_entity["roles"]:
            if role == 1:
                flag = True
            if role == 3:
                flag = True
        if flag:
            flag_device, device = get_iot_device_on_dynamoDB(event["deviceId"])
            if flag_device and device:
                flag_device_products, device_products = get_iot_device_products_on_dynamoDB(event["deviceId"])
                if flag_device_products and device_products:
                    products = []
                    for i in range(len(device_products)):
                        flagProduct, product = get_product_on_dynamoDB(device_products[i]["productId"])
                        if flagProduct and product:
                            products.append(product)
                        else:
                            return {
                                'statusCode': 500,
                                'body': {
                                    'msg': "Unable to get whole products"
                                }
                            }
                    for i in range(len(products)):
                        product = products[i]
                        for j in range(len(device_products)):
                            if device_products[j]["productId"] == product["id"]:
                                product["amount"] = device_products[j]["amount"]
                        products[i] = product
                    products_width=[]
                    for i in range(len(products)):
                        products_width[i] = products[i]["width"]
                    return {
                        'statusCode': 200,
                        'body': {"products":list_products, "widths":products_width}
                    }
                else:
                    return {
                        'statusCode': 500,
                        'body': {
                            'msg': "Unable to get device products"
                        }
                    }
            else:
                return {
                    'statusCode': 500,
                    'body': {
                        'msg': "Unable to get device"
                    }
                }
        if not flag:
            return {
                'statusCode': 500,
                'body': {
                    'msg': "Unauthorized access"
                }
            }
    else:
        return {
            'statusCode': 500,
            'body': {
                'msg': "Unable to retrieve user"
            }
        }
    return {
        'statusCode': 500,
        'body': {
            'msg': "Unable to retrieve user"
        }
    }
        
            