package my_source;

import java.util.Scanner;

public class MaxOfArray {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("---Get the max of heights---");
		System.out.print("Number of people: ");
		int num = scanner.nextInt();
		
		int[] height = new int[num];
		
		for (int i = 0; i < num; i++) {
			System.out.print("Write down your height[" + i + "]: ");
			height[i] = scanner.nextInt();
		}
		
		System.out.println("The max of height is " + maxOf(height) + ".");

	}
	
	static int maxOf(int[] a) {
		int max = a[0];
		for (int i = 0; i < a.length; i++) {
			if (a[i] > max) {
				max = a[i];
			}
		}
		return max;
	}

}
