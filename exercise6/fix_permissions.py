# Solución alternativa - usar política inline en lugar de crear política separada
import boto3
import json

# Usar los mismos clientes
sts_client = boto3.client('sts')
iam_client = boto3.client('iam')

# Variables ya definidas
session = boto3.session.Session()
region = session.region_name
account_id = sts_client.get_caller_identity()["Account"]
inference_profile = "us.amazon.nova-micro-v1:0" 
foundation_model = inference_profile[3:]
suffix = f"{region}-{account_id}"
agent_name = "hr-assistant-function-def"
agent_role_name = f'AmazonBedrockExecutionRoleForAgents_{agent_name}'

# Crear rol del agente con política inline
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"Service": "bedrock.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
    ]
}

bedrock_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "bedrock:InvokeModel",
            "Resource": [
                f"arn:aws:bedrock:*::foundation-model/{foundation_model}",
                f"arn:aws:bedrock:*:*:inference-profile/{inference_profile}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:GetInferenceProfile",
                "bedrock:ListInferenceProfiles",
                "bedrock:UseInferenceProfile"
            ],
            "Resource": f"arn:aws:bedrock:*:*:inference-profile/{inference_profile}"
        }
    ]
}

try:
    # Crear rol
    agent_role = iam_client.create_role(
        RoleName=agent_role_name,
        AssumeRolePolicyDocument=json.dumps(assume_role_policy)
    )
    print(f"Rol creado: {agent_role_name}")
except:
    agent_role = iam_client.get_role(RoleName=agent_role_name)
    print(f"Rol ya existe: {agent_role_name}")

# Agregar política inline al rol
iam_client.put_role_policy(
    RoleName=agent_role_name,
    PolicyName='BedrockInlinePolicy',
    PolicyDocument=json.dumps(bedrock_policy)
)

print("Política inline agregada al rol")
print(f"ARN del rol: {agent_role['Role']['Arn']}")