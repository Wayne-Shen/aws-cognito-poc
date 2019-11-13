import boto3

from config import get_cognito_properties

propeties = get_cognito_properties()
cognito_client = boto3.client('cognito-identity')


def get_token_for_user(user_id):
    """AWS Environment (AWS Lambda/ECS/EC2)"""
    token_response = cognito_client.get_open_id_token_for_developer_identity(
        IdentityPoolId=propeties['identity-pool-id'],
        Logins={
            propeties['identity-custom-domain']: user_id
        },
        TokenDuration=120
    )
    print(token_response)
    return token_response


sts_client = boto3.client('sts')


def get_sts_credential(token_response):
    """AWS Environment (AWS Lambda/ECS/EC2)"""
    sts_response = sts_client.assume_role_with_web_identity(
        RoleArn=propeties['assume-role-arn'],
        RoleSessionName='test-session-1',
        WebIdentityToken=token_response['Token'],
        DurationSeconds=900
    )
    print(sts_response)
    return sts_response


def test_s3(sts_credentials):
    """Client environment (Android/IOS)"""
    credential = sts_credentials['Credentials']
    session = boto3.Session(
        aws_access_key_id=credential['AccessKeyId'],
        aws_secret_access_key=credential['SecretAccessKey'],
        aws_session_token=credential['SessionToken'],
    )

    s3_client = session.client('s3')

    response = s3_client.list_buckets()
    print(response)


test_s3(get_sts_credential(get_token_for_user('test-user-3')))
# response = get_token_for_user('test-user-1')
