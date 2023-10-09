import requests
from jose import jwt, JWTError
from jwcrypto import jwk


def jwk_to_pem(jwk_json):
    key = jwk.JWK(**jwk_json)
    return key.export_to_pem()


def cognito_validate(token):
    print(token)
    # Configuration
    REGION = 'us-east-1'
    # USER_POOL_ID = 'us-east-1_KudKy0yPJ'
    USER_POOL_ID = 'us-east-1_1i5LrrrxV'
    COGNITO_KEYS_URL = f'https://cognito-idp.{REGION}.amazonaws.com/{USER_POOL_ID}/.well-known/jwks.json'

    # Fetch Cognito JWKS
    response = requests.get(COGNITO_KEYS_URL)
    keys = response.json()['keys']

    try:
        # Decode & Verify Token
        header = jwt.get_unverified_header(token)

        kid = header['kid']
        print(kid)
        print(keys)

        # Find the key with matching `kid` in the JWKS
        key_json = [k for k in keys if k['kid'] == kid][0]
        pem_key = jwk_to_pem(key_json)
        # Verify and decode the token
        payload = jwt.decode(token, pem_key, algorithms=['RS256'])
        return True
    except JWTError as e:
        return False
