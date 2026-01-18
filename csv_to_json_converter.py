import uuid
import random
from datetime import datetime
import json

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

vehicles_data = {}

for types, category in vehicles.items():
    if types == "Cars":
        current_type = "Car"
    elif types == "Bikes":
        current_type = "Bike"

    for category_name, cars in category.items():
        if category_name:
            current_category = category_name

        for car_name, price in cars.items():
            vehicle_id = str(uuid.uuid4())
            vehicles_data[vehicle_id] = {
                "model": car_name,
                "type": current_type,
                "category": current_category,
                "year": random.randint(2020, 2026),
                "price": price,
                "quantity": random.randint(1, 5),
                "status": "available",
                "owner_type": "system",
                "owner_id": None,
                "created_at": datetime.now().isoformat()
            }

with open(r'data\vehicles.json', 'w', encoding='utf-8') as f:
    json.dump(vehicles_data, f, indent=4)
