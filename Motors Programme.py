import os

import string

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print (os.getcwd())

Available_features = ('Add', 'Remove', 'Clear', 'View', 'Total Price', 'Price List', 'Update User Info', 'Feedback', 'Contact Us', 'Favourite Vehicles')

Consent_Terms = ('Yes', 'Ok', 'Yeah', 'Yup', 'Confirm', 'Y', 'O')

Termination_Terms = ('No', 'Nope', 'Cancel','Done', 'N', 'C', 'D' )

vehicles= {
    "Cars": {
        "Sport": {
            "Bugatti Chiron Super Sport 300+": 3900000,
            "Koenigsegg Jesko Absolut": 2800000,
            "McLaren Speedtail": 2250000,
            "Ferrari SF90 Stradale": 520000,
            "Lamborghini Huracan STO": 330000,
            "Porsche 911 GT3 RS": 240000,
            "Audi R8 V10 Performance": 190000,
            "Chevrolet Corvette Z06": 110000,
            "BMW M4 Competition": 87000,
            "Ford Mustang Shelby GT500": 80000
        },
        "SUV": {
            "Rolls-Royce Cullinan": 350000,
            "Bentley Bentayga Speed": 250000,
            "Lamborghini Urus": 230000,
            "Mercedes-AMG G 63": 179000,
            "Range Rover Autobiography LWB": 185000,
            "Porsche Cayenne Turbo GT": 196000,
            "Cadillac Escalade V": 150000,
            "BMW X7 M60i": 125000,
            "Audi RS Q8": 120000,
            "Lexus LX 600 F Sport": 105000
        },
        "Truck": {
            "GMC Hummer EV Pickup Edition 1": 115000,
            "Ford F-150 Raptor R": 109000,
            "Ram 1500 TRX": 85000,
            "Rivian R1T": 75000,
            "Chevrolet Silverado ZR2": 72000,
            "GMC Sierra 1500 Denali Ultimate": 83000,
            "Toyota Tundra Capstone": 76000,
            "Ford Ranger Raptor": 55000,
            "Nissan Frontier Pro-4X": 45000,
            "Honda Ridgeline Black Edition": 49000
        },
        "Electric": {
            "Tesla Model S Plaid": 110000,
            "Porsche Taycan Turbo S": 190000,
            "Lucid Air Grand Touring": 138000,
            "Mercedes-Benz EQS 580": 127000,
            "BMW iX M60": 110000,
            "Audi e-tron GT": 105000,
            "Ford Mustang Mach-E GT": 69000,
            "Polestar 2 Long Range Dual Motor": 62000,
            "Kia EV6 GT": 55000,
            "Hyundai Ioniq 5 Limited": 52000
        }
    },
    "Bikes": {
        "Sport": {
            "Ducati Superleggera V4": 100000,
            "Kawasaki Ninja H2R": 58000,
            "BMW M 1000 RR": 33000,
            "Honda CBR1000RR-R Fireblade SP": 28000,
            "Yamaha YZF-R1M": 27000,
            "Aprilia RSV4 Factory 1100": 26000,
            "KTM 1290 Super Duke R Evo": 19500,
            "Suzuki GSX-R1000R": 18000,
            "Triumph Speed Triple 1200 RS": 18500,
            "Kawasaki ZX-10R KRT Edition": 17000
        },
        "Cruiser": {
            "Harley-Davidson CVO Road Glide Limited": 50000,
            "Ducati Diavel V4": 27000,
            "Indian Challenger Dark Horse": 27000,
            "Triumph Rocket 3 R": 23500,
            "Harley-Davidson Fat Boy 114": 22000,
            "Indian Scout Rogue": 12000,
            "Honda Rebel 1100": 9500,
            "Yamaha Bolt R-Spec": 8500,
            "Kawasaki Vulcan S": 7300,
            "Suzuki Boulevard M109R B.O.S.S.": 15000
        },
        "Adventure": {
            "Ducati Multistrada V4 Rally": 29000,
            "BMW R 1300 GS": 19000,
            "KTM 1290 Super Adventure R": 21000,
            "Triumph Tiger 1200 Rally Pro": 23000,
            "Harley-Davidson Pan America 1250 Special": 20000,
            "Honda Africa Twin CRF1100L": 15000,
            "Yamaha Tenere 700": 10500,
            "Suzuki V-Strom 1050XT": 15000,
            "Kawasaki Versys 1000 SE LT+": 18000,
            "KTM 890 Adventure R": 14000
        },
        "Electric": {
            "Arc Vector": 120000,
            "LiveWire One (Harley-Davidson)": 23000,
            "Energica Ego+ RS": 25000,
            "Zero SR/S Premium": 20000,
            "Zero DSR/X": 21000,
            "Cake Kalk OR": 13000,
            "Fantic Motor Caballero 500 E": 15000,
            "Lightning LS-218": 38000,
            "Damon Hypersport Premier": 40000,
            "Super Soco TC Max": 5500
        }
    }
}

