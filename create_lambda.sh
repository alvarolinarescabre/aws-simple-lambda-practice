#!/bin/bash

# Creamos el rol de ejecución primero
aws iam create-role --role-name lambda-execute-rol --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

# Atachamos el rol a la política de Ejecución
aws iam attach-role-policy --role-name lambda-execute-rol --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Implementamos la función lambda
aws lambda create-function --function-name chamo-demo-lambda --zip-file fileb://main.zip  --handler main.lambda_handler --runtime python3.8 --role arn:aws:iam::663762823706:role/lambda-execute-rol

# Probamos la función lambda
aws lambda invoke --function-name chamo-demo-lambda --payload '{"name": "Chamo"}' output.txt

# Mostramos resultado
cat output.txt
