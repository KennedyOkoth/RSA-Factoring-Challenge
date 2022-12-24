import sys
from sympy import isprime

def find_primes(n):
    """Returns the two prime factors of n"""
    # create a list of the possible factors of n
    # (we only need to consider factors up to the square root of n)
    possible_factors = [i for i in range(2, int(n**0.5)+1)]
    # iterate over the possible factors and check if they are prime
    for i in possible_factors:
        if n % i == 0:
            p, q = i, n // i
            if isprime(p) and isprime(q):
                return p, q
    # if no prime factors were found, return None
    return None

def main():
    # get the file name from the command line arguments
    file_name = sys.argv[1]

    # open the file and read the number
    with open(file_name, 'r') as f:
        n = int(f.read().strip())

    # find the prime factors of n
    p, q = find_primes(n)

    # print the result
    if p and q:
        print(f"{n}={p}*{q}")
    else:
        print("Could not find prime factors")

if __name__ == "__main__":
    main()

