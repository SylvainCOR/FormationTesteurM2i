#-------------Suite de Fibonacci-----------------

def Fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return Fibonacci(n-1) + Fibonacci(n-2)

x = 9
print(f"Le résultat de Fibonacci({x}) donne : {Fibonacci(x)}")
