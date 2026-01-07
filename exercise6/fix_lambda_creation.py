# Código corregido para crear la función Lambda
import boto3
import json
import zipfile
from io import BytesIO

# Asegurar que lambda_function esté definida globalmente
lambda_function = None

try:
    # Package up the lambda function code
    s = BytesIO()
    z = zipfile.ZipFile(s, 'w')
    z.write("lambda_function_complete.py", "lambda_function.py")  # Renombrar en el zip
    z.write("employee_database.db")
    z.close()
    zip_content = s.getvalue()

    # Create Lambda Function
    lambda_function = lambda_client.create_function(
        FunctionName=lambda_function_name,
        Runtime='python3.12',
        Timeout=180,
        Role=lambda_iam_role['Role']['Arn'],
        Code={'ZipFile': zip_content},
        Handler='lambda_function.lambda_handler'
    )
    print(f"Lambda function created: {lambda_function['FunctionArn']}")
    
except Exception as e:
    print(f"Error creating Lambda: {e}")
    # Si ya existe, obtenerla
    try:
        lambda_function = lambda_client.get_function(FunctionName=lambda_function_name)
        print(f"Using existing Lambda: {lambda_function['Configuration']['FunctionArn']}")
    except:
        print("Lambda function not found")

# Verificar que lambda_function esté definida antes de usar
if lambda_function:
    lambda_arn = lambda_function.get('FunctionArn') or lambda_function['Configuration']['FunctionArn']
    print(f"Lambda ARN: {lambda_arn}")
else:
    print("ERROR: lambda_function is not defined")