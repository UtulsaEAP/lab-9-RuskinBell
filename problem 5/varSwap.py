def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   
   user_val_vect = [user_val2, user_val1, user_val4, user_val3]

   user_val1 = user_val_vect[0]
   user_val2 = user_val_vect[1]
   user_val3 = user_val_vect[2]
   user_val4 = user_val_vect[3]

   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here

   swapped_vect = ""

   for i in swap_values(user_input1, user_input2, user_input3, user_input4):
      swapped_vect = swapped_vect + " " + str(i)

   print(swapped_vect)

   #print those output

 