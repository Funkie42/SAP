package naiveSolution;

import java.io.*;
import java.util.Scanner;



public class LeseDateiEin {

	public static void main(String[] args) throws IOException { 
		// read data from file
		File inputData = new File("ueb1/u01puzzle-small1.txt");
		
		BufferedReader buffInput = new BufferedReader(new FileReader(inputData));
		
		int st;
		
		// init Gamegrid
		int[][] data = {{},{}}; 
		int gameLines = 0;
		int gameRows = 0;
		
		// Read inputdata
		int i = 0;
		int j = 0;
		while ((st = buffInput.read()) != -1) {
			
			st = st;
			
			//Read lenght and width of game
			if(i==0 && j==0) gameLines = st;
			if(i==0 && j==2){
				gameRows = st;
				data = new int[gameLines][gameRows];
				
			}
			
			// "?" = 0 in the array
			if((char)st == '?') {
				data[i-1][j] = 0;
			}
			// "W" = 1 in the array
			if((char)st == 'W') {
				data[i-1][j] = 1;
			}
			// "B" = 2 in the array
			if((char)st == 'B') {
				data[i-1][j] = 2;
			}
			
			j++;
			
			// On linebreak, start at next row
			if((char)st == '\n') {
				i++;
				j = 0;
			}
		}
		System.out.println(data[1].length);
		for(int a=0; a < data.length/8; a++) {
			for(int b=0; b < data[b].length/8; b++) {
				System.out.print(data[a][b]);
			}
			System.out.println("\n");
		}
	}
	
}
