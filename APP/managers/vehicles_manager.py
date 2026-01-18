from APP.core.base import BaseDataManager

class VehiclesManager(BaseDataManager):
    FILE_PATH = r'data\vehicles.json'
    
    def __init__(self):
        super().__init__(self.FILE_PATH)

    def browse_vehicles(self):
        vehicles = self.load_data()

        return [
            {
                "id": v_id,
                **v_info
            }
            for v_id, v_info in vehicles.items()
            if v_info.get("status") == "available"
        ]
