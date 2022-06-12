import sys
import os


def prime(s):
    # your code goes here
 def prime(number): 
    if number >1:
        for i in range(2, number):
            if number%i ==0:
               print(f"{number} is a prime")
            else: 
                print(f"{number} is not a prime")
    else:
        print("Enter number the is greater than one")             


prime(8)            


def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
