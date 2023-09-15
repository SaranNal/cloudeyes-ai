import requests
from jose import jwt, JWTError
from jwcrypto import jwk


def jwk_to_pem(jwk_json):
    key = jwk.JWK(**jwk_json)
    return key.export_to_pem()


# Configuration
REGION = 'us-east-1'
USER_POOL_ID = 'us-east-1_KudKy0yPJ'
# USER_POOL_ID = 'us-east-1_1i5LrrrxV'
COGNITO_KEYS_URL = f'https://cognito-idp.{REGION}.amazonaws.com/{USER_POOL_ID}/.well-known/jwks.json'

# Fetch Cognito JWKS
response = requests.get(COGNITO_KEYS_URL)
keys = response.json()['keys']

# Decode & Verify Token
token = 'eyJraWQiOiJMYjVyYTFhNEZmdmR5bllSS2R3djZMRzVJOElveWZXYTNzZ2ZOVXNTRjIwPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI3YzI2MjBjMy1jMWEzLTQ4NGEtOGY0NC05Mjk4Y2Q1MzRkMGQiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9LdWRLeTB5UEoiLCJjbGllbnRfaWQiOiI2OGpuZ2s1cjk5cDUzN2tqOXAwNWszZTU0bSIsIm9yaWdpbl9qdGkiOiJlZDIxMjk4Mi0xZGUxLTRiYmEtYjE2NC1kODFmMjJkYWNkYjYiLCJldmVudF9pZCI6ImU5M2Y4ZWViLWJhY2ItNGVmYi05NWI3LTZhZWIxOGE4ZmUwMCIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2OTQ3NTE5OTAsImV4cCI6MTY5NDc1NTU5MCwiaWF0IjoxNjk0NzUxOTkwLCJqdGkiOiJjZTU0MzUzYy05ZmM0LTQ1ODQtOTk2Ny05NDJkNjUzZTYxYzUiLCJ1c2VybmFtZSI6IjdjMjYyMGMzLWMxYTMtNDg0YS04ZjQ0LTkyOThjZDUzNGQwZCJ9.enT4ApiwaVGkUT3Jp5NQB2rV1ih4HCXgl9JWfu7IwCMyAe0Z1SaJt8mTciYHiCgxMKaZa4kjoCj5uOo27dN-gC19wLKF5srQ_6BFSE3V4VSnUFdwUpZLDzOUkCj5bvPmgxEqKgmsy3mst3g599bUI2CZBWe7_k1Q8uhoJAG8RQwICtS-m_TltkuKc6z7eIco_xMu1-nmtgsiyruYJayIgkODLOW8V2BsnkxiPWqbhnGEhE5LRdnT-RNpR4nVR5ceBxL3a6CZ7MhjmdIFy4nuPJ64Hcgr4eDLv5X-BsNZhz67HluWyyir4E6aCMu3ly3tReUnDiLgga-x28b_-75iNg'
header = jwt.get_unverified_header(token)
kid = header['kid']
print(kid)
print(keys)

# Find the key with matching `kid` in the JWKS
key_json = [k for k in keys if k['kid'] == kid][0]
pem_key = jwk_to_pem(key_json)

# payload = jwt.decode(token, pem_key, algorithms=['RS256'])


try:
    # Verify and decode the token
    payload = jwt.decode(token, pem_key, algorithms=['RS256'])
    print(payload)
except JWTError as e:
    print(f"Token validation failed: {e}")
