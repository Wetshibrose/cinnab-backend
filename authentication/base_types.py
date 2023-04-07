class ErrorMessageResponse:
    def __init__(self, message, status_code=400) -> None:
        self.message = message
        self.status_code=status_code

class LoginResponse:
    def __init__(self, access_token, refresh_token) -> None:
        self.access_token = access_token
        self.refresh_token = refresh_token