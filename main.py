import time

while True:
    try:
        toCount = input("Enter the number: ")
        startTime = time.time()

        def massiveCounting(maxNumber):
            count = 0
            while count <= maxNumber:
                count += 1
                currentTime = time.time()
            resultTime = currentTime - startTime
            return resultTime
        ourResult = massiveCounting(int(toCount))
        print(f"Computer count this for {ourResult} seconds")
        askYN = input("Wanna some number again?: ").lower()
        if (askYN == "y"):
            time.sleep(1)
            print("Alright :)")
            continue
        else:
            print("Goodbye :)")
            break
    except ValueError:
        print("Invalid input. Please enter a number.") #smí se dát funkce do try
