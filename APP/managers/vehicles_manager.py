from APP.core.base.base import BaseDataManager

class VehiclesManager(BaseDataManager):
    FILE_PATH = r'data\vehicles.json'
    
    def __init__(self):
        super().__init__(self.FILE_PATH)

    def get_all_vehicles(self):
        return self.load_data()

    def get_vehicle_by_id(self, v_id):
        vehicles = self.get_all_vehicles()
        return vehicles.get(v_id)
