from APP.core.result.base_result import BaseResult

class VehiclesResult(BaseResult):
    def __init__(self):
        super().__init__()
        self.data = []
        self.data_type = None

