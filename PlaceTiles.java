// Place Tiles of size 1*m in floor of size n*m
import java.util.Scanner;

public class PlaceTiles{
    public static int placeTile(int n , int m) {
        if(n==m){
            return 2;
        }
        if(n<m){
            return 1;
        }
        // vertically
        int vertPlacements = placeTile(n-m,m);
        // horizontally
        int horPlacements = placeTile(n-1, m);
        return vertPlacements + horPlacements;
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no. of row : ");
        int n = sc.nextInt();          //Matrix n*m
        System.out.print("Enter no. of Colmns : ");
        int m = sc.nextInt();
        System.out.print("Total Possible wave to Place Tiles : " );
        System.out.println(placeTile(n, m));
    }
}


//@harshmeena0645
