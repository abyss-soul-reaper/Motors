import uuid
from datetime import datetime
from base import BaseDataManager

class VehiclesManager(BaseDataManager):
    STATUS_AVAILABLE = 'available'
    STATUS_SOLD = 'sold'

    def __init__(self):
        super().__init__("vehicles.json")

    def add_vehicle(self, owner_id, brand, model, year, price, status=None):
        if status is None:
            status = self.STATUS_AVAILABLE

        vehicles = self.load_data()
        vehicle_id = str(uuid.uuid4())

        vehicles[vehicle_id] = {
            "owner_id": owner_id,
            "brand": brand,
            "model": model,
            "year": year,
            "price": price,
            "status": status.lower(),
            "created_at": datetime.now().isoformat()
        }

        self.save_data(vehicles)
        print(f"✅ Success: {brand} {model} added successfully with ID: {vehicle_id}")
        return vehicle_id

    def get_all_vehicles(self):
        return self.load_data()

    def get_user_vehicles(self, user_id):
        all_vehicles = self.load_data()

        user_vehicles = {
            v_id: v_data for v_id, v_data in all_vehicles.items() if v_data['owner_id'] == user_id
            }
        return user_vehicles

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
