from .logger_utils import get_logger
import traceback

def safe_run(use_logger=True):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            logger = None  # 🔧 Ensure it's always defined
            if use_logger:
                logger = get_logger(self.__class__.__name__)
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                msg = f"❌ in {self.filename} - {self.__class__.__name__} failed: {e}"
                trace = traceback.format_exc()
                if use_logger and logger:
                    logger.error(msg)
                    logger.error(trace)
                else:
                    print(msg)
                    print(trace)
                return None
        return wrapper
    return decorator