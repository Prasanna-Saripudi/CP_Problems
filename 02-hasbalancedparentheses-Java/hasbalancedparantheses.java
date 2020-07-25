// # Write the function hasBalancedParentheses, which takes a string and returns True 
// # if that code has balanced parentheses and False otherwise (ignoring all 
// # 	non-parentheses in the string). We say that parentheses are balanced if each 
// # right parenthesis closes (matches) an open (unmatched) left parenthesis, 
// # and no left parentheses are left unclosed (unmatched) at the end of the text. 
// # So, for example, "( ( ( ) ( ) ) ( ) )" is balanced, but "( ) )" is not balanced, and "( ) ) (" 
// # is also not balanced. Hint: keep track of how many right parentheses remain unmatched as 
// # you iterate over the string.

import java.util.*;

class hasbalancedparantheses {
	public boolean fun_hasbalancedparantheses(String s){
        if(s.length()==0) return true;
        Stack<Character> stack = new Stack<Character>();
        for(int i=0;i<s.length();i++){
            char curr = s.charAt(i);
            if(curr=='{' || curr=='['||curr=='('){
                stack.push(curr);
            }
            if(curr=='}'||curr==']'||curr==')'){
                if(stack.isEmpty()){
                    return false;
                }
                char prev = stack.peek();
                if(curr=='}' && prev=='{' || curr==']' && prev=='[' || curr==')' && prev=='('){
                    stack.pop();
                }else{
                    return false;
                }
            }
        }
		 return stack.isEmpty() ? true:false;	
	}
    public static void main(String[] args) {
        
    }
}
	