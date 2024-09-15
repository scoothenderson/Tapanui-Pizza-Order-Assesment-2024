ERROR_MSG = ('''
-----------------------------------------------------------------------------------
PLEASE ENTER A WHOLE NUMBER FROM 1 - 12 (e.g. '1' or '7' or '11') or 'f' or 'c':
-----------------------------------------------------------------------------------''')

QUESTION_SET = ['''
-----------------------------------------------------------------------------
INPUT FLAVOUR NUMBER (e.g '1'), 'f' TO FINALISE ORDER, or 'c' TO CANCEL ORDER:
-----------------------------------------------------------------------------\n''' , 
                '''
---------------------------------------------
ORDER DELIVERY? (Y/N) or 'c' TO CANCEL ORDER:
---------------------------------------------\n''' ,
                '''
----------------------------------------------
ENTER CUSTOMER ADDRESS or 'c' TO CANCEL ORDER:
----------------------------------------------\n''' ,
                '''
---------------------------------------------------
ENTER CUSTOMER PHONE NUMBER or 'c' TO CANCEL ORDER:
---------------------------------------------------\n''' ,
                '''
-------------------------------------------
ENTER CUSTOMER NAME or 'c' TO CANCEL ORDER:
-------------------------------------------\n'''] 

GOURM_COST = "13.50"
REG_COST = "8.50"
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
    global pizza_order, cusmer_info, delivery
    pizza_order = []
    cusmer_info = []
    delivery = False
    final = False

    #Maximum pizzas in order
    MAX_PIZZA = 5
    
    #Boundaries for suitable address length
    MAX_ADDRESS = 35
    MIN_ADDRESS = 5

    #Boundaries for suitable phone number length
    MAX_PHONE = 10
    MIN_PHONE = 8
    
    #Boundaries for suitable name length
    MIN_NAME = 3
    MAX_NAME = 12

    #Prints out pizza menu with corresponding numbers 
    for flavour in pizza_menu: 

        print(pizza_menu[flavour] + ' ' + '[' + flavour + ']') 

    #Loops for a maximum of 5 iterations
    count = 0
    flav_select = 0

    while count != MAX_PIZZA: 
        
        #Only asks for input if the user has not finalised order
        if final != True:

              flav_select = input(QUESTION_SET[0]).lower()
        
        else: 

            break

        #Cancels the order if the input was 'c'
        if flav_select == 'c':
          
          return False
        
        #Breaks the loop until max range is reached if input was 'f'
        if flav_select == 'f':
            
            final = True 

            break      
        
        #Checks to make sure number is an integer and exists in a range from 1 - 12
        try:
          
          if int(flav_select) in range (1, 13):
                
            #If the number entered is from 1-7, the pizza will cost $8.50
                if int(flav_select) in range(1, 8): 

                    pizza_order.append(pizza_menu[flav_select]) 

                    pizza_order.append(REG_COST) 

            #If the number entered is from 8-12, the pizza will cost $13.50
                elif int(flav_select) in range(8, 13): 

                    pizza_order.append(pizza_menu[flav_select]) 

                    pizza_order.append(GOURM_COST)        
          else:
              print(ERROR_MSG)

              continue

        except ValueError:

            print(ERROR_MSG)

            continue

        count += 1
    
    #Loops until broken
    while True:
        #Asks user if order is a delivery
        is_deliv = input(QUESTION_SET[1]).lower()
        
        if is_deliv in ('y', 'n', 'c'):
            #Breaks loop if correct input is given
            break

        else:

            print("INVALID INPUT, PLEASE ENTER 'y', 'n', or 'c'")
    

    #If it is a delivery, ask for address and phone number
    if is_deliv == 'y':

        delivery = True

        #Loops until broken 
        while True:
        
            cusmer_addr = input(QUESTION_SET[2])
            
            #Appends customer address if it fits requirements
            if len(cusmer_addr) > MIN_ADDRESS and len(cusmer_addr) < MAX_ADDRESS:
            
                cusmer_info.append(cusmer_addr)

                break
            
            #Cancels the order if input was 'c'
            elif cusmer_addr == 'c':
            
                return False
            
            else:
                print(f"PLEASE ENTER AN ADDRESS BETWEEN {MIN_ADDRESS} - {MAX_ADDRESS} CHARACTERS\n")
        
        #Loops until broken
        while True:
            try:
                cusmer_num = input(QUESTION_SET[3]).lower()

                #Cancels the order if input was 'c'
                if cusmer_num == 'c':
                    
                    return False
                
                #Tries to convert the number into an integer after removing spaces
                cusmer_num = cusmer_num.split()

                cusmer_num = int(''.join(cusmer_num))

                #appends customer number if it fits requirements
                if len(str(cusmer_num)) >= MIN_PHONE and len(str(cusmer_num)) <= MAX_PHONE:
                    
                    cusmer_info.append(cusmer_num)

                    break
                
                else:
                    print(f'PLEASE ENTER A PHONE NUMBER BETWEEN {MIN_PHONE} - {MAX_PHONE} NUMBERS\n')

            except ValueError:
                print("PLEASE ENTER INTEGERS ONLY")

    #Cancels the order if input was 'c'
    elif is_deliv == 'c':

        return False
    
    while True:
        #Asks for customer name regardless of being a delivery or not
        cusmer_name = input(QUESTION_SET[4])

        if len(cusmer_name) >= MIN_NAME and len(cusmer_name) <= MAX_NAME:
          
          cusmer_info.append(cusmer_name)

          break

        #Cancels the order if input was 'c'
        elif cusmer_name == 'c':
            
            return False
        
        

order_info()

print(pizza_order)
print(cusmer_info)