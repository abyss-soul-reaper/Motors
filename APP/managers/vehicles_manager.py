from APP.core.base.base import BaseDataManager

class VehiclesManager(BaseDataManager):
    FILE_PATH = r'data\vehicles.json'
    
    def __init__(self):
        super().__init__(self.FILE_PATH)

    def get_vehicles_data(self):
        return self.load_data()

    def browse_vehicles(self):
        vehicles = self.get_vehicles_data()

        result = {"success": True, "data": [], "error": None, "meta": None}

        result["data"] = [
            {"id": v_id, **v_info}
            for v_id, v_info in vehicles.items()
            if v_info.get("status") == "available"
        ]

        if not result["data"]:
            result["success"] = False
            result["error"] = "No available vehicles at the moment."

        return result

    def advanced_search(self, criteria):
        vehicles = self.get_vehicles_data()
        result = {"success": True, "data": [], "error": None, "meta": None}

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
                result["data"].append({"id": v_id,**v_info})

        if not result["data"]:
            result["success"] = False
            result["error"] = "No vehicles match the criteria."

        result["data"].sort(key=lambda v: v["price"])
        return result

    def vehicle_details(self, v_id):
        vehicles = self.get_vehicles_data()
        result = {"success": False, "data": None, "error": None, "meta": None}

        vehicle_info = vehicles.get(v_id)
        if vehicle_info:
            result["success"] = True
            result["data"] = {"id": v_id,**vehicle_info}

        else:
            result["error"] = "Vehicle not found or no results."

        return result
