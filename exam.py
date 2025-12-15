
import time
from functools import wraps


class SafeExecuteException(Exception):
    pass


def safe_execute(max_tries=1, timeout=None, delay=0):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for try_num in range(1, max_tries + 1):
                try:
                    if timeout:
                        start = time.time()
                    
                    result = func(*args, **kwargs)
                    
                    if timeout and (time.time() - start) > timeout:
                        raise TimeoutError(f"Забагато часу! Ліміт: {timeout}с")
                    
                    return result
                    
                except Exception as error:
                    last_error = error

                    if try_num < max_tries:
                        print(f"Спроба {try_num} невдала: {error}")
                        if delay > 0:
                            time.sleep(delay)  
                    else:
                        raise SafeExecuteException(
                            f"Функція '{func.__name__}' провалилася після {max_tries} спроб. "
                            f"Остання помилка: {error}"
                        )
        
        return wrapper
    
    return decorator