// # Write the function getInRange(x, bound1, bound2) which takes 3 int values
// # x, bound1, and bound2, where bound1 is not necessarily less than bound2. 
// # If x is between the two bounds, just return it unmodified. Otherwise, 
// # if x is less than the lower bound, return the lower bound, 
// # or if x is greater than the upper bound, return the upper bound.

class getinrange {
	public int fun_getinrange(int x, int bound1, int bound2){
		int low=bound1,high=bound2;
		if(bound1> bound2){
			low=bound2;
			high=bound1;
		}
		if(x>low && x<high) return x;
		else if(x<low) return low;
		else if(x>high) return high;
		return -1;
	}
	public static void main(String[] args) {	
	}
}