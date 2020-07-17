# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n
# and returns the nth palindromic Prime, which is a palidrome number such that
# it is also a prime. For example, 313 is a palindrome and it is prime
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2
# author: Prasanna Saripudi

def fun_nth_palindromic_prime(n):
    count = -1
    num = 2
    while n > count:
        # for checking palindrome can check using slicing or reversed(string) or iteration
        if str(num) == str(num)[::-1] and isPrime(num):
            count += 1
        if count == n:
            return num
        num += 1


def isPrime(num):
    # checking if prime or not, can also do via sieve of erosthenes
    if num <= 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True
