'''
using elif condition as there are many components.
'''
def calculate_electricity_bill(units):
    total = 0

    if units <= 100:
        total = units * 5
        print(f"0-{units} units @ ₹5/unit = ₹{total}")

    elif units <= 300:
        total = (100 * 5) + (units - 100) * 7
        print("0-100 units @ ₹5/unit = ₹500")
        print(f"101-{units} units @ ₹7/unit = ₹{(units - 100) * 7}")

    elif units <= 500:
        total = (100 * 5) + (200 * 7) + (units - 300) * 10
        print("0-100 units @ ₹5/unit = ₹500")
        print("101-300 units @ ₹7/unit = ₹1400")
        print(f"301-{units} units @ ₹10/unit = ₹{(units - 300) * 10}")

    else:  # Above 500
        total = (100 * 5) + (200 * 7) + (200 * 10) + (units - 500) * 15
        print("0-100 units @ ₹5/unit = ₹500")
        print("101-300 units @ ₹7/unit = ₹1400")
        print("301-500 units @ ₹10/unit = ₹2000")
        print(f"Above 500 units @ ₹15/unit = ₹{(units - 500) * 15}")

    print(f"\nTotal Amount Payable = ₹{total}")


def main():
    try:
        units = int(input("Enter electricity usage in kWh: "))
        if units < 0:
            print("Usage cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print("\nElectricity Bill:")
    calculate_electricity_bill(units)

if __name__ == "__main__":
    main()
