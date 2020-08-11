package my_source;

import java.util.Scanner;

public class SumOfArray {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Length of array: ");
		int num = scanner.nextInt();
		
		int[] a = new int[num];
		
		for (int i = 0; i < num; i++) {
			System.out.print("Write down number[" + i + "]: ");
			a[i] = scanner.nextInt();
		}
		
		System.out.println("The sum of array a is " + sumOf(a) + ".");

	}
	
	static int sumOf(int[] a) {
		int sum = 0;
		for (int i = 0; i < a.length; i++) {
			sum += a[i];
		}
		return sum;
	}

}
