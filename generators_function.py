#A generator is a special type of function that remembers its state and can produce 
#a sequence of values one at a time using the yield keyword (instead of return). 
def numbers():
  for i in range(1,6)
     yield i
gen = numbers()
print(next(gen))
