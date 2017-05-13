import boto3

def handler(event, context):
    client = boto3.client("dynamodb")
    item = client.get_item(TableName="pizzashoporder", Key={"order_id":{"S":event["order_id"]}})
    menu = client.get_item(TableName="pizzashopmenu",
                           Key={"menu_id":{"S":item["Item"]["menu_id"]["S"]}})

    response = "Which size do you want? "

    for item in menu["Item"]["size"]["L"]:
            response = response + str(i) + ". " + item["S"]
            if i<len(menu["Item"]["size"]["L"]):
                response = response + ", "
            i = i + 1
        return dict({"Message":response})

        client.update_item(TableName="pizzashoporder",
                           Key={"order_id":{"S":event["order_id"]}},
                           UpdateExpression="SET ord.#o = :o",
                           ExpressionAttributeNames={"#o": "size"},
                           ExpressionAttributeValues=
        

        client.update_item(TableName="pizzashoporder",
                           Key={"order_id":{"S":event["order_id"]}},
                           UpdateExpression="SET ord.#o = :o",
                           ExpressionAttributeNames={"#o": "costs"},
                           ExpressionAttributeValues=
                           {":o": {"N":menu["Item"]["price"]["L"][event["selection_number"]-1]["N"]}})

        response = "Your order costs" + menu["Item"]["price"]["L"][event["selection_number"]-1]["N"] +". We will email you when the order is ready. Thank you!"
        return dict({"Message":response})