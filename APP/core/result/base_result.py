class BaseResult:
    def __init__(self):
        self.ok = False
        self.error = None
        self.meta = None

    def fail(self, error):
        self.ok = False
        self.error = error
        return self
    
    def success(self):
        self.ok = True
        return self