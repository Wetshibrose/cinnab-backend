from typing import Any

class ErrorMessageResponse:
    def __init__(self, success:bool, error_message:str, status_code:int=400) -> None:
        self.success = success
        self.error_message = error_message
        self.status_code=status_code

class SuccessMessageResponse:
    def __init__(self, success:bool, data:dict[str, Any], status_code:int=400) -> None:
        self.success = success
        self.data = data
        self.status_code=status_code

