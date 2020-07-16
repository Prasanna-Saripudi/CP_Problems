// Write a non static method called "show_excitement" where the string
// "I am super excited for this course!" is returned exactly
// 5 times, where each sentence is separated by a single space.
// Return the string with "return".
// You can only have the string once in your code.
// Don't just copy/paste it 5 times into a single variable!
// author: Prasanna Saripudi

public class PythonBasics {
	public String show_excitement() {
		// str.repeat(n) not working for java8;only avai for java 11
		String s = "";
		for (int i = 0; i < 5; i++) {
			s += "I am super excited for this course! ";
		}
		return s;
	}

	public static void main(String args[]) {

	}
}