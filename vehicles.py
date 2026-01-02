import uuid
from datetime import datetime
from base import BaseDataManager

class VehiclesManager(BaseDataManager):
    STATUS_AVAILABLE = 'available'
    STATUS_SOLD = 'sold'
    FILE_PATH = "vehicles.json"

    def __init__(self):
        super().__init__(self.FILE_PATH)

    def advanced_search(self, filters):
        vehicles = self.load_data()
        results = {}

        for v_id, v_data in vehicles.items():
            match = True

            for key, value in filters.items():
                if key in v_data and v_data[key] != value:
                    match = False

            if match:
                results[v_id] = v_data
        return results

    def smart_add(self, new_v_data):
        vehicles = self.load_data()
        search_filter = {
            "brand": new_v_data.get("brand"),
            "model": new_v_data.get("model"),
            "year": new_v_data.get("year")
        }
        is_exsist = self.advanced_search(search_filter)

        if is_exsist:
            v_id = list(is_exsist.keys())[0]
            new_v_data = self._calculate_averages(vehicles.get(v_id), new_v_data)
            self.upt_v_ifo(v_id, new_v_data)
            return True
        
        v_id = str(uuid.uuid4())
        vehicles[v_id] = new_v_data
        self.save_data(vehicles)
        return True
        
    def upt_v_ifo(self, v_id, upts):
        vehicles = self.load_data()
        
        if v_id in vehicles:
            vehicle = vehicles.get(v_id)
            vehicle.update(upts)
        
        self.save_data(vehicles)

    @staticmethod
    def _calculate_averages(old_data, new_data):
        old_qty = old_data.get("quantity", 0)
        old_price = old_data.get("price", 0)
        new_qty = new_data.get("quantity", 1)
        new_price = new_data.get("price", 0)

        total_qty = old_qty + new_qty
        if total_qty > 0:
            avg_price = ((old_price * old_qty) + (new_price * new_qty)) // total_qty
        else:
            avg_price = new_price
        new_data["quantity"] = total_qty
        new_data["price"] = avg_price

        return new_data

    def buy_vehicles(self, filters):
        results = self.advanced_search(filters)
        if not results:
            print("⚠️ Error: No matching vehicle found.")
            return False
        
        v_id = list(results.keys())[0]
        v_data = results[v_id]
        if v_data["status"] == self.STATUS_AVAILABLE and v_data.get("quantity", 0) > 0:
            v_data["quantity"] -= 1

            if v_data['quantity'] == 0:
                v_data['status'] = self.STATUS_SOLD 

            vehicles = self.load_data()
            vehicles[v_id]  = v_data
            self.save_data(vehicles)
        
            print(f"✅ Purchase successful! Remaining quantity: {v_data['quantity']}")
            return True
        
        print("🚫 Vehicle is not available for sale.")
        return False

    def delete_vehicle(self, vehicle_id, requester_id, requester_role):
        vehicles = self.load_data()
        vehicle = vehicles.get(vehicle_id)

        if vehicle:
            is_owner = vehicle['owner_id'] == requester_id
            is_admin = requester_role == 'admin'

            if is_owner or is_admin:
                vehicles.pop(vehicle_id)
                self.save_data(vehicles)
                print(f"🗑️ Vehicle {vehicle_id} deleted successfully.")
                return True
            print("🚫 Permission Denied: You don't have authority to delete this.")
            return False

        print(f"⚠️ Error: Vehicle ID {vehicle_id} not found.")
        return False
