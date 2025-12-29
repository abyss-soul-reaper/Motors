"""
MOTORS: Vehicle Management System (VMS) Main Program.

Handles application startup, user authentication flow, 
and control structure for interacting with core packages.
"""

import os

import user_cart_logic.user_cart_logic as ucl

import file_storage.file_storage as fs

import vehicle_processing.vehicle_processing  as vp

import user_interface.user_interface as ui

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print (os.getcwd())

AVAILABLE_FEATURES = (
'Add', 'Remove', 'Clear', 'View', 'Total Price',
'Price List', 'Update User Info', 'Feedback', 'Contact Us', 'Favourite Vehicles'
    )

CONSENT_TERMS = ('Yes', 'Ok', 'Yeah', 'Yup', 'Confirm', 'Y', 'O')

TERMINATION_TERMS = ('No', 'Nope', 'Cancel','Done', 'N', 'C', 'D' )

if __name__ == "__main__":

    print("\n🚗 Motors Vehicle Ordering System 🏍️")

    email_logged_in = input ('\nWelcome To Motors. Please Write Your Email.\n').strip().lower()

    client = None

    while True :

        if ui.check_user_data(email_logged_in) :

            client = email_logged_in

            break

        sign_up = input (
            '\nYour Email Not Found. Please Sign Up.\nDo You Want To Fill The Requirements\n'
            ).strip().capitalize()

        if sign_up in CONSENT_TERMS :

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

            if Action in TERMINATION_TERMS :

                print ('\n✅ Exiting...')

                break

            if Action in ('Add', 'A') :

                ucl.addition(client)

            if Action in ('Remove', 'R') :

                ucl.removal(client, TERMINATION_TERMS)

            if Action in ('Clear', 'Cl') :

                ucl.clear(client)

            if Action in ('View', 'V') :

                ucl.view_cart(client)

            if Action in ('Total price', 'Total', 'T', 'Tp') :

                vp.total_price(client, vp.vehicles)

            if Action in ('Price list', 'Pl') :

                vp.price_list(vp.vehicles)

            if Action in ('Update user info', 'Ui', 'Up') :

                updated_name, updated_email = fs.update_user_info(client, TERMINATION_TERMS)

                if updated_name is not None:

                    user_name = updated_name

                    client = updated_email

                    print(f"👋 Welcome back, {user_name}!")

            if Action in ('Feedback', 'Fb') :

                fs.send_feedback(client)

            if Action in ('Contact us', 'Cu') :

                ui.contact_us()

            if Action in ('Favourite vehicles', 'Fav', 'Fv') :

                vp.favourite_vehicles(client, vp.vehicles, TERMINATION_TERMS, CONSENT_TERMS)

            else :

                ui.show_available_features(AVAILABLE_FEATURES)
