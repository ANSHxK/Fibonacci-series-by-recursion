def fibonacci(n):
  if n<=1:
    return n 
  else:
    return fibonacci(n-1) + fibonacci(n-2)
    
nterms = int(input("Enter a number: "))

for i in range(nterms):
  print("The fibonacci series for the number",nterms,"is: ", fibonacci(i))
  