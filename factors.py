import sys

def factors(n):
    """Returns a list of the factors of n"""
    # create a list of the possible factors of n
    # (we only need to consider factors up to the square root of n)
    possible_factors = [i for i in range(2, int(n**0.5)+1)]
    # filter the list to include only the actual factors of n
    factors = [i for i in possible_factors if n % i == 0]
    return factors

def main():
    # get the file name from the command line arguments
    file_name = sys.argv[1]

    # open the file and read the numbers
    with open(file_name, 'r') as f:
        numbers = [int(line.strip()) for line in f]

    # factor each number and print the result
    for n in numbers:
        p, q = factors(n)[:2]  # get the first two factors of n
        print(f"{n}={p}*{q}")

if __name__ == "__main__":
    main()

