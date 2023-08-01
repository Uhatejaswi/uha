def get_temperature(date):
    # Your code to fetch temperature data for the input date goes here
    # For demonstration purposes, let's assume the temperature is retrieved from a database or API
    temperature = 25.5
    return temperature

def get_wind_speed(date):
    # Your code to fetch wind speed data for the input date goes here
    # For demonstration purposes, let's assume the wind speed is retrieved from a database or API
    wind_speed = 15.7
    return wind_speed

def get_pressure(date):
    # Your code to fetch pressure data for the input date goes here
    # For demonstration purposes, let's assume the pressure is retrieved from a database or API
    pressure = 1012.3
    return pressure

def main():
    while True:
        print("Press 1 to get temperature.")
        print("Press 2 to get wind speed.")
        print("Press 3 to get pressure.")
        print("Press 0 to terminate the program.")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            date = input("Enter the date: ")
            temperature = get_temperature(date)
            print(f"The temperature on {date} is {temperature}°C.")
        elif choice == 2:
            date = input("Enter the date: ")
            wind_speed = get_wind_speed(date)
            print(f"The wind speed on {date} is {wind_speed} km/h.")
        elif choice == 3:
            date = input("Enter the date: ")
            pressure = get_pressure(date)
            print(f"The pressure on {date} is {pressure} hPa.")
        elif choice == 0:
            print("Terminating the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()