class VehiclesHandler():
    def __init__(self, v_mgr):
        self.v_mgr = v_mgr

    def browse_vehicles(self):
        vehicles = self.v_mgr.get_all_vehicles()

        result = {"success": True, "data": [], "error": None, "meta": None}

        result["data"] = [
            {"id": v_id, **v_info}
            for v_id, v_info in vehicles.items()
            if v_info.get("status") == "available"
        ]

        if not result["data"]:
            result["error"] = "No available vehicles at the moment."

        return result

    def advanced_search(self, criteria):
        vehicles = self.v_mgr.get_all_vehicles()
        result = {"success": True, "data": [], "error": None, "meta": None}

        filters = {
            "brand": lambda v,c: v.get("brand", None) == c,
            "model": lambda v,c: v.get("model", None) == c,
            "category": lambda v,c: v.get("category", None) == c,
            "year": lambda v,c: v.get("year", None) == c,
            "price": lambda v,c: v.get("price", None) <= c
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
        result = {"success": False, "data": None, "error": None, "meta": None}

        vehicle_info = self.v_mgr.get_vehicle_by_id(v_id)
        if vehicle_info:
            result["success"] = True
            result["data"] = {"id": v_id,**vehicle_info}

        else:
            result["error"] = "Vehicle not found or no results."

        return result


class VehiclesResult:
    def __init__(self):
        self.ok = False
        self.data = None
        self.data_type = None
        self.error = None
        self.meta = None
    
    def fail(self, error):
        self.ok = False
        self.error = error
        return self
    
    def success(self):
        self.ok = True
        return self