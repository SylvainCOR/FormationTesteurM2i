#-------------Factorielle-----------------

def factorielle(num):
    if num == 0 :
        return 1
    else :
        return num * factorielle(num - 1)


n = 13
print(f"{n}! = {factorielle(n)}")

