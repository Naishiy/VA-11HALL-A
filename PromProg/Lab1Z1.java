import java.util.Scanner;

public class Lab1Z1 {

    public static void main(String[] args) {
        /*Задание 1.6*/
        Scanner in = new Scanner(System.in);
        System.out.print("Текущая дата и время: ");
        String date1 = in.nextLine();
        String name = "Аверин, Маликова, Сафонова";
        String date2 = "05.02.2024, 14:58";
        System.out.println("\nРазработчики: " + name + "\nДата и время получения задания: " + date2 + "\nДата и время сдачи задания: " + date1 + "\n");

        in.close();
    }
}
