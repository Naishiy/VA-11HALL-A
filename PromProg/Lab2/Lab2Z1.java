import java.util.Scanner;

public class Lab2Z1 {

    public static void main() {

        /*Ввод чисел*/
        System.out.print("Введите несколько чисел: ");
        Scanner in = new Scanner(System.in);
        String line = in.nextLine();

        /*Считывание отдельных чисел*/
        for (String s : line.split(" ")) {

            /*Проверка состоит ли следующий после пробела набор символов из цифр*/
            if (s.matches("\\d+")) {

                System.out.print("Первым числом, состоящим только из чисел является: " + s + "\n");
                break;
            }
        }
    }
}