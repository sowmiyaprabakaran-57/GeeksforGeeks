// User function Template for Java
class Solution {
    public static String compareNM(int n, int m) {
        String greater="greater";
        String lesser="lesser";
        String equal="equal";
       if(n>m)
       {
           return greater;
       }
       else if(n<m)
       {
           return lesser;
       }
       else
       {
           return equal;
       }
   
        
    }
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        System.out.println(compareNM(n,m));
    }
}