import vehicle_processing.vehicle_processing  as vp

def add_items_logic(current_cart, vehicles_dict) :

    updated_cart = list (current_cart)

    count = 0

    print("\n💡 Displaying vehicles list to assist you...")

    ordered_vehicles = vp.show_vehicles(vehicles_dict)

    cars_list = {car_name.lower() for car_name in ordered_vehicles}

    while True :

        item_to_add = input ('\nPlease Write The Item That You Want To Add.\n').strip()

        count += 1

        if item_to_add.capitalize() in ('Done', 'Finish', 'D', 'F') :
            if count == 1 :

                print ('\n🚫 No new items were added. Cart remains unchanged.')
            else :

                print ('\n✅ Finished Adding items. Cart updated.')
            break

        try :

            item_index = int(item_to_add)

            if 1 <= item_index <= len(ordered_vehicles) :

                chosen_item = ordered_vehicles[item_index - 1]

                if chosen_item.lower() in cars_list:

                    updated_cart.append(chosen_item)

                    print (f'\n✅ successfully Added BY Number. "{chosen_item.strip()}"')

                    print ("\n🛒 Cart after Addition:")

                    for index, item in enumerate(updated_cart, start= 1) :

                        print (f'- {index} {item}')
                    continue

                else: 
                    print(f'\n⚠️ Internal Error: Item "{chosen_item}" not found in available list.')

            else :

                print ('\n⚠️ The number you entered is out of range. Please enter a valid number or name.')

                continue

        except ValueError :

            if item_to_add.lower() in cars_list :

                updated_cart.append(item_to_add)
                print (f'\n✅ successfully Added by Name. "{item_to_add.strip()}"')

                print ("\n🛒 Cart after Addition:")

                for index, item in enumerate(updated_cart, start= 1) :

                    print (f'- {index} {item}')

            else :

                print ('\n⚠️ The item you entered is not available. Please choose from the available vehicles.')

    return updated_cart

def addition(email) :

    user_cart = vp.get_user_cart(email)

    view_cart(email)

    final_cart_items = add_items_logic(user_cart, vp.vehicles)

    if final_cart_items != user_cart :

        vp.update_user_cart(email, final_cart_items)

def remove_items_logic(current_cart, Termination_Terms) :

    if not current_cart :

        print ('\n🛒 Your Cart Is Empty')

        return current_cart
    
    temp_cart = list(current_cart)

    count = 0

    items_removed_successfully = False

    while True :

        item_index_to_remove = input ('\nEnter The Number OF The Item You Want To Remove: ').strip()

        count += 1

        if item_index_to_remove.capitalize() in Termination_Terms :

            if count == 1 :

                print ('\n🚫 No new items were removed. Cart remains unchanged.')

                return temp_cart

            if items_removed_successfully :

                print('\n✅ Finished removing items. Cart updated.')

                return temp_cart
            
            else :

                print('\n❌ Removal operation cancelled. No items were removed.')    

                return temp_cart
            
        try:

            index_to_remove = int(item_index_to_remove)

            if 1 <= index_to_remove <= len(temp_cart) :

                items_removed_successfully = True

                removed_item = temp_cart.pop(index_to_remove - 1)

                print (f'\n🗑️ Successfully removed "{removed_item.strip()}".')

                print ("\n🛒 Cart after removal:")

                for index, item in enumerate(temp_cart, start= 1) : 

                    print (f'- {index} {item}')

                if not temp_cart :

                    print ("\n✅ Last item removed. Cart is now empty.")

                    return temp_cart
                
            else :

                print ('\n⚠️ The number you entered is out of range.')

        except ValueError:

            print ('\n⚠️ Invalid input. Please enter the item number.')

def removal(email, Termination_Terms) :

    user_cart = vp.get_user_cart(email)

    if user_cart:

        view_cart(email)

    final_cart_items = remove_items_logic(user_cart, Termination_Terms)

    if final_cart_items != user_cart :

        vp.update_user_cart(email, final_cart_items)

def clear(email) :

    user_cart = vp.get_user_cart(email)

    view_cart(email)

    if user_cart :

        vp.update_user_cart(email, [])

        print ('\n✅ Cart data successfully reset and saved.')

def view_cart(email_to_check) :

    user_cart = vp.get_user_cart(email_to_check) 

    if not user_cart:

        print('\n🛒 Your Cart Is Empty')

    else :

        print ('\n🛒 Your Current Cart Items:')

        for index, items in enumerate(user_cart, start=1) :

            print (f'- {index} {items.strip()}')
