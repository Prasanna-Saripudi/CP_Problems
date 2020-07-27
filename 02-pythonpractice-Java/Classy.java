// You can use this class to represent how classy someone
// or something is.
// "Classy" is interchangable with "fancy".
// If you add fancy-looking items, you will increase
// your "classiness".
// Create a function in "Classy" that takes a string as
// input and adds it to the "items" list.
// Another method should calculate the "classiness"
// value based on the items.
// The following items have classiness points associated
// with them:
// "tophat" = 2
// "bowtie" = 4
// "monocle" = 5
// Everything else has 0 points.
// Use the test cases below to guide you!

import java.util.ArrayList;
import java.util.List;

public class Classy {
    List<String> items;
    public Classy(){
    this.items=new ArrayList<String>();
    }

    public void addItem(String item){
        this.items.add(item);
    }
    public int classiness(){
        int score=0;
        for(String item:this.items){
            if(item=="tophat") score+=2;
            else if(item=="bowtie") score+=4;
            else if(item=="monocle") score+=5;
            else score+=0;
        }
        return score;
    }
    public static void main(String[] args) {
        
    }

}
