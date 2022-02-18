import random

def sum_1d_array(numbers):
   r =len(numbers)
   new_list=[numbers[0]]

   for i in range(1,r):
      numbers[i]+=numbers[i-1]
      new_list.append(numbers[i])
   return new_list

zadani = []
for i in range(1000):
   zadani.append(random.randint(1,9))

nums = [1,2,4,8,9,15,17]
print(sum_1d_array(nums))

# Program goes through list of number via for cycle.
# It starts new list with first number of original list.
# Then it takes next number and sum it with previous one. It goes until for cycle ends.
# I used zadani as example of creating random list of nums containing only one numeral.
# Example nums is used just to show it on shorter list.