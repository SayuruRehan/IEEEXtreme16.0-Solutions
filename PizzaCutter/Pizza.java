// Don't place your source in a package
import java.util.*;
import java.lang.*;
import java.io.*;

// Please name your class Main
class Main {
	public static void main (String[] args) throws java.lang.Exception {
	    Scanner sc = new Scanner(System.in);
	    
		int t = sc.nextInt();

		for (int T = 0; T < t; T++){
		    
		    int n = sc.nextInt();
		    int answer = 0;
		    
		    ArrayList<Integer> unique = new ArrayList<Integer>();
		    
		    for(int N = 0; N < n; N++){
		        int D = sc.nextInt();
		        if(D < 0){
		            D = (D % 180) + 180;
		        }
		        
		        int cut = Math.abs(D % 180);
		        if(!unique.contains(cut)){
		            unique.add(cut);
		            
		        }
		    }
		    
		    if (unique.size() == 0){
		        answer = 1;
		    }else{
		        answer = unique.size() * 2;
		    }
		    
		    System.out.println(answer);
		}
	}
}