def sort_names_alphabetically(vehicles_dict) :

    file_name = 'vehicles_data.txt'

    cars_list = []

    bikes_list = []

    all_vehicles = []

    for category, types in vehicles_dict.items() :

        for type_name, cars in types.items() :

            for car_name, price in cars.items() :

                if category == 'Cars' :

                    cars_list.append((car_name, category, price))

                elif category == 'Bikes' :

                    bikes_list.append((car_name, category, price))

    all_vehicles = cars_list + bikes_list

    output_lines = []

    for letter in string.ascii_uppercase : 
    
        starting_with_letter = []

        for name, category, price_t in all_vehicles :

            if name.startswith(letter) :

                starting_with_letter.append((name, category, price_t))

        if not starting_with_letter :

            continue

        output_lines.append(f'-' * 30)

        output_lines.append(f'-{letter}-')

        output_lines.append('-' * 30)

        sorted_group = sorted(starting_with_letter, key=lambda x:(0 if x[1] == 'Cars' else 1, x[0], x[2]))

        category_n = ''

        for cars_n, category_t, price_v in sorted_group :
                                
                if category_t != category_n :
                                
                    output_lines.append(f'{category_t}')

                    category_n = category_t

                output_lines.append(f'- {cars_n} : {price_v:,}$')

    output_lines.append('Sorting Finished.')

    final_output = '\n'.join(output_lines)

    if not os.path.exists(file_name) :

        print ('File Not Found. Creating New File...')

        with open (file_name, 'w', encoding= 'utf-8') as file :
            
            file.write(final_output)

    else :

        print ('File\'s Already Exists.')
    
    return final_output  

def available_features() :

    print ('That\'s The Available Features.')

    for index, feature in enumerate(Available_features, start=1) :

        print (f'- {index} {feature}')

def check_user_data(email_to_check) :

    file_name = 'User Data.txt'

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
    
    file_name = 'User Data.txt'

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

        print(f"⚠️ Error: File '{file_name}' not found.")
        return None

    return user_name

def save_useres_data() :

    file_name = 'User Data.txt'

    # --- Name ---
    name = input ('Please Write Your Name.\n').strip().capitalize()

    # --- Email ---
    email = input (f'Please Write Your Email {name}.\n').strip().lower()

    while '@gmail.com' not in email :

        print ('Invalid Email.')

        email = input ('Please Write Your Email And Make Sure It Contains @gmail.com\n').strip().lower()

    # --- Password ---
    password = input ('Please Write Your Password.').strip().lower()

    # --- Address ---
    address = input ('Please Write Your Address.\n').strip().title()

    # --- Phone ---
    phone = input ('Please Write Your Phone.\n').strip()

    user_data = f'{name}|{email}|{password}|{address}|{phone}\n'

    if check_user_data(email) :

        print ('🔴 Error: This Email Address Already Exists. Data Not Saved.')

        return False, None
    
    if not os.path.exists(file_name) :

        print ('File Not Found. Creating New File...')

        with open (file_name, 'w', encoding= 'utf-8') as file :

            file.write('Name|Email|Password|Address|Phone\n')

            file.write(user_data)

    else :

        with open (file_name, 'a', encoding= 'utf-8') as file :

            file.write(user_data)

    print(f"✅ User {name} registered successfully!")

    return True, email
    
def ensure_cart_file_exists() :

    file_name = 'Cart Data.txt'

    if not os.path.exists(file_name) :

        with open (file_name, 'w', encoding= 'utf-8') as file :

            file.write('Email|Cart Items\n')

def get_user_cart(email_to_check) :

    ensure_cart_file_exists()

    file_name = 'Cart Data.txt'

    user_cart = []

    with open (file_name, 'r', encoding= 'utf-8') as file :

        for line in file :

            if 'Email|Cart Items' in line :

                continue

            cart_info = line.strip().split("|")

            if len(cart_info) > 1 :

                if cart_info[0].lower() == email_to_check.lower() :

                    user_cart_raw = cart_info[1:]

                    user_cart = [item.strip() for item in user_cart_raw if item.strip()]

                    return user_cart

    return user_cart

