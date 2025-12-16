import os

import user_cart_logic.user_cart_logic as ucl

import file_storage.file_storage as fs

import vehicle_processing.vehicle_processing  as vp

import user_interface.user_interface as ui

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print (os.getcwd())

Available_features = ('Add', 'Remove', 'Clear', 'View', 'Total Price', 'Price List', 'Update User Info', 'Feedback', 'Contact Us', 'Favourite Vehicles')

Consent_Terms = ('Yes', 'Ok', 'Yeah', 'Yup', 'Confirm', 'Y', 'O')

Termination_Terms = ('No', 'Nope', 'Cancel','Done', 'N', 'C', 'D' )

if __name__ == "__main__":
    
    print("\n🚗 Motors Vehicle Ordering System 🏍️")
        
    email_logged_in = input ('\nWelcome To Motors. Please Write Your Email.\n').strip().lower()

    client = None

    while True :

        if ui.check_user_data(email_logged_in) :

            client = email_logged_in

            break

        else :

            sign_up = input ('\nYour Email Not Found. Please Sign Up.\nDo You Want To Fill The Requirements\n').strip().capitalize()

            if sign_up in Consent_Terms :

                success, new_email = fs.save_useres_data()

                if success :

                    email_logged_in = new_email

                    continue

            else :

                print ('\n👋 Thank You for visiting Motors.')

                break

    if client:

        user_name = ui.get_user_name(client)

        while True :

            Action = input (f'\nHello {user_name}, How Can I Help You?\n').strip().capitalize()

            if Action in Termination_Terms :

                print ('\n✅ Exiting...')

                break

            elif Action in ('Add', 'A') :

                ucl.addition(client)

            elif Action in ('Remove', 'R') :

                ucl.removal(client, Termination_Terms)

            elif Action in ('Clear', 'Cl') :

                ucl.clear(client)

            elif Action in ('View', 'V') :

                ucl.view_cart(client)

            elif Action in ('Total price', 'Total', 'T', 'Tp') :

                vp.total_price(client, vp.vehicles)

            elif Action in ('Price list', 'Pl') :

                vp.price_list(vp.vehicles)

            elif Action in ('Update user info', 'Ui', 'Up') :

                updated_name, updated_email = fs.update_user_info(client, Termination_Terms)
        
                if updated_name is not None:

                    user_name = updated_name 

                    client = updated_email

                    print(f"👋 Welcome back, {user_name}!")

            elif Action in ('Feedback', 'Fb') :
                
                fs.send_feedback(client)

            elif Action in ('Contact us', 'Cu') :

                ui.contact_us()

            elif Action in ('Favourite vehicles', 'Fav', 'Fv') :

                vp.favourite_vehicles(client, vp.vehicles, Termination_Terms, Consent_Terms)

            else :

                ui.show_available_features(Available_features)
