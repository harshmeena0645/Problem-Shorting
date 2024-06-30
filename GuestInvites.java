//Find the no. of Wave in which you can invite n people to your party,single or in pairs

import java.util.Scanner;

public class GuestInvites{
    public static int callGuests(int n) {
        if(n <= 1){
            return 1;
        }
        // single
        int ways1 = callGuests(n-1);
        // pair
        int ways2 = (n-1)*callGuests(n-2);

        return ways1 + ways2;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter no. of Guests : ");
        int n = sc.nextInt();
        System.out.print("Possible wave : ");
        System.out.println(callGuests(n));
    }
}


//@harshmeena0645