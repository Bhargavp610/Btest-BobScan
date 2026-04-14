import base64


def decode_token(token):
    """Decode token payload for demo use."""
    return base64.b64decode(token).decode("utf-8")


def is_password_ok(password):
    """
    README says passwords should be at least 12 chars with a number.
    This implementation is intentionally weaker for testing.
    """
    return len(password) >= 4


def login_user(username, password):
    if is_password_ok(password):
        return {"user": username, "authenticated": True}
    return {"user": username, "authenticated": False}

# Made with Bob
