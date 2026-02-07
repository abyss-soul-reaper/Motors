from APP.core.result.base_result import BaseResult

class Pagination_result(BaseResult):
    def __init__(self):
        super().__init__()
        self.payload = {
            "items": None,
            "curt_page": None
        }
        self.meta = {
            "total_pages": None,
            "per_page": None,
            "total_items": None,
            "can_move": False
        }