def update_user_cart(email, new_cart_items) :

    found_and_updated = False

    file_name = 'Cart Data.txt'

    with open (file_name, 'r', encoding= 'utf-8') as file :

        lines = file.readlines()

    new_cart_str = '|'.join(new_cart_items)

    new_line = f'{email.lower()}|{new_cart_str}\n'

    for i in range(len(lines)) :

        if i == 0 :

            continue

        line_email = lines[i].split('|')[0].strip().lower()

        if line_email == email.lower() :

            lines[i] = new_line

            found_and_updated = True

            break

    if not found_and_updated :

        lines.append(new_line)

    with open (file_name, 'w', encoding= 'utf-8') as file :

        file.writelines(lines)

    return True

def show_vehicles(vehicles_dict) :
    
    all_vehicles_list = []

    for category, types in vehicles_dict.items() :
        for type_name, cars in types.items() :
            for car_name, price in cars.items() :

                all_vehicles_list.append((price, category, type_name, car_name))

    all_vehicles_list.sort()

    count = 1
    current_type = ''
    
    print("=" * 50)
    print("✨ Available Vehicles (Sorted by Price) ✨")
    print("=" * 50)
    
    for price, main_category, type_name, car_name in all_vehicles_list :
        
        if type_name != current_type :
            print("-" * 40)
            print(f"- 🚗 {main_category} - {type_name.upper()} -")
            print("-" * 40)
            current_type = type_name 

        print(f'{str(count).zfill(2)}. {car_name:<30} | Price: {price:10,}$ ({main_category})')
        
        count += 1
        
    print("=" * 50)
    
    return [name for price, category, type_name, name in all_vehicles_list]

def add_items_logic(current_cart, vehicles_dict) :

    updated_cart = list (current_cart)

    count = 0

    print("💡 Displaying vehicles list to assist you...")

    ordered_vehicles = show_vehicles(vehicles_dict)

    cars_list = {car_name.lower() for car_name in ordered_vehicles}

    while True :

        item_to_add = input ('Please Write The Item That You Want To Add.\n').strip()

        count += 1

        if item_to_add.capitalize() in ('Done', 'Finish', 'D', 'F') :
            if count == 1 :

                print ('🚫 No new items were added. Cart remains unchanged.')
            else :

                print ('✅ Finished Adding items. Cart updated.')
            break

        try :

            item_index = int(item_to_add)

            if 1 <= item_index <= len(ordered_vehicles) :

                chosen_item = ordered_vehicles[item_index - 1]

                if chosen_item.lower() in cars_list:

                    updated_cart.append(chosen_item)

                    print (f'✅ successfully Added BY Number. "{chosen_item.strip()}"')

                    print ("🛒 Cart after Addition:")

                    for index, item in enumerate(updated_cart, start= 1) :

                        print (f'- {index} {item}')
                    continue

                else: 
                    print(f'⚠️ Internal Error: Item "{chosen_item}" not found in available list.')

            else :

                print ('⚠️ The number you entered is out of range. Please enter a valid number or name.')

                continue

        except ValueError :

            if item_to_add.lower() in cars_list :

                updated_cart.append(item_to_add)
                print (f'✅ successfully Added by Name. "{item_to_add.strip()}"')

                print ("🛒 Cart after Addition:")

                for index, item in enumerate(updated_cart, start= 1) :

                    print (f'- {index} {item}')

            else :

                print ('⚠️ The item you entered is not available. Please choose from the available vehicles.')

    return updated_cart

def addition(email) :

    user_cart = get_user_cart(email)

    view_cart(email)

    final_cart_items = add_items_logic(user_cart, vehicles)

    if final_cart_items != user_cart :

        update_user_cart(email, final_cart_items)

def remove_items_logic(current_cart) :

    if not current_cart :

        print ('🛒 Your Cart Is Empty')

        return current_cart
    
    temp_cart = list(current_cart)

    count = 0

    items_removed_successfully = False

    while True :

        item_index_to_remove = input ('Enter The Number OF The Item You Want To Remove: ').strip()

        count += 1

        if item_index_to_remove.capitalize() in Termination_Terms :

            if count == 1 :

                print ('🚫 No new items were removed. Cart remains unchanged.')

                return temp_cart

            if items_removed_successfully :

                print('✅ Finished removing items. Cart updated.')

                return temp_cart
            
            else :

                print('❌ Removal operation cancelled. No items were removed.')    

                return temp_cart
            
        try:

            index_to_remove = int(item_index_to_remove)

            if 1 <= index_to_remove <= len(temp_cart) :

                items_removed_successfully = True

                removed_item = temp_cart.pop(index_to_remove - 1)

                print (f'🗑️ Successfully removed "{removed_item.strip()}".')

                print ("🛒 Cart after removal:")

                for index, item in enumerate(temp_cart, start= 1) : 

                    print (f'- {index} {item}')

                if not temp_cart :

                    print ("✅ Last item removed. Cart is now empty.")

                    return temp_cart
                
            else :

                print ('⚠️ The number you entered is out of range.')

        except ValueError:

            print ('⚠️ Invalid input. Please enter the item number.')

