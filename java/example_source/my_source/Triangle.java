package my_source;

import java.util.Scanner;

public class Triangle {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		int n;

		System.out.println("왼쪽 위가 직각인 삼각형을 출력함.");

		do {
			System.out.print("삼각형 단의 갯수: ");
			n = stdIn.nextInt();
		} while (n <= 0);

		for (int i = 1; i <= n; i++) {
			for (int j = n - i + 1; j > 0; j--) {
				System.out.print('*');
			}
			System.out.println();
		}
		stdIn.close();
	}
}