import os

import string

from file_storage.file_storage import *

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

    file_name = 'data_files/vehicles_data.txt'

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

def show_vehicles(vehicles_dict) :
    
    all_vehicles_list = []

    for category, types in vehicles_dict.items() :
        for type_name, cars in types.items() :
            for car_name, price in cars.items() :

                all_vehicles_list.append((price, category, type_name, car_name))

    all_vehicles_list.sort()

    count = 1
    current_type = ''
    
    print('\n', "=" * 50)
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

def get_price_map(vehicles_dict) :

    price_map = {}

    for category, types in vehicles_dict.items() :

        for type_name, cars in types.items() :

            for car_name, price in cars.items() :

                price_map[car_name.lower()] = price

    return price_map

def calculate_total_price(user_cart, vehicles_dict) :

    if not user_cart :
        print("\n🛒 Your cart is empty. Total Price: 0$")
        return 0
    
    print("\n🧾 Generating Cart Summary and Total Price...")
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

            print(f"\n| ⚠️ Item not found: {item:<25} | UNAVAILABLE |")
            
    print('\n',"-" * 40)
    print(f"| Total Items: {item_count:<25} | {total_price:10,}$ |")
    print("-" * 40)
    
    return total_price

def total_price(email,vehicles_dict) :

    user_cart = get_user_cart(email)

    if not user_cart :

        print("\n🛒 Your cart is empty. No total to calculate.")
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

            print ('\n', '=' * 30)
            print (f'💸 Vehicles Between {current_min_price:,}$ and {max_price:,}$')
            print ('=' * 30)
            
            count = 1

            for price, car_name, category in vehicles_in_range :

                print('-' * 30)
                print (f'- {str(count).zfill(2)}. {car_name} ({category}) Price: {price:,}$')

                count += 1

        current_min_price = max_price

    if remaining_vehicles :

        print ('\n','=' * 50)
        print (f'👑 Exotic Vehicles (Over {price_limits[-1]:,}$):')
        print ('=' * 50)

        count = 1
        for price, car_name, category in remaining_vehicles:

            print (f'- {count}. {car_name} ({category}) Price: {price:,}$')
            count += 1

def favourite_vehicles(email, vehicles_dict, Termination_Terms, Consent_Terms) :

    current_favourites = get_user_favourites(email)

    while True :
        print("\n⭐ Favourite Vehicles Options ⭐")
        print("\n1. Add Item to Favourites")
        print("\n2. Remove Item from Favourites")
        print("\n3. View Favourites")
        print("\n4. Clear All Favourites")
        print("\n5. Back to Main Menu")

        choice = input ("\nEnter your choice (1-5): ").strip()

        if choice == '5' or choice.capitalize() in Termination_Terms :

            print("\n⬅️ Returning to Main Menu.")
            break

        elif choice == '1' :

            from user_cart_logic.user_cart_logic import add_items_logic

            print("\n📝 Adding Item to Favourites (Choose by name or number):")

            new_favourites = add_items_logic(current_favourites, vehicles_dict)

            if new_favourites != current_favourites :

                if update_user_favourites(email, new_favourites) :
                        
                    current_favourites = new_favourites
                    print("\n✅ Favourites list updated.")

        elif choice == '2' :

            if not current_favourites:
                print("\n⚠️ Your Favourites list is empty. Nothing to remove.")
                continue

            else :

                from user_cart_logic.user_cart_logic import remove_items_logic

                print("\n🗑️ Removing Item from Favourites:")

                print("\nYour Current Favourites:")
                for index, item in enumerate(current_favourites, start= 1) :

                    print (f'- {index}. {item}')

                new_favourites = remove_items_logic(current_favourites, Termination_Terms)

                if new_favourites != current_favourites :

                    if update_user_favourites(email, new_favourites) :

                        current_favourites = new_favourites

                        print("\n✅ Favourites list updated successfully.")

        elif choice == '3' :

            if not current_favourites :
                print("\n⚠️ Your Favourites list is empty.")

            else :
                print("\n✨ Your Favourite Vehicles ✨")

                for index, item in enumerate(current_favourites, start= 1) :

                    print (f'- {index}. {item}')

        elif choice == '4' :
            if current_favourites :
                confirm = input("\nAre you sure you want to clear ALL favourites? (Yes/No): ").strip().capitalize()
                if confirm in Consent_Terms :
                    if update_user_favourites(email, []) :
                        current_favourites = []
                        print("\n✅ All favourite items have been cleared.")
                    else :
                        print("\n❌ Failed to clear favourites.")
                else :
                    print("\n🚫 Clear operation cancelled.")
            else :
                print("\n⚠️ Favourites list is already empty.")
        else :
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 5.")
