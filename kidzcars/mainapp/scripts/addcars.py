import joblib

car_list = [
    "Mercedes-Benz 190 E 2.5 - 16 Evolution II '91",
    "Mercedes-Benz 300 SL Coupe '54",
    "Mercedes-Benz A 160 Avantgarde '98",
    "Mercedes-Benz Patent Motor Wagen 1886",
    "Mercedes-Benz CL 600 '00",
    "Mercedes-Benz CLK 55 AMG '00",
    "Mercedes-Benz Daimler Motor Carriage 1886",
    "Mercedes-Benz E 55 AMG '02",
    "Mercedes-Benz SL 500 (R129) '98",
    "Mercedes-Benz SL 500 (R230) '02",
    "Mercedes-Benz SL 600 (R129) '98",
    "Mercedes-Benz SL 600 (R230) '04",
    "Mercedes-Benz SL 55 AMG (R230) '02",
    "Mercedes-Benz SL 65 AMG (R230) '04",
    "Mercedes-Benz SLK 230 Kompressor '98",
    "Mercedes-Benz SLR McLaren '03"
]


cars_ready = []
for car in car_list:
    car_parts = car.split()
    brand = car_parts[0]
    model = car_parts[1]
    year = "20" + car_parts[-1].strip("'") if int(car_parts[-1].strip("'")) < 30 else "19" + car_parts[-1].strip("'")
    if len(car_parts) > 3:
        generation = " ".join(car_parts[2:-1])
    else:
        generation = ""
    print("Brand:", brand)
    print("Model:", model)
    print("Generation:", generation)
    print("Year:", year)
    print()

    cars_ready.append([brand, model, generation, year])

joblib.dump(cars_ready, 'cars_ready.joblib')