import java.util.Scanner;

public class Lab1_PromProg {

    public static void main(String[] args) {
        /*Задание 1.6*/
        Scanner in = new Scanner(System.in);
        System.out.print("Текущая дата и время: ");
        String date1 = in.nextLine();
        String name = "Аверин, Маликова, Сафонова";
        String date2 = "05.02.2024, 14:58";
        System.out.println("\nРазработчики: " + name + "\nДата и время получения задания: " + date2 + "\nДата и время сдачи задания: " + date1 + "\n");

        /*Задание 2.6*/
        System.out.print("Сколько чисел вы хотите ввести: ");
        int n = in.nextInt();

        int[] array = new int [n];
        for(int i = 0; i < n; i++)
        {
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
    }
}