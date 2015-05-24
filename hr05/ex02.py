item_name = raw_input("what would you like to buy: [alpha] ")
item_name.strip()


def get_quantity():
    quantity = ''
    while not quantity.isdigit():
        try:
            q = raw_input('how many {}: [integer] '.format(item_name))
            quantity = int(q)
            return quantity
        except:
            print('please try again.')


def get_price():
    price = ''
    while not price.isdigit():
        try:
            p = raw_input('how much do they cost: [decimal] ')
            price = float(p)
            return price
        except:
            print("please try again.")


item_quantity = get_quantity()
item_price = get_price()

print("The price of {} {} is ${}".format(item_quantity, item_name,
                                        (item_quantity * item_price)))
print('Thanks for shopping with us!')
