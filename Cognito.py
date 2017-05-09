import boto3

client = boto3.client('cognito-idp')


try:
  response = client.sign_up(
    ClientId="xxxxxxxxxx",
    Username="user1",
    Password="password",
    UserAttributes=[
      {
        "Name":"email",
        "Value":"xxx@xxx.com"
      },
      {
        "Name":"custom:customeAttribute1",
        "Value":"user"
      },
      {
        "Name":"custom:customeAttribute2",
        "Value":"two"
      },
      {
        "Name":"custom:customeAttribute3",
        "Value":"123456"
      }
      ]
    )
except Exception, error:
  response = error


'''
response = client.admin_initiate_auth(
    UserPoolId='us-xxxx-#_xxxxxxxx',
    ClientId='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    AuthFlow='ADMIN_NO_SRP_AUTH',
    AuthParameters={
        'USERNAME': 'user1',
        'PASSWORD':'password'
    }
)
'''


'''
response = client.respond_to_auth_challenge(
    ClientId='xxxxxxxxxxxxxxxxxxxxxxxxxx',
    ChallengeName='NEW_PASSWORD_REQUIRED', #Get this value from admin_initiate_auth response
    Session='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', #Get this value from admin_initiate_auth response
    ChallengeResponses={
      'USERNAME':'user1',
      'NEW_PASSWORD': 'password'
    }
)
'''

print response
