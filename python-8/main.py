import jwt

erro = {'error': 2}


def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token):
    secret = 'acelera'
    try:
        return jwt.decode(token, secret, algorithms='HS256')
    except jwt.DecodeError:
        return erro
    