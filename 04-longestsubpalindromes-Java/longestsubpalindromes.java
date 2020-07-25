// # Write the function longestSubpalindrome(s), that takes a string s and returns 
// the longest palindrome that occurs as consecutive characters (not just letters, but 
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!") 
// # returns "b-4-b". If there is a tie, return the lexicographically larger value -- 
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce") 
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions, 
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also, 
// from the explanation above, we see that longestSubpalindrome("aba") is "aba", 
// and longestSubpalindrome("a") is "a".
// @author: Prasanna Saripudi
import java.util.*;

class longestsubpalindromes {
	public String fun_longestsubpalindromes(String s){
        int maxL=0,start=0,low=0,high=0;
        String splain="";
        for(int i=1;i<s.length();i++){
            low = i-1;
            high=i;
            while(low>=0 && high < s.length()&&s.charAt(low)==s.charAt(high)){
                if(high-low+1>splain.length()){
                    splain=s.substring(low,high+1);
                }
                else if(high-low+1==splain.length() && s.substring(low,high+1).compareTo(splain) <0){
                    splain=s.substring(low,high+1);
                }
                --low;
                ++high;
            }
            low = i-1;
            high=i+1;
            while(low>=0&&high<s.length()&&s.charAt(low)==s.charAt(high)){
                if(high-low+1>splain.length()){
    splain=s.substring(low,high+1);
                }else if(high-low+1==splain.length() && s.substring(low,high+1).compareTo(splain) <0){
                   splain=s.substring(low,high+1);
                }
                --low;
                ++high;
            }
        }
		return splain;
    }
    public static void main(String[] args) {
        
    }
}
