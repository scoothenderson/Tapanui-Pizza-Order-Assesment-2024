QUESTION_SET = ["INPUT FLAVOUR NUMBER (e.g '1'), 'f' TO FINALISE ORDER, or 'c' TO CANCEL ORDER: " , 
                "ORDER DELIVERY? (Y/N) or 'c' TO CANCEL ORDER: " ,
                "ENTER CUSTOMER ADDRESS or 'c' TO CANCEL ORDER: " ,
                "ENTER CUSTOMER PHONE NUMBER or 'c' TO CANCEL ORDER: " ,
                "ENTER CUSTOMER NAME or 'c' TO CANCEL ORDER: "] 

pizza_menu = { 

    '1' : 'CHEESE', 

    '2' : 'GARLIC CHEESE', 

    '3' : 'HAM AND CHEESE', 

    '4' : 'HAWAIIAN', 

    '5' : 'MEAT LOVERS', 

    '6' : 'PEPPERONI', 

    '7' : 'SUPREME', 

    '8' : 'SEAFOOD', 

    '9' : 'KOREAN BBQ', 

    '10' : 'BUFFALO CHICKEN', 

    '11' : 'MARGHERITA', 

    '12' : 'DELUXE MEATLOVERS' 
     } 

#Function that gathers order information + customer details
def order_info(): 

    #reseting variables for reuse + loop ending variables
    global pizza_order, cusmer_info
    pizza_order = []
    cusmer_info = []
    delivery = False
    final = False
    MAX_PIZZA = 5

    #Prints out pizza menu with corresponding numbers 
    for flavour in pizza_menu: 

        print(pizza_menu[flavour] + ' ' + '[' + flavour + ']') 

    #Loops for a maximum of 5 iterations
    for count in range(MAX_PIZZA): 
        
        #Only asks for input if the user has not finalised order
        if final != True: 

            flav_select = input(QUESTION_SET[0]).lower()
        
        else: 

            break
        
        #Cancels the order if the input was 'c'
        if flav_select == 'c':
        
          return
        
        #Breaks the loop until max range is reached if input was 'f'
        if flav_select == 'f':
            
            final = True 

            break      
        
        #If the number entered is from 1-7, the pizza will cost $8.50
        if int(flav_select) in range(1, 8): 

            pizza_order.append(pizza_menu[flav_select]) 

            pizza_order.append('8.50') 

        #If the number entered is from 8-12, the pizza will cost $13.50
        elif int(flav_select) in range(8, 13): 

            pizza_order.append(pizza_menu[flav_select]) 

            pizza_order.append('13.50') 
    
    #Asks user if order is a delivery
    is_deliv = input(QUESTION_SET[1]).lower()

    #If it is a delivery, ask for address and number
    if is_deliv == 'y':

        delivery = True

        cusmer_addr = input(QUESTION_SET[2])
        cusmer_info.append(cusmer_addr)

        cusmer_num = input(QUESTION_SET[3])
        cusmer_info.append(cusmer_num)
        
    #Cancels the order if input was 'c'
    elif is_deliv == 'c':

        return
    
    #Asks for customer name regardless of being a delivery or not
    cusmer_name = input(QUESTION_SET[4])
    cusmer_info.append(cusmer_name)

order_info()

print(pizza_order)
print(cusmer_info)