# Mars Weight

"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

MARS_GRAVITY = 0.378

def main():
    # Get Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))

    # Calculate Mars weight
    mars_weight = earth_weight * MARS_GRAVITY
    rounded_weight = round(mars_weight, 2)

    # Print result
    print("The equivalent weight on Mars: " + str(rounded_weight))

if __name__ == "__main__":
    main()







# Planetary Weights Version
"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.
"""

# Gravity constants
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Get Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Get planet name
    planet = input("Enter a planet (capitalize first letter): ")

    # Decide gravity
    if planet == "Mercury":
        gravity = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity = VENUS_GRAVITY
    elif planet == "Mars":
        gravity = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity = URANUS_GRAVITY
    else:
        gravity = NEPTUNE_GRAVITY

    # Calculate planetary weight
    planetary_weight = earth_weight * gravity
    rounded_weight = round(planetary_weight, 2)

    # Print result
    print("The equivalent weight on " + planet + ": " + str(rounded_weight))

if __name__ == "__main__":
    main()
