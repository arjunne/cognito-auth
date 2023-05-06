import boto3

USER_POOL_ID = 'us-east-1_HUZcofD3L'
CLIENT_ID = '5hp6d2jqgrsusvlquvlkfgc8se'
REGION = 'us-east-1'

cognito = boto3.client('cognito-idp', region_name=REGION)

def signup(username, password, email):
    try:
        response = cognito.sign_up(
            ClientId=CLIENT_ID,
            Username=username,
            Password=password,
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': email
                }
            ]
        )
        return response['UserSub']
    except Exception as e:
        return str(e)

def confirm_signup(username, code):
    try:
        response = cognito.confirm_sign_up(
            ClientId=CLIENT_ID,
            Username=username,
            ConfirmationCode=code
        )
        return True
    except Exception as e:
        return str(e)

def authenticate(username, password):
    try:
        response = cognito.admin_initiate_auth(
            UserPoolId=USER_POOL_ID,
            ClientId=CLIENT_ID,
            AuthFlow='ADMIN_NO_SRP_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        return response['AuthenticationResult']
    except Exception as e:
        return str(e)
