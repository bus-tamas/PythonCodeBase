# Tamás Bus, 2023.10.17

def main():

    size = input("Do you want small, medium, or large?")
    coffee_type = input("Do you want brewed, espresso, or cold press?")
    decide_flavoring = input("Do you want a flavored syrup? (Yes or No)").lower()
    if decide_flavoring == "no":
        flavoring = "none"
    elif decide_flavoring == "yes":
        flavoring = input("Do you want hazelnut, vanilla, or caramel?")

    try:
        price = 0

        if size == "small":
            price += 2
        elif size == "medium":
            price += 3
        elif size == "large":
            price += 4
        else:
            raise ValueError("Invalid size choice")

        if coffee_type == "brewed":
            pass
        elif coffee_type == "espresso":
            price += 0.5
        elif coffee_type == "cold press":
            price += 1
        else:
            raise ValueError("Invalid type choice")


        if flavoring in ["hazelnut","vanilla","caramel"]:
            price += 0.5
        elif flavoring == "none":
            pass
        else:
            raise ValueError("Invalid flavoring choice")

        print(f"You asked for a {size} cup of {coffee_type} coffee with {flavoring} syrup.")
        print(f"Your cup of coffee costs: ${price}")
        print(f"The price with a tip is: ${round(price*1.15,2)}")

    except ValueError as e:
        print(e)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

