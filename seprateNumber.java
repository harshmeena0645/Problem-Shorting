import java.util.Scanner;

public class seprateNumber {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int positive = 0;
        int negative = 0;
        int zeroes = 0;
            System.out.print("1 for Continue , 0 for Exit:");
            int question = sc.nextInt();
            while(question==1){
                System.out.print("Enter your number: ");
                int value = sc.nextInt();
                if(value>0){
                    positive++;
                }
                else if(value<0){
                    negative++;
                }
                else{
                    zeroes++;
                }
                System.out.print("1 for Continue , 0 for Exit:");
                question = sc.nextInt();
                
            }
            System.out.println("positive :" + positive);
            System.out.println("negative : " + negative);
            System.out.println("zeroes : " + zeroes);
    }
}


//@harshmeena0645
