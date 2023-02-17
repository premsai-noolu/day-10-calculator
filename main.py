from art import logo
print(logo)

n1=int(input("what the 1st number "))
def add(n1,n2):
  return n1+n2

def mul(n1,n2):
  return n1*n2

def sub(n1,n2):
  return n1-n2

def div(n1,n2):
  return n1/n2
#n2=int(input("whats the next number "))
operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
} 
for i in operations:
  print(i)
calci=True
while calci:
  operator=input("pick an operation ")
  n2=int(input("whats the next number "))
  result=operations[operator]
  new_res=result(n1,n2)
  print(f"{n1} {operator} {n2} = {new_res} ")
  n1=new_res
  continues=input("Type Y to continue calculating with result or type N to stop current calculation ")
  if continues!="Y":
    break
    
   

