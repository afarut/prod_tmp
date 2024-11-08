import hashlib
import hmac
import time

def verify_telegram_auth(auth_data, bot_token):
    auth_data = dict(auth_data)
    hash_value = auth_data.pop('hash', None)
    data_check_string = '\n'.join(f"{key}={auth_data[key]}" for key in sorted(auth_data.keys()))
    secret_key = hashlib.sha256(bot_token.encode()).digest()
    calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
    if hash_value != calculated_hash:
        return False
    
    # 10 дне : 864000 секунд
    auth_date = int(auth_data.get("auth_date", 0))
    return time.time() - auth_date < 864000
