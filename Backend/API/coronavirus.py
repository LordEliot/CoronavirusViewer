# encoding: utf-8
import requests

request = requests.get('https://www.datos.gov.co/resource/gt2j-8ykr.json')
response = request.json()

print("Proyecto Covid-19: Colombia")
print("------------------------------------------")
print("Nacional:")
print("")

counter_recovered = 0
counter_death = 0

for case in response:
    if case["atenci_n"] == "Recuperado":
        counter_recovered += 1
    if case["atenci_n"] == "Fallecido":
        counter_death += 1

print("Casos positivos: " + str(len(response)))
print("Casos recuperados: " + str(counter_recovered))
print("Muertes: " + str(counter_death))

print("------------------------------------------")
print("Tolima:")
print("")

counter = 0
counter_recovered = 0
counter_death = 0

for case in response:
    if case["departamento"] == "Tolima":
        counter += 1
    if case["departamento"] == "Tolima" and case["atenci_n"] == "Recuperado":
        counter_recovered += 1
    if case["departamento"] == "Tolima" and case["atenci_n"] == "Fallecido":
        counter_death += 1

print("Casos positivos: " + str(counter))
print("Casos recuperados: " + str(counter_recovered))
print("Muertes: " + str(counter_death))

print("------------------------------------------")
print("Ibague:")
print("")

counter = 0
counter_recovered = 0
counter_death = 0

for case in response:
    if case["ciudad_de_ubicaci_n"] == u"Ibagué":
        counter += 1
    if case["atenci_n"] == "Recuperado" and case["ciudad_de_ubicaci_n"] == u"Ibagué":
        counter_recovered += 1
    if case["ciudad_de_ubicaci_n"] == u"Ibagué" and case["atenci_n"] == "Fallecido":
        counter_death += 1

print("Casos en Ibague: " + str(counter))
print("Casos recuperados en Ibague: " + str(counter_recovered))
print("Muertes: " + str(counter_death))

print("-----------------------")
print("Hecho por Diego Vidales")