import os

import string

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print (os.getcwd())

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

    return '\n'.join(output_lines)
                
if not os.path.exists('vehicles_data.txt') :

    with open ('vehicles_data.txt', 'w') as file :
        
        file.write(sort_names_alphabetically(vehicles))

else :

    print ('File\'s Already Exists.')


def check_user_data(email_to_check) :

    file_name = 'Users Data.txt'

    if not os.path.exists(file_name) :

        return False

    with open (file_name, 'r', encoding= 'utf-8') as file :

        for line in file :

            if "Name|Email|Address|Phone" in line:

                continue

            user_info = line.strip().split('|')

            if len(user_info) > 1 and  user_info[1].lower() == email_to_check.lower() :

                return True
            
    return False

def save_useres_data() :

    file_name = 'Users Data.txt'


    name = input ('Please Write Your Name\n').strip().capitalize()

    email = input (f'Please Write Your Email {name}\n').strip().lower()

    while '@gmail.com' not in email :

        print ('Invalid Email.')

        email = input (f'Please Write Your Email And Make Sure It Contains @gmail.com\n').strip().lower()

    address = input ('Please Write Your Address\n').strip()

    phone = input ('Please Write Your Phone\n').strip()

    user_data = f'{name}|{email}|{address}|{phone}\n'

    if check_user_data(email) :

        print ('\n🔴 Error: This Email Address Already Exists. Data Not Saved.')

        return
    
    if not os.path.exists(file_name) :

        print ('File Not Found. Creating New File...')

        with open (file_name, 'w', encoding= 'utf-8') as file :

            file.write('Name|Email|Address|Phone\n')

            file.write(user_data)

    else :

        with open (file_name, 'a', encoding= 'utf-8') as file :

            file.write(user_data)

    print (f'Thank You {name} To Visit World Motors, Your Data Saved Successfully.')

save_useres_data()

# user_info = {
        
#     'name' : 'Yasseen',
#     'E_mail' : 'User12345@gmail.com',
#     'Address' : 'Egypt,Alex',
#     'Phone' : '01212042272'
# }

# user_info2 = {
        
#     'name' : '',
#     'E_mail' : '',
#     'Address' : '',
#     'Phone' : ''
# }

# Cart = ["Kawasaki Ninja H2R", "Ferrari SF90 Stradale"]

# Old_Cart = Cart.copy()

# Available_features = ('List Of Prices', 'Update User Info', 'Feedback', 'Contact Us','Favourite', 'L', 'U', 'F', 'C', 'Fv')

# media = {
#      'FaceBook' : 'F.com',
#      'WhatsApp' : 'W.com',
#      'Instgram' : 'I.com',
#      'Telegram' : 'T.com',
#      'OUR Numbers' : "012\n011\n010"

# }

# favourite = []

# Agree = ('Yes', 'Ok', 'Yeah', 'Yup', 'Confirm', 'Y', 'O', 'c')

# rejection = ('No', 'Nope', 'N')

# updates = ('Add', 'Remove', 'Clear', 'Total Price', 'A', 'R', 'C', 'T')

# stop = 0

# first_round = True

# finish = ('Done', 'Finish', 'F', 'D')

# prices_list = (50000, 100000, 500000, 1000000)

# Guest = input ('Welcome To World Motors, Please Write Your Name Or Email.\n').strip().capitalize()

# while True :

#     count = 1

#     if Guest == user_info["E_mail"]:

#         choise1 = input (f'Hello {user_info["name"]}, How Can I Help You \nDo You Want To See Your Cart?\n' if first_round == True else 'What Do You Decide To Do?\n' ).strip().capitalize()

#     else :
            
#         if Guest not in user_info.values() :

#                 print (f'Hello {Guest}, My Pleasure To See You')

#                 ask_s = input ('Do You Want To Sign In?\n').strip().capitalize()

#                 while True :
                     
#                     if ask_s in Agree :
                                            
#                             info_e = input (f'Please Write Your Email {Guest}\n').strip()

#                             if '@gmail.com' not in info_e :
                                
#                                 reinfo_e = input (f'Please Write Your Email And Make Sure It Contains @gmail.com\n').strip().capitalize()

