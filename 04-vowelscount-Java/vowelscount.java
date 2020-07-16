// # Write the function vowelCount(s), that takes a string s, 
// # and returns the number of vowels in s, ignoring case, 
// # so "A" and "a" are both vowels. The vowels are "a", "e", "i", "o", and "u". 
// # So, for example, ("Abc def!!! a? yzyzyz!") returns 3 (two a's and one e).

class vowelscount {
	public int fun_vowelscount(String s) {
		int count = 0;
		s = s.toLowerCase();
		for (int i = 0; i < s.length(); i++) {
			char ch = s.charAt(i);
			if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u')
				count++;
		}
		return count;
	}

	public static void main(String[] args) {

	}
}