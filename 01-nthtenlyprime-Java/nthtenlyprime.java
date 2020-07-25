// # Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
// # and returns the nth Additive Prime, which is a prime number such that 
// # the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
// # is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2
//@author: Prasanna Saripudi

// question has been given additive primes., but cases arent for additive
// think the question should be "primes that have the sum of their digits to be 10"
// eg: 19 => 1+9 = 10 and 19 is a prime
class nthtenlyprime {
	public static int fun_nthtenlyprime(int n){
        int count = 0;
        int value=19;
        while(count < n){
            value+=2;
            if(isPrime(value) && sum_digits(value)==10){
                count+=1;
                // System.out.println(value);
            }

        }
		return value;
    }
    public static int sum_digits(int num){
        int sum = 0;
        while(num>0){
            sum += (num%10);
            num /=10;
        }
        return sum;
    }
    public static boolean isPrime(int num){
        if(num<=1) return false;
        else if(num==2 || num==3) return true;
        for(int i=0;i<=num/2;i++){
            if(num%i==0) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        int n = 0;
        System.out.println(fun_nthtenlyprime(0));
    }

}