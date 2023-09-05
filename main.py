import json

def lambda_handler(event, context):
    name = event.get('queryStringParameters', None)
    if name:
        msg = 'Hola {}!'.format(name['name'])
    else:
        msg = 'Hola Chamo =^.^='
    return{  
        'statusCode': 200,
        'body': json.dumps(msg)
    }
