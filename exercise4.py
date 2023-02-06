"""
Created by (Esteban Gómez) in  ${2022}
"""
"""
Create a function to convert currencies in an exchange office. It will have a local constant
containing a nested tuple with the exchange rates for the desired currencies (euro, yen, dollar
and sterling pound). It will receive the original currency, the target currency and the quantity to
change and will return the quantity of money in the target currency.
"""

def currencies_exchange(currency1=str, currency2=str,
                        quantity_to_change=float):
    """@This function convert currencies"""
    exchange_rates= (146.75, 1, 0.88), (0.0068, 0.0068, 0.0060), (1, 146.37,
                    0.88),(1.14,167.08, 1.14)
    euro=exchange_rates[0]
    yen = exchange_rates[1]
    dollar = exchange_rates[2]
    sterling_pound= exchange_rates[3]
    if currency1=="euro":
        if currency2=="yen":
            final_value= euro[0] * quantity
        elif currency2=="dollar":
            final_value= euro[1] * quantity
        elif currency2 == "sterling pound":
            final_value = euro[2] * quantity
    elif currency1=="yen":
        if currency2=="euro":
            final_value= yen[0] * quantity
        elif currency2=="dollar":
            final_value= yen[1] * quantity
        elif currency2 == "sterling pound":
            final_value = yen[2] * quantity
    elif currency1=="dollar":
        if currency2=="euro":
            final_value= dollar[0] * quantity
        elif currency2=="yen":
            final_value= dollar[1] * quantity
        elif currency2 == "sterling pound":
            final_value = dollar[2] * quantity
    elif currency1=="sterling pound":
        if currency2=="euro":
            final_value= sterling_pound[0] * quantity
        elif currency2=="yen":
            final_value= sterling_pound[1] * quantity
        elif currency2 == "dollar":
            final_value = sterling_pound[2] * quantity
    return final_value

from_currency= str(input("Which currency you want to change: ")).lower()
to_currency=str(input("To which currency you want to change your currency: "
                      "")).lower()
quantity=float(input("How much you want to change: "))

print(currencies_exchange(from_currency,to_currency,quantity), to_currency)