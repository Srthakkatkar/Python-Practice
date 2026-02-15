colour = input("Enter the Colour of Signal : ").strip().lower()

valid_colours = ["red", "yellow", "green"]

if colour in valid_colours:

    if colour == "red":
        print("STOP")

    elif colour == "yellow":
        print("Ready to GO")

    elif colour == "green":
        print("GO")

else:
    print("Invalid Information! Please enter Red, Yellow, or Green.")
