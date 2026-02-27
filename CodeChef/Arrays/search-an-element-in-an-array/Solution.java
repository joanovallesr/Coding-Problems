public class Solution {
    public static void main (String[] args) throws java.lang.Exception
	{
	    Scanner scan = new Scanner(System.in);
	    
	    int N = scan.nextInt();
	    int X = scan.nextInt();
	    int[] A = new int[N];
	    
	    for (int i = 0; i < N; i++) {
	        A[i] = scan.nextInt();
	    }
	    
		for (int i = 0; i < N; i++) {
		    if (A[i] == X) {
		        System.out.println("YES");
		        return;
		    }
		}
		
		System.out.println("NO");
	}
}
