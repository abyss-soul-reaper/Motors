from APP.core.base import BaseDataManager

class VehiclesManager(BaseDataManager):
    FILE_PATH = r'data\vehicles.json'
    
    def __init__(self):
        super().__init__(self.FILE_PATH)

    def get_vehicles_data(self):
        return self.load_data()

    def browse_vehicles(self):
        vehicles = self.get_vehicles_data()

        return [
            {
                "id": v_id,
                **v_info
            }
            for v_id, v_info in vehicles.items()
            if v_info.get("status") == "available"
        ]
    
    def vehicle_details(self, v_id):
        vehicles = self.get_vehicles_data()
        vehicle_info = vehicles.get(v_id)
        if vehicle_info:
            return {
                "id": v_id,
                **vehicle_info
            }
        return None    
