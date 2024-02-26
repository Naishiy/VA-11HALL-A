import java.util.Scanner;

public class Lab2Z1 {

    public static void main() {

        /*Ввод чисел*/
        System.out.print("Введите несколько чисел: ");
        Scanner in = new Scanner(System.in);
        String line = in.nextLine();
        String[] numbers = line.split(" ");

        /*Считывание отдельных чисел*/
        for (String s: numbers) {

            boolean isNumber = s.matches("\\d+");
            /*Проверка состоит ли следующий после пробела набор символов из цифр*/
            if (isNumber) {

                /*Строка для проверки на повторяющиеся цифры*/
                String duplicanty = new String();

                /*Счетчик повторений цифр в числе*/
                boolean flag = true;

                /*Проверка состоит ли следующий после пробела набор символов из разных цифр*/
                for (String ch : s.split("")) {

                    /*Проверка на повторное содержание символа в числе*/
                    if (duplicanty.contains(ch)) {
                        flag = false;
                        break;
                    }

                    duplicanty += ch;
                }

                /*Вывод первого числа, состоящего только из различных цифр*/
                if (flag) {

                    System.out.print("Первым числом, состоящим только из различных цифр является: " + s + "\n");
                    break;
                }
            }
        }
    }
}
