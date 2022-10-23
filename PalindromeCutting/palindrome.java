import java.util.*;
import java.lang.*;
import java.io.*;

class Main{
    static int countPS(String str){
        int n = str.length();
        int[][] cps = new int[n][n];
        
        for (int i = 0; i < n; i++)
            cps[i][i] = 1;
            
        for (int l = 2; l <= n; l++){
            for (int i = 0; i <= n - l; i++) {
                int k = l + i - 1;
                
                if(str.charAt(i) == str.charAt(k)) {
                    cps[i][k] = cps[i][k - 1] + cps[i + 1][k] + 1;
                }
                else{
                    cps[i][k] = cps[i][k - 1] + cps[i + 1][k] - cps[i + 1][k - 1];
                }
            }
        }
        return cps[0][n - 1];
    }
    public static void main(String args[]){
        String str = "abcb";
        System.out.println(countPS(str));
    }
}