#                             info_a = input ('Please Write Your Address\n').strip()

#                             info_p = input ('Please Write Your Phone\n').strip()

#                             user_info2['name'] = Guest

#                             user_info2['E_mail'] = info_e if '@gmail.com' in info_e else reinfo_e

#                             user_info2['Address'] = info_a

#                             user_info2['Phone'] = info_p

#                             print ('That\'s Your Info.')

#                             for info2, info3 in user_info2.items() :
                                 
#                                 print (f'- Your {info2} Is {info3}')  

#                             print (f'Thank You {Guest} To Visit World Motors.')

#                             break                        

#                     elif ask_s in rejection :
                        
#                         print (f'Thank You {Guest} To Visit World Motors.')

#                         break
#                 break

#         elif Guest in user_info.values() :

#                 check = input  (f'Hello {user_info["name"]} \nWe Want To Check If You Are signed in.\nSo We Need You To Write Your Email To Know.\n').strip().capitalize()

#                 if check == user_info['E_mail'] :

#                     choise1 = input (f'Hello {user_info["name"]}, How Can I Help You \nDo You Want To See Your Cart?\n').strip().capitalize()

#                 else :

#                     sign = input (f'{Guest} You\'r Not Signed In Do You Want To sign In?\n').strip().capitalize()

#                     if sign in Agree :
                         
#                         if '@gmail.com' not in check :
                                
#                                 reinfo_e3 = input (f'Please Write Your Email And Make Sure It Contains @gmail.com\n').strip().capitalize()

#                         info_a3 = input ('Please Write Your Address\n').strip()

#                         info_p3 = input ('Please Write Your Phone\n').strip()

#                         user_info2['name'] = Guest

#                         user_info2['E_mail'] = check if '@gmail.com' in check else reinfo_e3

#                         user_info2['Address'] = info_a3

#                         user_info2['Phone'] = info_p3

#                         print ('That\'s Your Info.')

#                         for info_2, info_3 in user_info2.items() :
                                 
#                             print (f'- Your {info_2} Is {info_3}')  

#                         print (f'Thank You {Guest} To Visit World Motors.')

#                     elif sign in rejection :
                         
#                         print (f'Thank You {Guest} To Visit World Motors.')

#                     break
               
#     if choise1 in Agree  :

#         print(f'Your Cart Is Empty.'if len (Cart) == stop else 'That\'s Your Cart.')

#         count = 1

#         for vehicles2 in Cart :
            
#             print (f'- {count} Is {vehicles2}')

#             count += 1

#         print ('-' * 20 if len (Cart) == stop else 'Do You Want To Confirm? \nAfter Confirmation The Vehicles Will Deliver To Your Address.')

#         print ('Available Updates')

#         count = 1

#         for update in updates[:4] :
                
#                 print (f'- {count} {update}')

#                 count += 1

#         show = input ('Or You Can choose From Available Updates.\n').strip().capitalize()

#         if show in Agree :
                
#             print ('The Progress Is Finished.\nThe Vehicles Will Deliver To Your Addres.')

#             break

#         while True :

#             if show == updates[0] or show ==updates[4] :
                    
#                 while True :
                        
#                     ask = input ('Please Write The Vehicle That You Want To Add.\n').strip()

#                     if ask in str(finish).lower() :
                        
#                         print ('The Progress Is Finished')

#                         break

#                     print  ('-' * 20)

#                     found_vehicle = None

#                     for key, value in vehicles.items() :

#                         for key2, value2 in value.items() :

#                             for key3, value3 in value2.items() :
                                    
#                                 if ask == key3 :
                                        
#                                     found_vehicle =key3

#                             if found_vehicle : break

#                         if found_vehicle : break

#                     if found_vehicle :

#                         if found_vehicle in Cart :
                                
#                             check2 = input (f'{found_vehicle} Is Aleardy In The List. \nDo You Want To Add It Again\n').strip().capitalize()

#                             if check2 in Agree :
                                
#                                 Cart.append(found_vehicle)

#                                 print('That\'s Your Cart.')

#                                 count = 1

#                                 for vehicles_n in Cart :
                                        
#                                     print (f'- {count} Is {vehicles_n}')

#                                     count += 1

#                             elif check2 in rejection :
                                
