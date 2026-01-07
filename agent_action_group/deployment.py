import boto3
import json
import zipfile
import os

def create_lambda_deployment_package():
    """Create deployment package for Lambda function"""
    with zipfile.ZipFile('lambda_function.zip', 'w') as zip_file:
        zip_file.write('lambda_function.py')
    print("Lambda deployment package created: lambda_function.zip")

def deploy_lambda_function():
    """Deploy Lambda function to AWS"""
    lambda_client = boto3.client('lambda')
    
    with open('lambda_function.zip', 'rb') as zip_file:
        zip_content = zip_file.read()
    
    try:
        response = lambda_client.create_function(
            FunctionName='bedrock-agent-task-manager',
            Runtime='python3.9',
            Role='arn:aws:iam::YOUR_ACCOUNT:role/lambda-execution-role',
            Handler='lambda_function.lambda_handler',
            Code={'ZipFile': zip_content},
            Description='Task Manager for Bedrock Agent',
            Timeout=30
        )
        print(f"Lambda function created: {response['FunctionArn']}")
        return response['FunctionArn']
    except lambda_client.exceptions.ResourceConflictException:
        print("Function already exists, updating...")
        response = lambda_client.update_function_code(
            FunctionName='bedrock-agent-task-manager',
            ZipFile=zip_content
        )
        print("Lambda function updated")
        return response['FunctionArn']

def create_bedrock_agent_action_group(lambda_arn):
    """Create action group in Bedrock Agent"""
    bedrock_agent = boto3.client('bedrock-agent')
    
    with open('openapi_schema.json', 'r') as f:
        api_schema = f.read()
    
    try:
        response = bedrock_agent.create_action_group(
            agentId='YOUR_AGENT_ID',
            agentVersion='DRAFT',
            actionGroupName='TaskManager',
            description='Manages tasks for the user',
            actionGroupExecutor={
                'lambda': lambda_arn
            },
            apiSchema={
                'payload': api_schema
            }
        )
        print(f"Action group created: {response['actionGroup']['actionGroupId']}")
    except Exception as e:
        print(f"Error creating action group: {e}")

if __name__ == "__main__":
    print("Creating Lambda deployment package...")
    create_lambda_deployment_package()
    
    print("Deploying Lambda function...")
    lambda_arn = deploy_lambda_function()
    
    print("Creating Bedrock Agent action group...")
    create_bedrock_agent_action_group(lambda_arn)