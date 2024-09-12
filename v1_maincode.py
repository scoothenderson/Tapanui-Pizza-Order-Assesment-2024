def order_info():
    question = input('Input testing case (Y/N)').lower()
    if question == 'y':
      return True
    elif question == 'n':
      return False

def receip_print():
  print("Heres the receipt!")
  question = input('Input whether the details are correct (Y/N) or c to cancel: ').lower()
  if question == 'y':
    return True
  elif question == 'n':
    return False
  elif question == 'c':
    return False

while quit != True:
   
   open_quest = input("Enter 'o' to order, or 'q' to quit: ").lower()

   if open_quest == 'q':
     
     print('Thank you for using PIZZA ORDERING SYSTEM.')

     quit = True

     break
   
   elif open_quest == 'o':
      
      if order_info() == False:
     
       continue
    
      else:

       if receip_print() == False:
         
         print('Order is either not correct or the user wants to cancel, either way we will let them restart')
         
         continue
       
       else:
         
         print('Success! order is complete!')
        
     

