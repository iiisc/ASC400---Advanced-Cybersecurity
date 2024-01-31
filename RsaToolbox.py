"""
Question 1: An attacker may have access to the public key and cipher text, it is mathematically impossbible to decrypt due to the factorization problem.
Question 2: The most commonly used method is trial division which entails checking whether n is divisible by any integer from 2 to sqrt(n). Why this is
depends on redundancy, any factor greater than sqrt(n) would already have corresponding factor smaller than sqrt(n).
Question 3: (lösa tillsammans https://www.symbolab.com/solver/modulo-calculator/15%5E%7B19%7D%20mod%2077?or=input)
"""

def renderMenu():
    print("""     ▄████████    ▄████████    ▄████████          ███      ▄██████▄   ▄██████▄   ▄█       ▀█████████▄   ▄██████▄  ▀████    ▐████▀ 
    ███    ███   ███    ███   ███    ███      ▀█████████▄ ███    ███ ███    ███ ███         ███    ███ ███    ███   ███▌   ████▀  
    ███    ███   ███    █▀    ███    ███         ▀███▀▀██ ███    ███ ███    ███ ███         ███    ███ ███    ███    ███  ▐███    
   ▄███▄▄▄▄██▀   ███          ███    ███          ███   ▀ ███    ███ ███    ███ ███        ▄███▄▄▄██▀  ███    ███    ▀███▄███▀    
  ▀▀███▀▀▀▀▀   ▀███████████ ▀███████████          ███     ███    ███ ███    ███ ███       ▀▀███▀▀▀██▄  ███    ███    ████▀██▄     
  ▀███████████          ███   ███    ███          ███     ███    ███ ███    ███ ███         ███    ██▄ ███    ███   ▐███  ▀███    
    ███    ███    ▄█    ███   ███    ███          ███     ███    ███ ███    ███ ███▌    ▄   ███    ███ ███    ███  ▄███     ███▄  
    ███    ███  ▄████████▀    ███    █▀          ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ ▄█████████▀   ▀██████▀  ████       ███▄ 
    ███    ███                                                                  ▀                                                 """)
    uin = input("***************** RSA Toolbox ******************\n\n~~ WHAT FUNCTION DO YOU WANT TO RUN? ~~\n\n1. Check if num is prime.\n2. Extended Euclidean Algorithm.\n3. Euler phi function.\n4. Calculate modular inverse.\n5. Use file for testcase.\n\n************************************************\n> ")

    match uin:
        case "1":
            x = int(input("What number do you want to check?: "))
            print(isPrime(x))
        case "2":
            a = int(input("a: "))
            b = int(input("b: "))
            print(getGCD(a, b))
        case "3":
            n = int(input("n: "))
            print(getPhi(n))
        case "4":
            print("func4")


def isPrime(a):
    if (a < 2):
        return False
    for i in range(2, a):
        if (a % i == 0):
            return False
    return True

def getGCD(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = getGCD(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

def isRelativePrime(a, b):
    if (getGCD(a, b)[0] == 1):
        return True
    return False

def getModularInverse(n, b):
    gcd, x, y = getGCD(n,b)
    if (gcd == 1):
        return y % n
    return "None found"

def getPhi(n):
    list = []
    for i in range(1, n+1):
        if (isRelativePrime(i,n)):
            list.append(i)
    return list


if __name__ == "__main__":
    while(1):
        renderMenu()
