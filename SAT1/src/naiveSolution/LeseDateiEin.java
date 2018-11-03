package naiveSolution;

import java.io.*;


public class LeseDateiEin {

	public static void main(String[] args) {
		//File inputData = new File("../../ueb1/u01puzzle-small1.txt");
		File inputData = new File("/home/marius/Stuff/SAP/SAT1/ueb1/u01puzzle-small2.txt");
		BufferedReader buffInput = new BufferedReader(new FileReader(inputData));
		
		String st;
		
		while ((st = buffInput.readLine()) != null) {
			System.out.println(st);
		}
	
	}
	
}
