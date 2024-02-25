import java.util.Scanner;

public class Lab2Z2 {

    public static void main() {

        Scanner in = new Scanner(System.in);
        long number;
        int start;
        int end;

        System.out.println("Начальная СС: ");
        start = Integer.parseInt(in.nextLine());

        System.out.println("Конечная СС:");
        end = in.nextInt();

        System.out.println("Введите число: ");
        number = Long.parseLong(in.nextLine(), start);

        System.out.println("Полученое число " + Long.toString(number, end));
    }
}
