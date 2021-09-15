# Currency Converter

if __name__ == "__main__":
    with open('currencyData.txt') as f:
        lines = f.readlines()

    currencyDict = {}
    for line in lines:
        parsed = line.split('\t')
        currencyDict.update({parsed[0]: [float(parsed[1]), float(parsed[2])]})

    print("\n*****Currency Converter*****")
    print("Available options:")
    [print(item) for item in currencyDict.keys()]

    currency_from = input("\nFrom which currency you want to convert your amount?\n")

    amount = int(input(f"\nEnter an amount in {currency_from}: "))

    currency_to = input("\nEnter currency you want to convert this amount to?\n")

    print(f"\n{amount} {currency_from} is equal to "\
    f"{amount * currencyDict[currency_from][1] * currencyDict[currency_to][0]} {currency_to}")
