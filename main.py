import random

def sum_1d_array(numbers):
   r =len(numbers)
   prev_num=[numbers[0]]

   for i in range(1,r):
      numbers[i]+=numbers[i-1]
      prev_num.append(numbers[i])
   return prev_num

zadani = []
for i in range(1000):
   zadani.append(random.randint(1,9))

nums = [1,2,4,8,9,15,17]
print(sum_1d_array(nums))








