# from APP.core.base.base import BaseDataManager

# class VehiclesManager(BaseDataManager):
#     FILE_PATH = r'data\vehicles.json'
    
#     def __init__(self):
#         super().__init__(self.FILE_PATH)

#     def get_vehicles_data(self):
#         return self.load_data()

#     def browse_vehicles(self):
#         vehicles = self.get_vehicles_data()

#         result = {"success": True, "data": [], "error": None, "meta": None}

#         result["data"] = [
#             {"id": v_id, **v_info}
#             for v_id, v_info in vehicles.items()
#             if v_info.get("status") == "available"
#         ]

#         if not result["data"]:
#             result["error"] = "No available vehicles at the moment."

#         return result

#     def advanced_search(self, criteria):
#         vehicles = self.get_vehicles_data()
#         result = {"success": True, "data": [], "error": None, "meta": None}

#         filters = {
#             "brand": lambda v,c: v.get("brand", None) == c,
#             "model": lambda v,c: v.get("model", None) == c,
#             "category": lambda v,c: v.get("category", None) == c,
#             "year": lambda v,c: v.get("year", None) == c,
#             "price": lambda v,c: v.get("price", None) <= c
#         }

#         for v_id, v_info in vehicles.items():
#             if all(
#                 filters[key](v_info, value)
#                 for key, value in criteria.items()
#                 if value is not None
#             ):
#                 result["data"].append({"id": v_id,**v_info})

#         if not result["data"]:
#             result["success"] = False
#             result["error"] = "No vehicles match the criteria."

#         result["data"].sort(key=lambda v: v["price"])
#         return result

#     def vehicle_details(self, v_id):
#         vehicles = self.get_vehicles_data()
#         result = {"success": False, "data": None, "error": None, "meta": None}

#         vehicle_info = vehicles.get(v_id, None)
#         if vehicle_info:
#             result["success"] = True
#             result["data"] = {"id": v_id,**vehicle_info}

#         else:
#             result["error"] = "Vehicle not found or no results."

#         return result

# import uuid
# from APP.core.base.base import BaseDataManager
# from APP.core.security.security import hash_password
# from APP.core.validation.validators import is_valid_email, is_valid_phone

# class UserManager(BaseDataManager):
#     FILE_PATH = r'data\users.json'

#     def __init__(self):
#         super().__init__(self.FILE_PATH)

#     def get_users_data(self):
#         return self.load_data()

#     def register(self, user_data):
#         result = {"success": False, "data": None, "error": None, "meta": None}

#         email = user_data.get("basic_info", {}).get("email", "").lower()
#         phone = user_data.get("contact_info", {}).get("phone", "")

#         if not is_valid_email(email):
#             result["error"] = "Invalid email address"
#             return result

#         if phone and not is_valid_phone(phone):
#             result["error"] = "Invalid phone number"
#             return result

#         users = self.get_users_data()

#         for usr_data in users.values():
#             if usr_data["basic_info"]["email"].lower() == email:
#                 result["error"] = "Email already exists"
#                 return result

#         user_data.pop("user_id", None)
#         user_id = str(uuid.uuid4())
#         user_data["basic_info"]["password"] = hash_password(
#             user_data["basic_info"]["password"]
#         )
#         users[user_id] = user_data
#         self.save_data(users)

#         result["success"] = True
#         result["data"] = {
#             "user_id": user_id,
#             "role": user_data["account"]["role"],
#             "is_profile_complete": user_data["account"]["is_profile_complete"]
#         }

#         return result

#     def login(self, user_data):
#         result = {"success": False, "data": None, "error": None, "meta": None}

#         users = self.get_users_data()
#         email = user_data.get("email", "").lower()
#         password = hash_password(user_data.get("password", ""))

#         for u_id, u_data in users.items():
#             if (
#                 u_data["basic_info"]["email"].lower() == email
#                 and u_data["basic_info"]["password"] == password
#             ):
#                 result["success"] = True
#                 result["data"] = {
#                     "user_id": u_id,
#                     "role": u_data["account"]["role"],
#                     "is_profile_complete": u_data["account"]["is_profile_complete"]
#                 }
#                 return result
            
#         result["error"] = "Invalid email or password"
#         return result
