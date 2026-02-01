import java.util.Scanner;

class Reverse {
    String s;

    // Constructor with default value
    Reverse(String s) {
        this.s = s;
    }

    // Method to return reversed string
    String getReverse() {
        String reversed = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            reversed += s.charAt(i);
        }
        return reversed;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Take input from user
        System.out.print("Enter a string: ");
        String input = sc.nextLine();

        // Create obje
