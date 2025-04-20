def main():
    
    countries = {
        "Peturksbouipo": 16,
        "Stanlau": 25,
        "Mayengua": 48
    }

    
    user_age = int(input("How old are you? "))


    for country, age_limit in countries.items():
        if user_age >= age_limit:
            print(f"You can vote in {country} where the voting age is {age_limit}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {age_limit}.")


if __name__ == '__main__':
    main()
