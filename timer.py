import timeit
from datetime import datetime


def log_elapsed_time(target_func):
    """
      함수(target_func)를 호출하면 해당 함수의 소요시간을 {함수이름}.log 파일에 기록하는 decorator 함수

      ---
    :param target_func: function
    :return:
    """
    import logging

    logger = logging.getLogger(target_func.__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(f"{target_func.__name__}.log")
    logger.addHandler(file_handler)

    def wrapper(*args, **kwargs):

        start_time = timeit.default_timer()
        target_func(*args, **kwargs)
        end_time = timeit.default_timer()
        logger.info(f"[{datetime.now()}] elapsed time: {end_time-start_time}")
        return None

    return wrapper