def removal(email) :

    user_cart = get_user_cart(email)

    if user_cart:

        view_cart(email)

    final_cart_items = remove_items_logic(user_cart)

    if final_cart_items != user_cart :

        update_user_cart(email, final_cart_items)

def clear(email) :

    user_cart = get_user_cart(email)

    view_cart(email)

    if user_cart :

        update_user_cart(email, [])

        print ('✅ Cart data successfully reset and saved.')

def view_cart(email_to_check) :

    user_cart =get_user_cart(email_to_check) 

    if not user_cart:

        print('🛒 Your Cart Is Empty')

    else :

        print ('🛒 Your Current Cart Items:')

        for index, items in enumerate(user_cart, start=1) :

            print (f'- {index} {items.strip()}')

def get_price_map(vehicles_dict) :

    price_map = {}

    for category, types in vehicles_dict.items() :

        for type_name, cars in types.items() :

            for car_name, price in cars.items() :

                price_map[car_name.lower()] = price

    return price_map

def calculate_total_price(user_cart, vehicles_dict) :

    if not user_cart :
        print("🛒 Your cart is empty. Total Price: 0$")
        return 0
    
    print("🧾 Generating Cart Summary and Total Price...")
    print("-" * 40)

    price_map = get_price_map(vehicles_dict)

    total_price = 0

    item_count = 0

    for item in user_cart :

        item_lower = item.lower()

        if item_lower in price_map :
            price = price_map[item_lower]
            total_price += price
            item_count += 1

            print (f'| {item_count}. {item:<25} | {price:10,}$ |')

        else :

            print(f"| ⚠️ Item not found: {item:<25} | UNAVAILABLE |")
            
    print("-" * 40)
    print(f"| Total Items: {item_count:<25} | {total_price:10,}$ |")
    print("-" * 40)
    
    return total_price

def total_price(email,vehicles_dict) :

    user_cart = get_user_cart(email)

    if not user_cart :

        print("🛒 Your cart is empty. No total to calculate.")
        return
    
    calculate_total_price(user_cart, vehicles_dict)

def search(vehicles_dict) :

    all_vehicles = []

    for category, types in vehicles_dict.items() :

        for type_name, cars in types.items() :

            for car_name, price in cars.items() :

                all_vehicles.append((price, car_name, category))

    return all_vehicles

def price_list(vehicles_dict) :

    price_limits = [20000, 50000, 100000, 500000, 1000000, 2000000, 3000000, 4000000]

    all_vehicles = search(vehicles_dict)

    all_vehicles.sort()

    remaining_vehicles = list(all_vehicles)

    current_min_price = 0

    for max_price in price_limits :

        vehicles_in_range = []

        i = 0

        while i < len(remaining_vehicles) :

            price, car_name, category = remaining_vehicles[i]

            if  price < max_price :

                vehicles_in_range.append((price,car_name,category))
                remaining_vehicles.pop(i)

            else:

                break

        if vehicles_in_range :

            print ('=' * 30)
            print (f'💸 Vehicles Between {current_min_price:,}$ and {max_price:,}$')
            print ('=' * 30)
            
            count = 1

            for price, car_name, category in vehicles_in_range :

                print('-' * 30)
                print (f'- {str(count).zfill(2)}. {car_name} ({category}) Price: {price:,}$')

                count += 1

        current_min_price = max_price

    if remaining_vehicles :

        print ('=' * 50)
        print (f'👑 Exotic Vehicles (Over {price_limits[-1]:,}$):')
        print ('=' * 50)

        count = 1
        for price, car_name, category in remaining_vehicles:

            print (f'- {count}. {car_name} ({category}) Price: {price:,}$')
            count += 1

