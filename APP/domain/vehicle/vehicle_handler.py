from APP.domain.vehicle.vehicle_result import VehiclesResult

class VehiclesHandler:
    """
    Handler class for all vehicle-related operations.

    Responsibilities:
        - Browse available vehicles.
        - Perform advanced search based on criteria.
        - Retrieve detailed information for a specific vehicle.

    Each method returns a VehiclesResult instance with:
        - data (list[dict]): List of vehicle dictionaries (even if one element).
        - meta (dict): Optional metadata (e.g., total_count).
        - ok (bool): True if operation succeeded or logically valid, False if failed.
        - error (str | None): Error message if any.
    """

    def __init__(self, v_mgr):
        """
        Initialize the handler with a vehicle manager.

        Args:
            v_mgr: Instance of the vehicle manager (v_mgr) responsible for data access.
        """
        self.v_mgr = v_mgr

    def browse_vehicles(self) -> VehiclesResult:
        """
        Retrieve all available vehicles.

        Returns:
            VehiclesResult: Contains:
                - data: list of available vehicles
                - meta: {"total_count": int}
                - ok: True always (empty list is valid)
        """
        res = VehiclesResult()

        res.payload = [
            {"id": v_id, **v_info}
            for v_id, v_info in self.v_mgr.get_all_vehicles().items()
            if v_info.get("status") == "available"
        ]

        if not res.payload:
            res.fail("No available vehicles at the moment.")

        res.meta = {"total_count": len(res.payload)}
        res.payload.sort(key=lambda v: v["price"])
        return res.success()

    def advanced_search(self, criteria: dict) -> VehiclesResult:
        """
        Perform a filtered search on vehicles based on criteria.

        Args:
            criteria (dict): Search parameters, e.g.,
                {"brand": "Toyota", "model": None, "year": 2020, "price": 50000}

        Returns:
            VehiclesResult: Contains:
                - data: list of vehicles matching criteria
                - meta: {"total_count": int}
                - ok: False if no match found, True otherwise
                - error: error message if no match
        """
        res = VehiclesResult()
        vehicles = self.v_mgr.get_all_vehicles()

        filters = {
            "brand": lambda v, c: v.get("brand") == c,
            "model": lambda v, c: v.get("model") == c,
            "category": lambda v, c: v.get("category") == c,
            "year": lambda v, c: v.get("year") == c,
            "price": lambda v, c: v.get("price") is not None and v.get("price") <= c
        }

        data = []
        for v_id, v_info in vehicles.items():
            # Only apply filters that exist in criteria and have non-None values
            if all(
                key in filters and filters[key](v_info, value)
                for key, value in criteria.items()
                if value is not None
            ):
                data.append({"id": v_id, **v_info})

        res.payload = data

        if not res.payload:
            return res.fail("No vehicles match the criteria.")

        res.meta = {"total_count": len(res.payload)}
        res.payload.sort(key=lambda v: v["price"])
        return res.success()

    def vehicle_details(self, v_name) -> VehiclesResult:
        res = VehiclesResult()

        info = self.v_mgr.get_vehicle_by_name(v_name)

        if len(info) < 1:
            res.fail("Vehicle not found or no results.")

        elif len(info) > 1:
            res.meta = {"message": "More than one vehicle exists!", "count": len(info)}
            res.payload = info

        else:
            res.payload = info
        return res.success()
