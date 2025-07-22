from functools import wraps
from exception_handler import global_exception_handler

def api_error_handler(func):
    """
    예외 처리 데코레이터

    함수 실행을 감싸서 성공 시 표준 응답을,
    실패 시 global_exception_handler를 통해 일관된 응답을 반환

    - 성공: {"success": True,  "data":  ...}
    - 실패: {"success": False, "error": ...}
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            response = {"success": True}
            if result is not None:
                response["data"] = result
            return response

        except Exception as e:
            return global_exception_handler(e)
            
    return wrapper
