from APP.core.result.base_result import BaseResult
from APP.core.utils.errors import wrap_error

class DispatcherResult(BaseResult):
    def __init__(self, stage, feature):
        super().__init__()
        self.stage = stage
        self.feature = feature
        self.payload = {
            "input": None,
            "normalized": None,
            "system": None,
            "result": None
        }

    def fail(self, raw_error):
        self.ok = False
        self.error = wrap_error(self.stage, self.feature, raw_error)
        return self