def get_new_info(current_data) :

    current_name = current_data['Name']
    current_email = current_data['Email']
    current_password = current_data['Password']
    current_address = current_data['Address']
    current_phone = current_data['Phone']

    print("User Data Update Options:")
    print("1. Partial Update (Change one or more fields).")
    print("2. Full Re-entry (Fill all fields again).")
    print("3. Cancel Update.")

    choice = input().strip()

    if choice == '3' or choice.capitalize() in Termination_Terms :

        print("🚫 Update operation cancelled.")
        return None, None, None, None, None # Return None for all fields
    
    elif choice == '1' :

        print("📝 Partial Update Mode (Leave blank to keep current value):")

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

        print("📝 Full Re-entry Mode (All fields must be filled):")
        
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
        print("⚠️ Invalid option. Update cancelled.")
        return None, None, None, None, None

def update_user_info(target_email) :

    file_name = 'User Data.txt'
    lines = []
    found_user = False

    try :

        with open (file_name, 'r', encoding= 'utf-8') as file :

            lines = file.readlines()
    except FileNotFoundError :

        print(f"❌ Error: User data file not found: {file_name}")
        return
    
    for i, line in enumerate(lines) :

        if i == 0 :

            continue

        parts = line.strip().split('|')

        if len(parts) >= 5 and parts[1].strip().lower() == target_email.lower() :

            current_data = {
                'Name': parts[0].strip().capitalize(),
                'Email': parts[1].strip().lower(),
                'Password': parts[2].strip(),
                'Address': parts[3].strip().title(),
                'Phone': parts[4].strip()
            }

        results = get_new_info(current_data)

        if results[0] is None :
            return None, target_email
        
        new_name, new_email, new_password, new_Address, new_phone = results

        updated_line = f'{new_name}|{new_email}|{new_password}|{new_Address}|{new_phone}\n'

        lines[i] = updated_line

        found_user = True
        
        break
    
    if not found_user :

        print(f"❌ User with email '{target_email}' not found.")
        return None, target_email
    
    try :

        with open (file_name, 'w', encoding= 'utf-8') as file :

            file.writelines(lines)

            print("=" * 50)
            print(f"✅ Success! User information for {new_email} has been updated and saved.")
            print("=" * 50)

            if new_email != target_email :

                print(f"❗ Your new email is: {new_email}. Please use it for future logins.")
    except Exception as e :

        print(f"❌ An error occurred while writing to the file: {e}")
    
        return None
    
    return new_name, new_email

def send_feedback(user_email) :

    file_name = 'Feedback.txt'

    print("💬 Feedback and Suggestions Center 💬")
    print("-" * 45)

    feedback_text = input("Please write your feedback/suggestions (or leave blank to cancel):\n> ").strip()

    if not feedback_text :

        print("🚫 No feedback submitted. Thank you.")
        return
    
    log_entry = f"{user_email}|{feedback_text}\n"

    try :
    
        if not os.path.exists(file_name) :

            print ('File Not Found. Creating New File...')

            with open (file_name, 'w', encoding= 'utf-8') as file :

                file.write('Email|Feedback\n')

                file.write(log_entry)

        else :

            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(log_entry)
            
        # Success message
        print("-" * 45)
        print("✅ Success! Your feedback has been successfully received. We appreciate your time.")

    except Exception as e :

        print(f"❌ An error occurred while saving the feedback: {e}")

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

def get_user_favourites(email_to_check) :

    file_name = 'Favourite.txt'

    user_favourites = []

    if not os.path.exists(file_name) :

        with open (file_name, 'w', encoding= 'utf-8') as file :

            file.write('Email|Favourite Vehicles\n')

        return user_favourites
    
    with open (file_name, 'r', encoding= 'utf-8') as file :

        for line in file :

            if "Email|Favourite Vehicles" in line :
                continue

            fav_info = line.strip().split('|')

            if len(fav_info) > 1 :

                if fav_info[0].lower() == email_to_check.lower() :

                    user_favourites_raw = fav_info[1:]

                    user_favourites = [item.strip() for item in user_favourites_raw if item.strip()]

                    return user_favourites
                
    return user_favourites

def update_user_favourites(email, new_favourites) :
    
    file_name = 'Favourite.txt'

    lines = []

    found_and_updated = False

    if not os.path.exists(file_name):

        with open(file_name, 'w', encoding='utf-8') as file:
            file.write("Email|Favourite Vehicles\n")

    with open (file_name, 'r', encoding= 'utf-8') as file :

        lines = file.readlines()

    new_fav_str = '|'.join(new_favourites)
    new_line = f'{email}|{new_fav_str}\n'

    for i in range(len(lines)) :

        if i == 0 :
            continue

        line_email = lines[i].split('|')[0].strip().lower()

        if line_email == email.lower() :

            lines[i] = new_line
            found_and_updated = True

            break

    if not found_and_updated :

        lines.append(new_line)

    with open (file_name, 'w', encoding= 'utf-8') as file :

        file.writelines(lines)

    return True