#                                 print (f'{found_vehicle} Didn\'t Add To Cart.')
#                         else :
                                
#                             Cart.append(found_vehicle)

#                             print('That\'s Your Cart.')

#                             count = 1

#                             for vehicles_n in Cart :
                                    
#                                 print (f'- {count} Is {vehicles_n}')

#                                 count += 1

#                             count = 1

#                             print ('That\'s Your Old Cart')

#                             for vehicles2 in Old_Cart :
                                            
#                                 print(f'- {count} Is {vehicles2}')

#                                 count += 1

#                     else :

#                         print (f'- {ask} Is Not In The Available Vehicles. \nPlease Choose From Available vehicles.')

#                         count = 1

#                         print (f'Available Vehicles.')

#                         category_l = []

#                         count = 1

#                         for one1, two2 in vehicles.items() :

#                             for three3, four4 in two2.items() :

#                                 for five5, six6 in four4.items() :
                                     
#                                     category_l.append((five5,one1))

#                         category_n = ''

#                         for cars_t, types in category_l :
                                         
#                             if types != category_n :
                                              
#                                 print (f'{types}')

#                                 category_n = types
                                     
#                             print (f'- {str(count).zfill(2)} {cars_t}')

#                             count += 1

#             elif show == updates[1] or show == updates[5] :
                    
#                     while True :
                        
#                         removing = input ('Please Choose The Vehicle That You Want To Remove.\n').strip()

#                         if removing in str (finish).lower() :

#                             print ('The Progress Is Finished.')

#                             break

#                         if removing in Cart :
                            
#                             Cart.remove(removing)

#                             print('-' * 20 if len (Cart) == stop else 'Done\nThat\'s Your Cart.')

#                             count = 1

#                             for vehicles2 in Cart :
                                                    
#                                 print (f'- {count} Is {vehicles2}')

#                                 count += 1

#                             print ('That\'s The Old cart.')

#                             count = 1

#                             for vehicles3 in Old_Cart :
                                                        
#                                     print(f'- {count} Is {vehicles3}')

#                                     count += 1

#                         elif removing not in Cart :
                            
#                             print (f'{removing} Is Not In The Cart.')

#                             print('That\'s Your Cart.')
                            
#                             count = 1

#                             for vehicles2 in Cart :
                                                    
#                                 print (f'- {count} Is {vehicles2}')

#                                 count += 1

#                         print ('-' * 20)

#                         if len(Cart) == stop :
                            
#                             print ('Your Cart Is Empty')

#                             break

#             elif show == updates[2] or show == updates[6] :
                
#                 while True :
                    
#                     Cart.clear()

#                     if len(Cart) == stop :
                        
#                         print ('Your Cart In Empty')

#                         print ('that\'s The Old Cart.')

#                         count = 1

#                     for vehicles4 in Old_Cart :
                                                
#                         print(f'- {count} Is {vehicles4}')

#                         count += 1
                    
#                     break

#                 break

#             elif show == updates[3] or show == updates[7] :
                 
#                 print('-' * 20 if len (Cart) == stop else 'Done\nThat\'s Your Cart.')

#                 count = 1

#                 for vehicles2 in Cart :
                                        
#                     print (f'- {count} Is {vehicles2}')

#                     count += 1
                
#                 if len (Old_Cart) != len (Cart) :

#                     print ('That\'s The Old cart.')

#                     count = 1

#                     for vehicles3 in Old_Cart :
                                                
#                             print(f'- {count} Is {vehicles3}')

#                             count += 1

#                 Total_Price = 0
                
#                 for item_in_cart in Cart :
                     
#                     found_price = 0
                    
#                     for catrgory, types_dict in vehicles.items() :
                        
#                         for type_name, cars_dict in types_dict.items() :
                             
#                              if item_in_cart in cars_dict :
                                  
#                                 found_price = cars_dict[item_in_cart]
                                  
#                                 Total_Price += found_price
                                
#                                 print (f'- {item_in_cart} Price Is ${found_price:,}')

#                                 break
                             
#                         if found_price : break
                    
#                     if found_price == 0 :
                         
#                          print (f'Warning: Price For {item_in_cart} Not Found.')

