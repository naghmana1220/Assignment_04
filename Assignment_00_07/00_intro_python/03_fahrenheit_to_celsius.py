def main():
    fahrenhit = float(input("\033[1;3m Enter temperature in fahrenhit: \033[0m "))

    celsius = (fahrenhit - 32) *5.0 / 9.0

    print(f"Temperature: {fahrenhit}F = {celsius}C")

if __name__ =='__main__':
   main()