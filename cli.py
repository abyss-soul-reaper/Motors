import re

class UserInterface:
    START_MENU = ('Login', 'Register', 'Exist')
    PHONE_PATTERN = r'^01[0125]\d{8}$'
    EMAIL_PATTERN = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    def __init__(self):
        pass

    def get_registration_input(self):
        name = input('   Name: ').strip().lower()
        while not name:
            name = input('  Name can\'t be empty. Enter Name: ').strip().lower()

        email = input('   Email: ').strip().lower()
        while not (email and re.match(self.EMAIL_PATTERN, email)):
            email = input("   ❌ Invalid Email. Enter a valid Email: ").strip().lower()

        password = input('   Password: ').strip().lower()
        while not password:
            password = input('   Password can\'t be empty. Enter Password: ').strip().lower()
        
        phone = None
        address = None
        
        complete = input('   Complete Profile Now? (y/n): ').strip().lower()
        if complete == 'y':
            
            phone = input('   Phone: ').strip()
            while not (phone and re.match(self.PHONE_PATTERN, phone)):
                phone = input('   ❌ Invalid Phone. Enter Egyptian Phone: ').strip()

            address = input('   Address: ').strip().title()
            while not address:
                address = input('   Address can\'t be empty. Enter Address').strip().title()

        return name, email, password, phone, address
    
    @staticmethod
    def get_login_input():
        email = input('   📧 Email: ').strip().lower()
        password = input('   🔑 Password: ').strip()
        return email, password
    
    def show_start_menu(self):
        for operation in self.START_MENU:
            print(f'   - {operation}')
        choice = input('\nSelect an option from the menu: ').strip().lower()
        return choice