#                 print (f'Total Price Is ${Total_Price:,}')

#                 break
                
#     elif choise1 in rejection :

#                 print(f'Ok {user_info["name"]}, That\'s Things That I Can Help You with.')

#                 count = 1

#                 for featers in Available_features[:4] :
                    
#                     print (f'- {count} {featers}')
                    
#                     count += 1

#                 first_round = False
                
#     elif choise1 in Available_features :
         
#         while True :
              
#             if choise1 == Available_features[0] or choise1 == Available_features[5] :
                
#                 print (f'Prices Under ${prices_list[0]}')

#                 count = 1

#                 sorting = []

#                 for category_cars, cars_type in vehicles.items() :
                    
#                     for cars_shape, final_value in cars_type.items() :
                            
#                             for cars_name, price_value in final_value.items():
                                
#                                 if price_value < prices_list[0] :

#                                     sorting.append((price_value, cars_name, category_cars))

#                 sorting.sort(reverse=True)

#                 current_category = ''

#                 for sort_prices, name, categorys  in sorting :

#                     if categorys != current_category :
                         
#                         print (f'- {categorys}')
                        
#                         current_category = categorys

#                     print (f'- {count} {name} Price Is ${sort_prices}')

#                     count += 1

#                 print (f'Prices Under ${prices_list[1]}')

#                 count = 1
                
#                 sorting_two = []

#                 for dict_cars, dict_type in vehicles.items() :
                    
#                     for shape_cars, last_value in dict_type.items() :
                            
#                             for name_cars, cost in last_value.items():
                                 
#                                  if prices_list[0] < cost < prices_list[1] :
                                      
#                                       sorting_two.append((cost, name_cars, dict_cars))

#                 sorting_two.sort(reverse=True)

#                 new_category = ''

#                 for sort, name_two, categorys2 in sorting_two :
                     
#                      if categorys2 != new_category :
                          
#                         print (f'- {categorys2}')

#                         new_category = categorys2
                     
#                      print (f'- {count} {name_two} Price Is ${sort}')

#                      count += 1

#                 print (f'Prices Under ${prices_list[2]}')

#                 count = 1
                
#                 sorting_three = []

#                 for one, two in vehicles.items() :
                    
#                     for three, four in two.items() :
                            
#                             for five, six in four.items():
                                 
#                                  if prices_list[1] < six < prices_list[2] :
                                      
#                                       sorting_three.append((six, five, one))

#                 sorting_three.sort(reverse=True)

#                 just_category = ''

#                 for sorted1, name_three, categorys3 in sorting_three :

#                     if categorys3 != just_category :
                         
#                         print (f'{categorys3}')
                    
#                         just_category = categorys3
                     
#                     print (f'- {count} {name_three} Price Is ${sorted1}')

#                     count += 1

#                 print (f'Prices Under ${prices_list[3]}')

#                 count = 1
                
#                 sorting_four = []

#                 for seven, eight in vehicles.items() :
                    
#                     for nine, ten in eight.items() :
                            
#                             for eleven, twelve in ten.items():
                                 
#                                  if prices_list[2] < twelve < prices_list[3] :
                                      
#                                       sorting_four.append((twelve, eleven, seven))

#                 sorting_four.sort(reverse=True)

#                 last_category = ''

#                 for sorted2, name_four, categorys4 in sorting_four :
                     
#                     if categorys4 != last_category :
                         
#                         print (f'{categorys4}')

#                         last_category = categorys4
                     
#                     print (f'- {count} {name_four} Price Is ${sorted2}')

#                     count += 1

#                 break
            
#             elif choise1 == Available_features[1] or choise1 == Available_features[6] :

#                 info_n = input ('Please Write Your Name\n').strip().capitalize()
                 
#                 info_e2 = input (f'Please Write Your Email {info_n}\n').strip().capitalize()

#                 if '@gmail.com' not in info_e2 :
                    
#                     reinfo_e2 = input (f'Please Write Your Email And Make Sure It Contains @gmail.com\n').strip().capitalize()

#                 info_a2 = input ('Please Write Your Address\n').strip()

#                 info_p2 = input ('Please Write Your Phone\n').strip()

#                 user_info['name'] = info_n

