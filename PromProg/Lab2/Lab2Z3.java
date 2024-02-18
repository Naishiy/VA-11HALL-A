import java.util.Scanner;
import java.util.Random;

public class Lab2Z3 {

    public static void main() {

        /*Создание матрицы*/
        System.out.print("\nВведите размерность матрицы: ");
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        float[][] A = new float[n][n];

        /*Заполнение матрицы*/
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = random.nextFloat() * (2 * n + 1) - n;
            }
        }
// Выводим матрицу на консоль
        System.out.println("\nМатрица A до округления:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(A[i][j] + " ");
            }
            System.out.println();
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = Math.round(A[i][j]);
            }
        }
        System.out.println("\nМатрица A после округления:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(A[i][j] + " ");
            }
            System.out.println();
        }
    }
}
