import boto3


def handler(event, context):
    # Your code goes here!
    client = boto3.client("dynamodb")
    item = client.get_item(TableName="pizzashoporder", Key=event)
    response = dict()
    response["menu_id"] = item["Item"]["menu_id"]["S"]
    response["order_id"] = item["Item"]["order_id"]["S"]
    response["customer_name"] = item["Item"]["customer_name"]["S"]
    response["customer_email"] = item["Item"]["customer_email"]["S"]
    response["order"] = []
    for it in item["Item"]["ord"]["M"]:
        if it == "costs":
            response["order"].append([it, item["Item"]["ord"]["M"][it]["N"]])
        else:
            response["order"].append([it, item["Item"]["ord"]["M"][it]["S"]])
    return response

