# Constants for gravity on different planets
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():
    # Get the user's Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))

    # Get the name of the planet
    planet = input("Enter a planet: ")

    # Select the correct gravity constant
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY

    # Calculate planetary weight
    planetary_weight = earth_weight * gravity_constant
    rounded_weight = round(planetary_weight, 2)

    # Print result
    print("The equivalent weight on " + planet + ": " + str(rounded_weight))

# This runs the main function if this file is executed directly
if __name__ == "__main__":
    main()
