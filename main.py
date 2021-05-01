import json

def lambda_handler(event, context):
    if 'queryStringParameters' in event and 'name' in event['queryStringParameters']:
        msg = 'Hola  {}!'.format(event["queryStringParameters"]['name'])
    else:
        msg = 'Hola CICE!'
    return{  
        'statusCode': 200,
        'body': json.dumps(msg)
    }

