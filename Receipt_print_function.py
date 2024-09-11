def receip_print(order, is_deliv, detail):

    prices = []
    total_cost = 0

    for cost in range(1, len(order), 2):

        prices.append(order[cost])

        total_cost += float(order[cost])
    
    flavours = []

    for item in range(0, len(order), 2):

        flavours.append(order[item])
    
    print('------------------------')
    print('Total pizzas ordered: ' + str(len(flavours)))
    print('------------------------')
    print(' Pizzas ordered ')
    print('----------------')

    for count in range(0, len(flavours)):

        print(flavours[count], '- $' + prices[count])
    
    if is_deliv == True:

        print()
        print('Delivery surcharge + $3.00\n')

        total_cost += 3
    
    print('------------------')
    print('Total cost - $' + str(total_cost))
    print('------------------\n')

    print(' Customer details ')
    print('------------------')
    
    if is_deliv == True:
        print('Customer Address: ' + (detail[0]) + '\n')
        print('Customer Phone number: ' + (detail[1]) + '\n')
    
    print('Order name: ' + (detail[2]))
    print('------------------')

    confirm = input("ORDER CORRECT? (Y/N), or 'c' TO CANCEL ORDER: ")

    if confirm == 'Y':
        return True
    
    if confirm == 'N':
        return False
    
    else:
        return False



pizza_order = ['CHEESE', '8.50', 'GARLIC CHEESE', '8.50', 'SEAFOOD', '13.50', 'MARGHERITA', '13.50']
delivery = True
cusmer_info = ['123 Mate Road', '123 456 7890', 'Bill Gates']

receip_print(pizza_order, delivery, cusmer_info)
