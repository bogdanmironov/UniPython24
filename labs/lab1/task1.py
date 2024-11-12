'''
Задача 1 (0.75т.)
Напишете функция gather_weather_forecast, която приема:

location: низ (str) - име на местоположение
hours_from_now: list от цели числа (int) - часове от текущия момент, за които имаме прогноза
temperatures: list от цели числа (int) - температури за съответните часове (в градуси Целзий)
rain_probabilities: list от цели числа (int) - вероятности за дъжд за съответните часове (между 0 и 100)
pressures: list от цели числа (int) - налягания за съответните часове (в хектопаскали)
Приемете, че дължините на списъците hours_from_now, temperatures, rain_probabilities и pressures ще съвпадат винаги.

Функцията да върне резултат с тип речник, съдържащ следните ключове и стойности:

location: стойността на аргумента location
forecast: списък от речници всяка прогноза. Всеки от тях съдържа следните ключове и стойности:
hour: стойността на съответния елемент от hours_from_now
temperature: стойността на съответния елемент от temperatures
rain probability: стойността на съответния елемент от rain_probabilities
pressure: стойността на съответния елемент от pressures
Hint: в list се добавя елемент с метода append.
'''


def gather_weather_forecast(location, hours_from_now, temperatures, rain_probabilities, pressures):
    weather_forecast = {"location": location, "forecast": []}

    for hour, temperature, rain_probability, pressure in zip(hours_from_now, temperatures, rain_probabilities, pressures):
        weather_forecast["forecast"].append({
            "hour": hour,
            "temperature": temperature,
            "rain probability": rain_probability,
            "pressure": pressure
        })

    return weather_forecast


assert gather_weather_forecast("Test Island", [1], [22], [12], [1000]) == {
    "location": "Test Island",
    "forecast": [
        {"hour": 1, "temperature": 22, "rain probability": 12, "pressure": 1000},
    ]
}

assert gather_weather_forecast("Studentski Grad", [24, 48, 72], [20, 18, 15], [0, 50, 88], [1000, 990, 980]) == {
    "location": "Studentski Grad",
    "forecast": [
        {"hour": 24, "temperature": 20, "rain probability": 0, "pressure": 1000},
        {"hour": 48, "temperature": 18, "rain probability": 50, "pressure": 990},
        {"hour": 72, "temperature": 15, "rain probability": 88, "pressure": 980},
    ]
}

print("✅ All OK! +0.75 points")