#                 user_info['E_mail'] = info_e2 if '@gmail.com' in info_e2 else reinfo_e2

#                 user_info['Address'] = info_a2

#                 user_info['Phone'] = info_p2

#                 print ('That\'s Your Info.')

#                 for info4, info5 in user_info.items() :
                        
#                     print (f'- Your {info4} Is {info5}')  

#                 print (f'Thank You {info_n} To Visit World Motors.')

#                 break

#             elif choise1 == Available_features[2] or choise1 == Available_features[7] :
                 
#                 feed_back = input ('Please Write Your FeedBack Here\n').strip().title()

#                 if feed_back :
                      
#                     print ('Thanks To Your FeedBack.\nWe\'ll Do Our Best For You.')

#                 break

#             elif choise1 == Available_features[3] or choise1 == Available_features[8] :

#                 print ('- OUR Media And Numbers')

#                 print ('-' * 20)
                 
#                 for m_key, m_value in media.items() :
                     
#                     print (f'- {m_key} \n{m_value}')

#                 break

#             elif choise1 == Available_features[4] or choise1 == Available_features[9] :

#                 stop = 0
                 
#                 if len (favourite) == stop :
                     
#                     print ('You Don\'t Have Any Favourite vehicle')

#                     local_first_input = True

#                     category_2 = []

#                     count = 1

#                     import string

#                     current_row = []

#                     cars_list = []

#                     bikes_list = []
                    
#                     if first_round == True :

#                         for one11, two22 in vehicles.items() :

#                             for three33, four44 in two22.items() :

#                                 for five55, six66 in four44.items() :
                                        
#                                     if one11 == 'Cars' :
                                        
#                                         cars_list.append((five55, one11))

#                                     elif one11 == 'Bikes' :
                                        
#                                         bikes_list.append((five55, one11))

#                                 category_2 = cars_list + bikes_list    

#                         for letter in string.ascii_uppercase :
                                
#                             current_row.append(letter)

#                         for letters in current_row :

#                             category_n2 = ''

#                             print (f'-{letters}-')

#                             print ('-' * 30)
                        
#                             found_any = False

#                             for cars_t2, types2 in category_2 :

#                                 if cars_t2[0] == letters : 
                                                        
#                                     if types2 != category_n2 :
                                                        
#                                         print (f'{types2}')

#                                         category_n2 = types2

#                                     print (f'- {count} {cars_t2}')

#                                     count += 1
                                    
#                                     found_any = True

#                             if not found_any :
                                        
#                                 print (f'There Is No Vehicle Starts With {letters}')

#                                 print ('-' * 30)

#                         first_round = False

#                         all_car_names = []

#                         for car_name3, car_type5 in category_2 :

#                             all_car_names.append(car_name3)

#                     while True :
                        
#                         add = input ('Please choose The Vehicle You Want To Add To Your Favourite\n' if local_first_input == True else 'Do You Want To Add More?\nOr End The Progress?\n').strip()

                        
#                         if add in str(finish).lower() :
                            
#                             print ('The Progress Is Finished')

#                             break

#                         elif add in all_car_names :
                            
#                             favourite.append(add)

#                             print ('That\'s Your Favourite Vehicles')

#                             count = 1

#                             for cars01 in favourite :
                                
#                                 print (f'- {count} {cars01}')

#                                 count += 1

#                             local_first_input = False

#                         elif add not in all_car_names :
                            
#                             print ('You Can Choose From Available Vehicles')


#                     break

#                 else :
                     
#                     print ('That\'s Your Favourite Vehicles')

#                     count = 1

#                     for cars0 in favourite :
                          
#                         print (f'- {count} {cars0}')

#                         count += 1

#                     break

#         break
    
#     else :

#             print (f'You Just Can Use These.')

#             count = 1

#             for reactions in Agree[:5] :
                    
#                     print (f'- {count} {reactions}')

#                     count += 1

#             count = 1

#             print ('Or')

#             for reactions in rejection[:2] :
                    
#                     print (f'- {count} {reactions} ')

#                     count += 1

#             count = 1

#             print ('Or')

#             for featers in Available_features[:4] :
                
#                 print (f'- {count} {featers}')
                
#                 count += 1

#             first_round = False