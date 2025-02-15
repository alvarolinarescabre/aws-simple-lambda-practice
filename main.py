def lambda_handler(event, context):

    if not event['rawQueryString']:
        name = 'KeepCoder'
    else:
        name = event['queryStringParameters']['name']
        

    return {
        'headers': {
            'Content-Type': 'text/plain; charset=utf-8'
        },
        'statusCode': 200,
        'body': f'Hola {name} desde una función Lambda'
    }
