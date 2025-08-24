// User function template for Java

class Solution 
{
    static String toLower(String s)
    {
        
     return s.toLowerCase();
        
    }
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        String s=sc.next();
        System.out.println(toLower(s));
        
    }
}