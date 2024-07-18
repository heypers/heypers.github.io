import hashlib
import hmac
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_SECRET = os.getenv("GTK")


class Verificator:
    @staticmethod
    def verify_github_signature(data, signature):
        secret = bytes(GITHUB_SECRET, 'utf-8')
        sha_name, signature = signature.split('=')
        if sha_name == 'sha1':
            mac = hmac.new(secret, msg=data, digestmod=hashlib.sha1)
        elif sha_name == 'sha256':
            mac = hmac.new(secret, msg=data, digestmod=hashlib.sha256)
        else:
            return False
        return hmac.compare_digest(mac.hexdigest(), signature)

    @staticmethod
    def verify_token(token):
        return hmac.compare_digest(token, GITHUB_SECRET)