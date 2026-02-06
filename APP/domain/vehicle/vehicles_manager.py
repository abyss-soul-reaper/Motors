from APP.core.base.base import BaseDataManager

class VehiclesManager(BaseDataManager):
    FILE_PATH = r'data\vehicles.json'
    
    def __init__(self):
        super().__init__(self.FILE_PATH)

    def get_all_vehicles(self):
        return self.load_data()

    def get_vehicle_by_name(self, v_name):
        vehicles = self.get_all_vehicles()
        details = [
            {"id": v_id, **v_info}
            for v_id, v_info in vehicles.items()
            if v_info.get("full_name") == v_name
        ]

        return details
