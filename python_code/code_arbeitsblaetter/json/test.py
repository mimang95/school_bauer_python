import json

# json_datei_pfad = "./personen.json"

# with open(json_datei_pfad, 'r', encoding='UTF8') as datei:
#     personen_data = json.load(datei)

# print('Erster Name ' + personen_data[1]['Name'])
# print(personen_data)

# gesuchte_person = input("Geben Sie einen Namen ein: ")
# for person in personen_data:
#     if person['Name'] == gesuchte_person:
#         print(person)

# anzahl = len(personen_data)
# for i in range(anzahl):
#     for key in personen_data[i]:
#         print(key, ':', personen_data[i][key])

#print(personen_data)

json_datei_pfad = "./sensoren.json"

with open(json_datei_pfad, 'r') as file:
    data = json.load(file)

print(data)
for sensor_name in data:
    sensor_info = data[sensor_name]
    print(f"Sensor {sensor_info['Nummer']}: Temperatur {sensor_info['Temperatur']}°C")

def ermittle_defekte_sensoren():
    for sensor_name in data:
        sensor_info = data[sensor_name]
        if sensor_info['Temperatur'] <= 0 or sensor_info['Temperatur'] >= 60:
            print(f'Sensor {sensor_info} ist defekt')

ermittle_defekte_sensoren()

def ermittle_durchschnittswert():
    sum = 0
    count = 0
    for sensor_name in data:
        sensor_info = data[sensor_name]
        if sensor_info['Temperatur'] >= 0 and sensor_info['Temperatur'] <= 60:
            sum += sensor_info['Temperatur']
            count += 1
    return sum/count

print(ermittle_durchschnittswert())