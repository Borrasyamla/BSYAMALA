
n=int(input('enter n:'))
even_sum=0
odd_sum=0
for i in range(1,n+1):
if i%2==0:
 even_sum=even_sum+i
else:
odd_sum=odd_sum+i
print('the sum of even numbers:',even_sum)
print('the sum of odd numbers:',odd_sum)

Output:
enter n:5
the sum of even numbers:6
the sum of odd numbers:9
