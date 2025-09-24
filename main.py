from mylib import MyLib as mlb

inputchar   = input("Enter Character: ")
inputnumber = input("How many turns you want to run: ")

for round in range ( 0 ,  int(inputnumber ) ) :
    result = mlb.myfunc( inputchar  ,  round ) 
    print (result)
