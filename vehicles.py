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

    def upt_v_ifo(self, v_id, upts):
        vehicles = self.load_data()
        
        if v_id in vehicles:
            vehicle = vehicles.get(v_id)
            vehicle.update(upts)
        
        self.save_data(vehicles)

    def buy_vehicles(self, brand, model, year):
        v_id, vehicles = self.the_finder(brand, model, year)
        if v_id is None:
            print('')
            return False

        v_data = vehicles[v_id]

        crt_qty = v_data['quantity']
        crt_sts = v_data['status']
        if crt_sts == 'available' and crt_qty > 0:
            v_data['quantity'] -= 1
            if v_data['quantity'] == 0: v_data['status'] = self.STATUS_SOLD
        
        self.save_data(vehicles)

    def add_vehicle(self, owner_id, brand, model, v_type, year, price, quantity=1, role='user', status=None):
        if status is None:
            status = self.STATUS_AVAILABLE

        vehicles = self.load_data()
        vehicle_id = str(uuid.uuid4())

        vehicles[vehicle_id] = {
            "owner_id": owner_id,
            "brand": brand,
            "model": model,
            "type": v_type,
            "year": year,
            "price": price,
            "quantity": quantity,
            "role": role,
            "status": status.lower(),
            "created_at": datetime.now().isoformat()
        }

        self.save_data(vehicles)
        print(f"✅ Success: {brand} {model} added successfully with ID: {vehicle_id}")
        return vehicle_id

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

    def update_status(self, vehicle_id, new_status, user_role):
        vehicles = self.load_data()

        if user_role.lower() != 'admin':
            print("🚫 Access Denied: Only staff can update vehicle status.")
            return False

        if vehicle_id in vehicles:
            vehicles[vehicle_id]['status'] = new_status
            self.save_data(vehicles)
            print(f"🔄 Status updated to '{new_status}' for vehicle {vehicle_id}.")
            return True

        print(f"⚠️ Error: Vehicle ID {vehicle_id} not found.")
        return False

    def the_finder_interface(self):
            pass

    def get_all_available(self):
        pass

    def view_all_vehicles(self):
        pass

    def smart_add_vehicle(self):
        pass

    def update_vehicle_info(self):
        pass