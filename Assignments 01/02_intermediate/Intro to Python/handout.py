# Milestone #1: Mars Weight (Earth → Mars Weight Calculator)

earth_weight = float(input("Enter a weight on Earth: "))
mars_weight = earth_weight * 0.378


print("The equivalent on Mars:", round(mars_weight, 2))


#  Milestone #2: All Planets (Earth → Any Planet Weight Calculator)

gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}


earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")


planet_weight = earth_weight * gravity_factors[planet]


print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")
