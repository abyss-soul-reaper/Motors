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
    
    def advanced_search(self, criteria):
        vehicles = self.get_vehicles_data()
        results = []

        filters = {
            "brand": lambda v,c: v.get("brand") == c,
            "model": lambda v,c: v.get("model") == c,
            "category": lambda v,c: v.get("category") == c,
            "year": lambda v,c: v.get("year") == c,
            "price": lambda v,c: v.get("price") <= c
        }

        for v_id, v_info in vehicles.items():
            if all(
                filters[key](v_info, value)
                for key, value in criteria.items()
                if value is not None
            ):
            
                results.append({
                    "id": v_id,
                    **v_info
                })

        return sorted(results, key=lambda v: v["price"])
