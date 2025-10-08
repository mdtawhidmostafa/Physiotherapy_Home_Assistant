from cryptography.fernet import Fernet  

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_otp(otp):
    return cipher_suite.encrypt(otp.encode()).decode()

def decrypt_otp(encrypted_otp):
    return cipher_suite.decrypt(encrypted_otp.encode()).decode()


from django.core.signing import TimestampSigner, SignatureExpired

def verify_and_extract_otp(signed_otp):
    try:
        signer = TimestampSigner()
        otp = signer.unsign(signed_otp, max_age=60)  # OTP expires after 60 seconds
        return otp
    except SignatureExpired:
        return None  # OTP has expired
    except Exception:
        return None  # Invalid signature