def favourite_vehicles(email, vehicles_dict) :

    current_favourites = get_user_favourites(email)

    while True :
        print("⭐ Favourite Vehicles Options ⭐")
        print("1. Add Item to Favourites")
        print("2. Remove Item from Favourites")
        print("3. View Favourites")
        print("4. Clear All Favourites")
        print("5. Back to Main Menu")

        choice = input ("Enter your choice (1-5): ").strip()

        if choice == '5' or choice.capitalize() in Termination_Terms :

            print("⬅️ Returning to Main Menu.")
            break

        elif choice == '1' :

            print("📝 Adding Item to Favourites (Choose by name or number):")

            new_favourites = add_items_logic(current_favourites, vehicles_dict)

            if new_favourites != current_favourites :

                if update_user_favourites(email, new_favourites) :
                        
                    current_favourites = new_favourites
                    print("✅ Favourites list updated.")

        elif choice == '2' :

            if not current_favourites:
                print("⚠️ Your Favourites list is empty. Nothing to remove.")
                continue

            else :

                print("🗑️ Removing Item from Favourites:")

                print("Your Current Favourites:")
                for index, item in enumerate(current_favourites, start= 1) :

                    print (f'- {index}. {item}')

                new_favourites = remove_items_logic(current_favourites)

                if new_favourites != current_favourites :

                    if update_user_favourites(email, new_favourites) :

                        current_favourites = new_favourites

                        print("✅ Favourites list updated successfully.")

        elif choice == '3' :

            if not current_favourites :
                print("⚠️ Your Favourites list is empty.")

            else :
                print("✨ Your Favourite Vehicles ✨")

                for index, item in enumerate(current_favourites, start= 1) :

                    print (f'- {index}. {item}')

        elif choice == '4' :
            if current_favourites :
                confirm = input("Are you sure you want to clear ALL favourites? (Yes/No): ").strip().capitalize()
                if confirm in Consent_Terms :
                    if update_user_favourites(email, []) :
                        current_favourites = []
                        print("✅ All favourite items have been cleared.")
                    else :
                        print("❌ Failed to clear favourites.")
                else :
                    print("🚫 Clear operation cancelled.")
            else :
                print("⚠️ Favourites list is already empty.")
        else :
            print("⚠️ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    
    print("🚗 Motors Vehicle Ordering System 🏍️")
        
    email_logged_in = input ('Welcome To Motors. Please Write Your Email.\n').strip().lower()

    client = None

    while True :

        if check_user_data(email_logged_in) :

            client = email_logged_in

            break

        else :

            sign_up = input ('Your Email Not Found. Please Sign Up.\nDo You Want To Fill The Requirements\n').strip().capitalize()

            if sign_up in Consent_Terms :

                success, new_email = save_useres_data()

                if success :

                    email_logged_in = new_email

                    continue

            else :

                print ('👋 Thank You for visiting Motors.')

                break

    if client:

        user_name = get_user_name(client)

        while True :

            Action = input (f'Hello {user_name}, How Can I Help You?\n').strip().capitalize()

            if Action in Termination_Terms :

                print ('✅ Exiting...')

                break

            elif Action in ('Add', 'A') :

                addition(client)

            elif Action in ('Remove', 'R') :

                removal(client)

            elif Action in ('Clear', 'Cl') :

                clear(client)

            elif Action in ('View', 'V') :

                view_cart(client)

            elif Action in ('Total price', 'Total', 'T', 'Tp') :

                total_price(client, vehicles)

            elif Action in ('Price list', 'Pl') :

                price_list(vehicles)

            elif Action in ('Update user info', 'Ui', 'Up') :

                updated_name, updated_email = update_user_info(client) 
        
                if updated_name is not None:

                    user_name = updated_name 

                    client = updated_email

                    print(f"👋 Welcome back, {user_name}!")

            elif Action in ('Feedback', 'Fb') :
                
                send_feedback(client)

            elif Action in ('Contact us', 'Cu') :

                contact_us()

            elif Action in ('Favourite vehicles', 'Fav', 'Fv') :

                favourite_vehicles(client,vehicles)

            else :

                available_features()

