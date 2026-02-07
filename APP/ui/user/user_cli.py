from datetime import datetime

from APP.core.validation.validators import *
from APP.ui.user.cli_helper import *


class UserInterface:
    """
    CLI layer responsible ONLY for:
    - Collecting user input
    - Displaying data
    - Orchestrating CLI flows (loops, menus)

    No business logic here.
    """

    # ======================================================
    # AUTH INPUTS
    # ======================================================

    def register(self):
        """Collect registration data from user"""
        print("\n--- Register New Account ---")

        name = input("Name: ")
        while not name:
            name = input("❌ Name is required: ")

        email = input("Email: ")
        while not (email and is_valid_email(email)):
            email = input("❌ Invalid Email. Try again: ")

        password = input("Password: ")
        while not password:
            password = input("❌ Password is required: ")

        confirm_password = input("Confirm Password: ")
        while confirm_password != password:
            print("❌ Passwords do not match!")
            confirm_password = input("Try again: ")

        role = input("Enter role (buyer/seller) (default buyer): ")
        if not (role and is_valid_role(role)):
            print("❌ Invalid role. Defaulting to 'buyer'.")
            role = "buyer"

        user_data = {
            "name": name,
            "email": email,
            "password": password,
            "role": role,
            "created_at": datetime.now().isoformat()
        }

        print("\nOptional: Complete your profile? (y/n)")
        if input(">> ").lower() == "y":
            phone = input("Phone: ")
            while not (phone and is_valid_phone(phone)):
                phone = input("❌ Invalid Egyptian Phone: ")

            address = input("Address: ")
            while not address:
                address = input("❌ Address can't be empty: ")

            user_data.update({
                "phone": phone,
                "address": address,
                "is_profile_complete": True
            })

        return user_data

    def login(self):
        """Collect login credentials"""
        print("\n--- User Login ---")

        email = input("Email: ")
        while not (email and is_valid_email(email)):
            email = input("❌ Invalid Email. Try again: ")

        password = input("Password: ")
        while not password:
            password = input("❌ Password is required: ")

        return {"email": email, "password": password}

    # ======================================================
    # ROLE & PERMISSIONS DISPLAY
    # ======================================================

    @staticmethod
    def role_groups(index_map, role):
        """Display role groups and return selected group"""
        print(f"\n=== {role} Features ===")

        for i, group in index_map.items():
            print(f"-- {i}. {group} --")

        choice = input("Select a group number: ")
        while not choice.isdigit() or int(choice) not in index_map:
            choice = input("❌ Invalid choice. Try again: ")

        return index_map[int(choice)]

    @staticmethod
    def role_features(action_map, group):
        """Display actions for a selected group"""
        print(f"\n=== {group} Actions ===")

        for i, act in action_map.items():
            print(f"-- {i}. {act} --")

        choice = input("Select action number: ")
        while not choice.isdigit() or int(choice) not in action_map:
            choice = input("❌ Invalid choice. Try again: ")

        return action_map[int(choice)]

    # ======================================================
    # PAGINATOR FLOW (ORCHESTRATOR)
    # ======================================================

    def paginator_display(self, sys_ctrl, pag, render_fn):
        """
        Main browsing loop.
        Acts as orchestrator, NOT renderer.
        """
        print("\n--- Available Vehicles ---")

        page_num = 1
        commands = resolve_command

        while True:
            page_state = get_page_state(pag, page_num)

            if not page_state["ok"]:
                print(page_state["reason"])
                return

            page = page_state["page"]
            items = page.payload.get("items", [])
            curt_page = page.payload.get("curt_page", 1)

            total_pages = page.meta.get("total_pages", 1)
            total_items = page.meta.get("total_items", 0)

            # -------- Display --------
            print(f"\nPage {curt_page} of {total_pages} | Total Vehicles: {total_items}")
            render_fn(items)

            # -------- Input --------
            print("\nCommands: [n] Next | [p] Prev | [s] Search | [d] Details | [q] Quit")
            command = input("Enter command: ")
            action = commands(command)

            # -------- Actions --------
            if action["type"] == "NAVIGATION":
                nav_result = update_navigation_state(
                    action["action"], curt_page, pag
                )
                nav_state = handle_navigation_result(nav_result)

                if nav_state["ok"]:
                    page_num = nav_state["next_page"]
                else:
                    print(f"❌ {nav_state['error']}")

            elif action["type"] == "SYSTEM":
                system_command_handler(sys_ctrl, action["action"])

            elif action["type"] == "EXIT":
                print("Exiting vehicle browsing.")
                break

            else:
                print(f"❌ {action.get('error', 'Invalid command')}")

    # ======================================================
    # VEHICLE DISPLAY
    # ======================================================

    @staticmethod
    def render_vehicle_brief(vehicles):
        """Render brief vehicle list"""
        print("-" * 60)

        for idx, vehicle in enumerate(vehicles, 1):
            print(
                f"\n{str(idx).zfill(2)}. "
                f"{vehicle.get('full_name'):<40} | "
                f"{vehicle.get('price', 0):<10,} $"
            )

        print("-" * 60)

    @staticmethod
    def render_vehicle_details(vehicle):
        """Render full vehicle details"""
        print("\n--- Vehicle Details ---")
        print("-" * 50)

        print(f"Full Name: {vehicle.get('full_name')}")
        print(f"Brand    : {vehicle.get('brand')}")
        print(f"Model    : {vehicle.get('model')}")
        print(f"Type     : {vehicle.get('type')}")
        print(f"Category : {vehicle.get('category')}")
        print(f"Price    : {vehicle.get('price', 0):,} $")
        print(f"Year     : {vehicle.get('year')}")

        print("-" * 50)

    # ======================================================
    # VEHICLE INPUTS
    # ======================================================

    @staticmethod
    def select_vehicle(vehicles):
        """Select one vehicle from a list"""
        if not vehicles:
            return None

        if len(vehicles) == 1:
            return vehicles[0]

        print("\nMultiple vehicles found:")
        for i, v in enumerate(vehicles, 1):
            print(
                f"[{i}] {v.get('full_name')} | "
                f"{v.get('price', 0):,} $ | "
                f"Year: {v.get('year', 'N/A')}"
            )

        choice = input("Select vehicle number: ")
        return vehicles[int(choice) - 1]

    def vehicle_details_input(self):
        """Input for vehicle details search"""
        name = input("Enter Vehicle Full Name for details: ")
        while not name:
            name = input("❌ Vehicle name cannot be empty: ")
        return {"full_name": name}

    def advanced_search_input(self):
        """Collect advanced search filters"""
        print("\n--- Advanced Vehicle Search ---")

        brand = input("Brand (optional): ") or None
        model = input("Model (optional): ") or None
        category = input("Category (optional): ") or None

        year_input = input("Year (optional): ")
        year = int(year_input) if year_input.isdigit() else None

        return {
            "brand": brand,
            "model": model,
            "category": category,
            "year": year
        }
