import math
def calculate_discount(price,discount_percent):
    new_price = price - (price * discount_percent / 100)
    if discount_percent >=20 :
        return new_price
    else:
        print('Discounts below 20% cannot be applied ')
        return price


price = float(input('Enter price ($): '))
discount_percent = int(input('Enter discount percent: '))

final_price = calculate_discount(price,discount_percent)
print(f'Your final price is {final_price} $')