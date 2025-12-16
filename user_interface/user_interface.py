import os

def show_available_features(Available_features) :

    print ('\nThat\'s The Available Features.')

    for index, feature in enumerate(Available_features, start=1) :

        print (f'- {index} {feature}')

def check_user_data(email_to_check) :

    file_name = 'data_files/User Data.txt'

    if not os.path.exists(file_name) :

        return False

    with open (file_name, 'r', encoding= 'utf-8') as file :

        for line in file :

            if "Name|Email|Password|Address|Phone" in line:

                continue

            user_info = line.strip().split('|')

            if len(user_info) > 1 and  user_info[1].lower() == email_to_check.lower() :

                return True
            
    return False

def get_user_name(email) :
    
    file_name = 'data_files/User Data.txt'

    user_name = None

    try :
            
        with open (file_name, 'r', encoding= 'utf-8') as file :

            for line in file :

                if "Name|Email|Password|Address|Phone" in line:

                    continue

                user_info = line.strip().split('|')

                if len(user_info) > 1 and  user_info[1].lower() == email.lower() :

                    return user_info[0]

    except FileNotFoundError :

        print(f"\n⚠️ Error: File '{file_name}' not found.")
        return None

    return user_name

def get_new_info(current_data, Termination_Terms) :

    current_name = current_data['Name']
    current_email = current_data['Email']
    current_password = current_data['Password']
    current_address = current_data['Address']
    current_phone = current_data['Phone']

    print("\nUser Data Update Options:")
    print("\n1. Partial Update (Change one or more fields).")
    print("\n2. Full Re-entry (Fill all fields again).")
    print("\n3. Cancel Update.")

    choice = input().strip()

    if choice == '3' or choice.capitalize() in Termination_Terms :

        print("\n🚫 Update operation cancelled.")
        return None, None, None, None, None # Return None for all fields
    
    elif choice == '1' :

        print("\n📝 Partial Update Mode (Leave blank to keep current value):")

        # --- Name ---
        new_name = input(f"   Name (Current: {current_name}): ").strip().capitalize()
        new_name = new_name if new_name else current_name
        
        # --- Email ---
        new_email = input(f"   Email (Current: {current_email}): ").strip().lower()
        new_email = new_email if new_email else current_email
        
        # --- Password ---
        new_password = input(f"   Password (Current: {current_password}): ").strip()
        new_password = new_password if new_password else current_password

        # --- Address ---
        new_address = input(f"   Address (Current: {current_address}): ").strip().title()
        new_address = new_address if new_address else current_address
        
        # --- Phone ---
        new_phone = input(f"   Phone (Current: {current_phone}): ").strip()
        new_phone = new_phone if new_phone else current_phone

        return new_name, new_email, new_password, new_address, new_phone
    
    elif choice == '2' :

        print("\n📝 Full Re-entry Mode (All fields must be filled):")
        
        # --- New Name ---
        new_name = input("   New Name: ").strip().capitalize()
        while not new_name:
            new_name = input("   Name cannot be empty. Enter Name: ").strip().capitalize()
            
        # --- New Email ---
        new_email = input("   New Email: ").strip().lower()
        while not new_email:
            new_email = input("   Email cannot be empty. Enter Email: ").strip().lower()
        
        # --- New Password ---
        new_password = input("   New Password: ").strip()
        while not new_password:
            new_password = input("   Password cannot be empty. Enter Password: ").strip()

        # --- New Address ---
        new_address = input("   New Address: ").strip().title()
        while not new_address:
            new_address = input("   Address cannot be empty. Enter Address: ").strip().title()
            
        # --- New Phone ---
        new_phone = input("   New Phone: ").strip()
        while not new_phone:
            new_phone = input("   Phone cannot be empty. Enter Phone: ").strip()
            
        return new_name, new_email, new_password, new_address, new_phone

    else:
        print("\n⚠️ Invalid option. Update cancelled.")
        return None, None, None, None, None

def contact_us():
    
    """Displays all official and social contact channels."""
    
    print("📞 Contact Us & Support 📞")
    print("=" * 55)
    print("For sales, support, or inquiries, please use the following channels:")
    print("-" * 55)

    print("### Official Contact ###")
    print("📧 Email Support: support@motors.com") 
    print("☎️ Phone (Sales): +20 100 123 4567")
    print("📍 Main Office: 123 Autostrad St, New Cairo, Egypt")
    print("-" * 55)

    print("--- Social Media & Messaging ---")
    print("🔵 Facebook: MotorsOfficial")
    print("📸 Instagram: @MotorsEG")
    print("🟢 WhatsApp: +20 100 123 4567 (Direct chat)")
    print("💬 Telegram: t.me/MotorsSupport")
    print("🖥️ Website: www.motors.com") 
    
    print("=" * 55)
