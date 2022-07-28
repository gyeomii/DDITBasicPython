package day04;

public class MyRef2 {
	public static void changeString(String a) {
		a = "3";
	}
	public static void changeArr(String[] a) {
		a[0] = "3";
	}
	
	public static void main(String[] args) {
		String b = "1";
		String[] bb = {"1"};
		
		System.out.println(b);
		System.out.println(bb[0]);
		
		changeString(b);
		changeArr(bb);

		System.out.println(b);
		System.out.println(bb[0]);
	}
}
