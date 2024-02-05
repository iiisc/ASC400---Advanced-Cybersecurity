import os

"""
Question 1: 
    An attacker may have access to the public key and cipher text, 
    it is mathematically impossbible to decrypt due to the factorization problem.
Question 2: 
    The most commonly used method is trial division which entails checking whether n is divisible by any integer from 2 to sqrt(n). 
    Why this is depends on redundancy, any factor greater than sqrt(n) would already have corresponding factor smaller than sqrt(n).
Question 3: The RSA encryption algorithm is c=m^e mod n where c is the encrypted message, 
    m is the message, e and n is the private key. 
    In this case m=15 e=19 n=77 which gives c=15^19 mod 77 = 36. The complete calculation would be as follows:
    
    15^9 mod 77 => 
    (15^2)^9 * 15 mod 77 
    => ((((15^2 mod 77)^9) mod 77) * (15 mod 77)) mod 77
    => ((((225 mod 77)^9) mod 77) * 15) ) mod 77
    => (((((5041 mod 77)^4) mod 77) * 71) mod 77) * 15) mod 77
    => ((((((1296 mod 77)^2) mod 77) * 71) mod 77) * 15) mod 77 
    => ((((4096 mod 77) * 71) mod 77) * 15) mod 77
    => ((1065 mod 77) * 15) mod 77
    => 960 mod 77
    = 36
"""

def renderMenu():
    """ Renders the menu for the application"""

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
            if (isPrime(x)):
                print(f'{x} is a prime number')
            else:
                print(f'{x} is not a prime number')

        case "2":
            a = int(input("a: "))
            b = int(input("b: "))
            gcd = getGCD(a, b)
            print(f'GCD = {gcd[0]}. X = {gcd[1]}. Y = {gcd[2]}')

        case "3":
            n = int(input("n: "))
            phi = getPhi(n)
            print(f'{len(phi)} positive integers smaller then {n} are relative prime to {n}.')
            print(f'The numbers are: {phi}')

        case "4":
            integer = int(input("Integer: "))
            modulus = int(input("Modulus: "))
            modularInverse = getModularInverse(modulus, integer)
            if (isinstance(modularInverse, int)):
                print(f'The multiplicative inverse of integer {integer} (mod {modulus}) is {modularInverse}')
            else:
                print(f"No multiplicative inverse of integer {integer} (mod {modulus}) found.")

def isPrime(a):
    """ Checks if a numbers is a prime number. Returns bool"""
    if (a < 2):
        return False
    for i in range(2, a):
        if (a % i == 0):
            return False
    return True

def getGCD(a, b):
    """ Finds greatest common denominator for two numbers """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = getGCD(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

def isRelativePrime(a, b):
    """ Checks if two numbers are relative prime to each other. Returns bool """
    if (getGCD(a, b)[0] == 1):
        return True
    return False

def getModularInverse(n, b):
    """ Calculates modular inverse. Returns int or string """
    gcd, x, y = getGCD(n,b)
    if (gcd == 1):
        return y % n
    return "None found"

def getPhi(n):
    """ Eulers totient phi. Returns list """
    list = []
    for i in range(1, n+1):
        if (isRelativePrime(i,n)):
            list.append(i)
    return list


if __name__ == "__main__":
    while(1):
        os.system('cls')
        renderMenu()
        input("\n Press any key to continue. There is no exit. You will enjoy it.\n")

