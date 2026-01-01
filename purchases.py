from base import BaseDataManager

class PurchasesManager(BaseDataManager):
    FILE_PATH = 'purchases.json'
    def __init__(self):
        super().__init__(self.FILE_PATH)