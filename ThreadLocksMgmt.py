from threading import Lock

class ThreadLocksMgmt:
    _instance = None
    _lock = Lock()
    _lockDictLock = Lock()
    _answersFromCoreLock = Lock()
    
    def __init__(self):
        self.locksDict = {}
        self.answersFromCoreLock = {}
        raise RuntimeError('call def instance')
        
    @classmethod
    def get_instance(cls):
        if cls._instance:
            return cls._instance
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls.__new__(cls)
                cls._instance.locks_dict = {}
                return cls._instance
            else:
                return cls._instance
            
    def thread_lock(self, requestId):
        lock = Lock()
        self.locks_dict[requestId] = lock
        lock.acquire()
            