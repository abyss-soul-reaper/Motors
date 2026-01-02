import re
from datetime import datetime

class UserInterface:
    START_MENU = ('Login', 'Register', 'Exit')
    PHONE_PATTERN = r'^01[0125]\d{8}$'
    EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    LAST_YEAR = datetime.now().year

    def __init__(self):
        pass
    def get_registration_ipt(self):
        print("\n--- Register New Account ---")

        name = input('Name: ').strip().title()
        while not name:
            name = input('❌ Name is required: ').strip().title()

        email = input('Email: ').strip().lower()
        while not (email and re.match(self.EMAIL_PATTERN, email)):
            email = input("❌ Invalid Email. Try again: ").strip().lower()

        password = input('Password: ').strip()
        while not password:
            password = input('❌ Password is required: ').strip()

        confirm_password = input("Confirm Password: ").strip()
        while confirm_password != password:
            print("❌ Passwords do not match!")
            confirm_password = input("Try again: ").strip()

        user_data = {
            "name": name,
            "email": email,
            "password": password
        }

        print("\nOptional: Complete your profile? (y/n)")
        if input('>> ').strip().lower() == 'y':
            
            phone = input('Phone: ').strip()
            while not (phone and re.match(self.PHONE_PATTERN, phone)):
                phone = input('❌ Invalid Egyptian Phone: ').strip()
            user_data["phone"] = phone

            address = input('Address: ').strip().title()
            while not address:
                address = input('❌ Address can\'t be empty: ').strip().title()
            user_data["address"] = address

        return user_data

    def get_authenticate_ipt(self):
        print ('\n--- Login ---')

        email = input('Email: ').strip().lower()
        while not (email and re.match(self.EMAIL_PATTERN, email)):
            email = input("❌ Invalid Email. Try again: ").strip().lower()

        password = input('Password: ').strip()
        while not password:
            password = input('❌ Password is required: ').strip()
        
        user_data = {
            "email": email,
            "password": password
        }
        return user_data
    
    def show_start_menu(self):
        print("\n--- Welcome to Vehicle Management System ---")
        
        for index, option in enumerate(self.START_MENU, 1):
            print(f"  {index}. {option}")
        
        choice = input('\n➤ Select your move: ').strip()
        return choice 

    @staticmethod
    def get_v_data_ipt():
        print("\n--- Add New Vehicle ---")

        brand = input('Brand: ').strip().title()
        while not brand:
            brand = input('❌ Brand is required: ').strip().title()

        model = input('Model: ').strip().title()
        while not model:
            model = input('❌ Model is required: ').strip().title()

        v_type = input('Type (e.g., Sedan, SUV): ').strip().title()
        while not v_type:
            v_type = input('❌ Type is required: ').strip().title()

        while True:
            try:
                year = int(input('Year: ').strip())
                if 1886 <= year <= UserInterface.LAST_YEAR: break 
                print("❌ Please enter a valid year (1886-2026).")
            except ValueError:
                print("❌ Invalid input. Please enter the year as a number.")

        while True:
            try:
                price = int(input('Price: ').strip())
                if price > 0: break
                print("❌ Price must be greater than 0.")
            except ValueError:
                print("❌ Invalid input. Please enter the price as a number.")

        while True:
            qty_input = input('Quantity (Default is 1): ').strip()
            if not qty_input:
                quantity = 1
                break
            try:
                quantity = int(qty_input)
                if quantity > 0: break
                print("❌ Quantity must be at least 1.")
            except ValueError:
                print("❌ Invalid input. Please enter a number or leave it empty.")

        v_data = {
            "brand": brand,
            "model": model,
            "type": v_type,
            "year": year,
            "price": price,
            "quantity": quantity,
        }
        return v_data
    
    @staticmethod
    def get_v_srh_ipt():
        print("\n--- Search Inventory (Press Enter to skip any field) ---")
        v_srh_data = {}

        brand = input('➤ Brand: ').strip().title()
        if brand: v_srh_data["brand"] = brand

        model = input('➤ Model: ').strip().title()
        if model: v_srh_data["model"] = model

        v_type = input('➤ Type : ').strip().title()
        if v_type: v_srh_data["type"] = v_type

        try:
            year_input = input('➤ Year : ').strip()
            if year_input: v_srh_data["year"] = int(year_input)
        except ValueError:
            print("  ⚠️ Invalid year ignored. Searching by other criteria...")

        try:
            price_input = input('➤ Max Price: ').strip()
            if price_input: v_srh_data["price"] = int(price_input)
        except ValueError:
            print("  ⚠️ Invalid price ignored. Searching by other criteria...")

        return v_srh_data
