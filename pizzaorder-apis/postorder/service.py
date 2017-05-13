import boto3
import json

def makeformat(list, varname):
    return [dict({varname:item}) for item in list]

def handler(event, context):
    client = boto3.client("dynamodb")
    try:
        client.put_item(TableName="pizzashoporder",
                        Item={"order_id":{"S":event["order_id"]},
                              "menu_id":{"S":event["menu_id"]},
                              "customer_name":{"S":event["customer_name"]},
                              "customer_email":{"S":event["customer_email"]}})
        menu = client.get_item(TableName="pizzashopmenu", Key={"menu_id":{"S":event["menu_id"]}})
        response = "Hi "+event["customer_name"]+", please choose one of these selection: 1. Cheese, 2. Pepperoni, 3.Vegetable"
        
    except Exception, e:
        return 400, e
    return 200, "OK", {"Message":response}
