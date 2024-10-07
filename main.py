def main():
    while True:
        # GUI
        choice = input("Enter Corresponding number to function: \n 1: Get a City's Weather \n 2: Compare Cities \n q: Quit \n\n").strip()

        if choice == '1':
            import createrequest as cr
            cr.WeatherInfo()
        elif choice == '2':
            import comparerequest as crt
            crt.CompareRequest()
        elif choice.lower() == 'q':
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid input. Please type '1', '2', or 'q' to quit.\n")

# Runs GUI
if __name__ == "__main__":
    main()
