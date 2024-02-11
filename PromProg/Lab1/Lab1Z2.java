import java.util.Scanner;

public class Lab1Z2 {
    public static void main() {
        /*Задание 2.6*/
        Scanner in = new Scanner(System.in);
        System.out.print("Сколько чисел вы хотите ввести: ");
        int n = in.nextInt();

        int[] array = new int [n];
        for(int i = 0; i < n; i++)
        {
            i++;
            System.out.print("Число " + i + " = ");
            i--;
            array[i] = in.nextInt();
        }
        System.out.println("Простыми являются:");

        for(int i = 0; i < n; i++){
            boolean f = true;

            for (int a = 2; a < array[i]; a++){

                if(array[i] % a == 0){
                    f = false;
                    break;
                }
            }

            if(f){
                System.out.print(array[i] + " ");
            }
        }
        in.close();
    }
}
