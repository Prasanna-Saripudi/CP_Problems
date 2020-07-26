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
        int len = s.length(), count=0;
        if(len==1) return s;
        StringBuilder rev = new StringBuilder();
        rev.append(s);
        rev=rev.reverse();
        String palins="";
        for(int i=0;i<len;i++){
            for(int j=len-1;j>i;j--){
                String x= s.substring(i,j+1),y=rev.substring(len-j-1,len-i);
                if(x.equals(y) && x.length()>palins.length()) palins=x;
                else if(x.equals(y) && x.length()==palins.length() &&x.compareTo(palins)>0) palins=x;
            }
        }
        return palins;
    }
    public static void main(String[] args) {
        
    }
}
