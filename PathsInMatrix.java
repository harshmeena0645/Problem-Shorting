// Count total paths in maze to move from (0,0) to (n,m)
import java.util.Scanner;

public class PathsInMatrix{
    public static int paths(int i, int j, int n,int m){
        if( i==n || j==n ){
            return 0;
        }
        if( i== n-1 && j== n-1 ){
            return 1;
        }
        int downpath = paths( i+1 , j, n , m );
        int rightpath= paths(i, j+1, n , m );
        return downpath + rightpath ;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no. of row : ");
        int n = sc.nextInt();        //Matrix n*m
        System.out.print("Enter no. of Colmns : ");
        int m = sc.nextInt();
        int totalPaths = paths(0,0,n,m);
        System.out.print("Total Possible wave : ");
        System.out.println(totalPaths);
    }
}


//@harshmeena0645
