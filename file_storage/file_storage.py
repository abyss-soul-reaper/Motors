import os

import datetime

from user_interface.user_interface import *

def save_useres_data() :

    file_name = 'data_files/User Data.txt'

    # --- Name ---
    name = input ('\nPlease Write Your Name.\n').strip().capitalize()

    # --- Email ---
    email = input (f'\nPlease Write Your Email {name}.\n').strip().lower()

    while '@gmail.com' not in email :

        print ('\nInvalid Email.')

        email = input ('\nPlease Write Your Email And Make Sure It Contains @gmail.com\n').strip().lower()

    # --- Password ---
    password = input ('\nPlease Write Your Password.').strip().lower()

    # --- Address ---
    address = input ('\nPlease Write Your Address.\n').strip().title()

    # --- Phone ---
    phone = input ('\nPlease Write Your Phone.\n').strip()

    user_data = f'{name}|{email}|{password}|{address}|{phone}\n'

    if check_user_data(email) :

        print ('\n🔴 Error: This Email Address Already Exists. Data Not Saved.')

        return False, None
    
    if not os.path.exists(file_name) :

        print ('\nFile Not Found. Creating New File...')

        with open (file_name, 'w', encoding= 'utf-8') as file :

            file.write('Name|Email|Password|Address|Phone\n')

            file.write(user_data)

    else :

        with open (file_name, 'a', encoding= 'utf-8') as file :

            file.write(user_data)

    print(f"\n✅ User {name} registered successfully!")

    return True, email
     
def ensure_cart_file_exists() :

    file_name = 'data_files/Cart Data.txt'

    if not os.path.exists(file_name) :

        with open (file_name, 'w', encoding= 'utf-8') as file :

            file.write('Email|Cart Items\n')

def get_user_cart(email_to_check) :

    ensure_cart_file_exists()

    file_name = 'data_files/Cart Data.txt'

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

    file_name = 'data_files/Cart Data.txt'

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

def update_user_info(target_email, Termination_Terms) :    

    file_name = 'data_files/User Data.txt'
    lines = []
    found_user = False

    try :

        with open (file_name, 'r', encoding= 'utf-8') as file :

            lines = file.readlines()
    except FileNotFoundError :

        print(f"\n❌ Error: User data file not found: {file_name}")
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

        results = get_new_info(current_data, Termination_Terms)

        if results[0] is None :
            return None, target_email
        
        new_name, new_email, new_password, new_Address, new_phone = results

        updated_line = f'{new_name}|{new_email}|{new_password}|{new_Address}|{new_phone}\n'

        lines[i] = updated_line

        found_user = True
        
        break
    
    if not found_user :

        print(f"\n❌ User with email '{target_email}' not found.")
        return None, target_email
    
    try :

        with open (file_name, 'w', encoding= 'utf-8') as file :

            file.writelines(lines)

            print('\n',"=" * 50)
            print(f"✅ Success! User information for {new_email} has been updated and saved.")
            print("=" * 50)

            if new_email != target_email :

                print(f"\n❗ Your new email is: {new_email}. Please use it for future logins.")
    except Exception as e :

        print(f"\n❌ An error occurred while writing to the file: {e}")
    
        return None
    
    return new_name, new_email

def send_feedback(user_email) :

    file_name = 'data_files/Feedback.txt'

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print("\n💬 Feedback and Suggestions Center 💬")
    print("-" * 45)

    feedback_text = input("\nPlease write your feedback/suggestions (or leave blank to cancel):\n> ").strip()

    if not feedback_text :

        print("\n🚫 No feedback submitted. Thank you.")
        return
    
    log_entry = f"{timestamp}|{user_email}|{feedback_text}\n"

    try :
    
        if not os.path.exists(file_name) :

            print ('\nFile Not Found. Creating New File...')

            with open (file_name, 'w', encoding= 'utf-8') as file :

                file.write('Time|Email|Feedback\n')

                file.write(log_entry)

        else :

            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(log_entry)
            
        # Success message
        print("-" * 45)
        print("✅ Success! Your feedback has been successfully received. We appreciate your time.")

    except Exception as e :

        print(f"\n❌ An error occurred while saving the feedback: {e}")

def update_user_favourites(email, new_favourites) :
    
    file_name = 'data_files/Favourite.txt'

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

def get_user_favourites(email_to_check) :

    file_name = 'data_files/Favourite.txt'

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
