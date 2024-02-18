import java.util.Scanner;

public class Lab2Z2 {

    public static void main() {

        /*Считывание двоичного числа и задание переменных для цикла*/
        System.out.print("\nВведите двоичное число: ");
        Scanner in = new Scanner(System.in);
        String line = in.nextLine();
        char[] number = line.toCharArray();

        int res = 0;
        int digit = 1;

        /*Прогонка всего двоичного числа, если встретилась "1", то сложение результата со значением соответствующим разряду*/
        for (int i = line.length() - 1; i >=0; i--){

            if (number[i] == '1') {

                res += digit;
            }
            digit *= 2;
        }

        /*Вывод ответа*/
        System.out.print("Число в десятичной СС: ");
        System.out.println(res);
    }
}
