public class HelloWorld{
     public static void main(String []args){
        System.out.println("Mercy Kibathi, merciek66@gmail.com, @mercykibathih, Genomics, @mercykibathi1, hamming distance = 1");
     }
}

// Java program to find hamming distance
// b/w two string
class GFG
{
// function to calculate Hamming distance
static int hammingDist(String str1, String str2)
{
	int i = 0, count = 0;
	while (i < str1.length())
	{
		if (str1.charAt(i) != str2.charAt(i))
			count++;
		i++;
	}
	return count;
}

// Driver code
public static void main (String[] args)
{
	String str1 = "@mercykibathih";
	String str2 = "@mercykibathi1";

	// function call
	System.out.println(hammingDist (str1, str2));
}
}


