import json


def hello(event, context):
    body = {
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

    
def sum(event, context):
    body = json.loads(event['body'])
    value1 = body['value1']
    value2 = body['value2']

    response = {
        "statusCode": 200, 
        "body": json.dumps({
            "result": f"{value1} + {value2} = {value1 + value2}",
            "input": {
                "event.body": body,
                "event": event
            }
        })
    }

    return response


def update_user(event, context):
    # this is a simple test
    # the user id always is 1 for simplicity

    user_id = event["pathParameters"]["user_id"]
    # if not user_id == 1 or user_id == "1":
    #     raise Exception("User not found!")

    user_in = json.loads(event["body"])

    db_user = {
        "user_id": 1,
        "username": "joao@gmail.com",
        "password": "56978184-1930-4578-b8a2-7610d3d3842a",
        "name": "João Paulo Antunes de Souza"
    }
    db_user["user_id"] = user_in["user_id"]
    db_user["username"] = user_in["username"]
    db_user["password"] = user_in["password"]
    db_user["name"] = user_in["name"]

    response = {
        "statusCode": 200, 
        "body": json.dumps({
            "user_id": user_id,
            "user_in": user_in,
            "db_user": db_user,
            "input": {
                "event": event
            }
        })
    }

    return response


def delete_user(event, context):
    user_id = event["pathParameters"]["user_id"]

    response = {
        "statusCode": 200, 
        "body": json.dumps({
            "user_id": user_id,
            "db_user": None,
            "input": {
                "event": event
            }
        })
    }

    return response