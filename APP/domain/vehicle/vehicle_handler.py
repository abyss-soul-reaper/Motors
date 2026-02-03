from APP.domain.vehicle.vehicle_result import VehiclesResult

class VehiclesHandler():
    def __init__(self, v_mgr):
        self.v_mgr = v_mgr

    def browse_vehicles(self):
        vehicles = self.v_mgr.get_all_vehicles()
        res = VehiclesResult()

        res.data = [
            {"id": v_id, **v_info}
            for v_id, v_info in vehicles.items()
            if v_info.get("status") == "available"
        ]

        if not res.data:
            res.fail("No available vehicles at the moment.")

        return res.success()
    
    def advanced_search(self, criteria):
        vehicles = self.v_mgr.get_all_vehicles()
        res = VehiclesResult()

        filters = {
            "brand": lambda v,c: v.get("brand", None) == c,
            "model": lambda v,c: v.get("model", None) == c,
            "category": lambda v,c: v.get("category", None) == c,
            "year": lambda v,c: v.get("year", None) == c,
            "price": lambda v,c: v.get("price", None) <= c
        }
        data = []

        for v_id, v_info in vehicles.items():
            if all(
                filters[key](v_info, value)
                for key, value in criteria.items()
                if value is not None
            ):
                res.data = data.append({"id": v_id,**v_info})

        if not res.data:
            return res.fail("No vehicles match the criteria.")

        res.data.sort(key=lambda v: v["price"])
        return res.success

    def vehicle_details(self, v_id):
        vehicle_info = self.v_mgr.get_vehicle_by_id(v_id)
        res = VehiclesResult()

        if vehicle_info:
            res.data = {"id": v_id,**vehicle_info}
        else:
            res.fail("Vehicle not found or no results.")

        return res.success()
