


def introductionToDictionaries():
   dict = {}
   dict[1] = 1
   dict[2] = 1
   dict[3] = 2
   dict[(1,2,3,4)] = "weird"
   dict["odd"] = 876

   if 2 in dict:
      print("2 is a key!")
      print("its value is" + str(dict[2]))

   dict2 = {1:1, 2:1, 3:2} # key:value pairs



def recursion(n):
   def fib(n):
      if n <= 2:
         return 1
      else:
         return fib(n - 1) + fib(n - 2)
   print(fib(n))

def topDown(n):
   #Top-down
   memory = {1:1, 2:1}
   def fib(n):
       if n <= 2:
           return 1
       if n in memory:
           return memory[n]
       else:
           memory[n] = fib(n-1) + fib(n-2)
           return memory[n]
   print(fib(n))



#Bottom-up
def bottomUp(n):

   fib = [0 for i in range(n+5)]
   fib[0] = 0
   fib[1] = 1
   fib[2] = 1
   for i in range(3, n+1):
      fib[i] = fib[i-1] + fib[i-2]
   print(fib[n])

recursion(40)
bottomUp(100)
topDown(100)

