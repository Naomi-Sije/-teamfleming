public class Task1_Kibathi{
// Java program to find hamming distance
// b/w two string


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
    String name = "Mercy Kibathi";
    String email = "merciek66@gmail.com";
    String slack= "@mercykibathih";
    String twitter= "@mercykibathi1";
    String biostack = "Genomics";
	String str1 = "@mercykibathih";
	String str2 = "@mercykibathi1";

	// function call
	

	System.out.println(name + ", " + email + ", " + slack +", " + biostack + ", " + twitter + ", " + hammingDist (str1, str2));
}
}

