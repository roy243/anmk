class strong
{
	public static void main(String[] args)
	{
		for (int i = 1; i <= 5000; i++)
		{
			if (isItStrong(i))
			{			
				System.out.println(i);
			}
		}
	}
	static boolean isItStrong(int num) {
		int no = num;
		int sum = 0;
		while (no > 0) {
			int digit = no % 10;
			sum += fact(digit);
 
			no = no / 10;
		}
		return sum == num;
	}
	static int fact(int digit) {
		int f = 1;
		for (int j = digit; j > 1; j--) {
			f *= j;
		}
		return f;
	}
}
