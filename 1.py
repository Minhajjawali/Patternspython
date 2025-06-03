//code for lecture 5-patterns (I) and patterns (II)
//import java.util.Scanner;
//public class patterns5{
    // public static void main(String[] args) {
    //     Scanner sc =new Scanner(System.in);

   // 1.STAR PATTERN(nested loops)
//     for(int line=1; line<=4;line++){
//         for(int star=1; star<=line;star++){
//             System.out.print("*");
//         }
//         System.out.prinoutscmamityln();

}







    //2.inverted star pattern
//     int n=4 ;
//      for(int line=1; line<=4;line++){
//         for(int star=1; star<=n-line+1;star++){
//             System.out.print("*");
//         }
//         System.out.println();

// }


//3.half pyramid number pattern
// for(int line=1; line<=4;line++){    // for numbner of lines
//     for(int num=1;num<=line;num++){    // for the characters in each line
//         System.out.print(num);         // printing the characers
//     }
//     System.out.println();
// }


//4.inverted pyramid number pattern
// int n=4;
// for(int line=1; line<=4;line++){
//     for(int num=1;num<=n-line+1;num++){
//         System.out.print(num);
//     }
//     System.out.println();
// }


//5.character pattern
// char chr='A';  
// for(int line=1; line<=4;line++){  //outer loop
//     for(int innerline=1;innerline<=line;innerline++){ //inner loop
//         System.out.print(chr);
//         chr++;

//     }
//     System.out.println();
// }


//6.inverted character pattern
// int j=4;    
// char chr='A';  
// for(int line=1; line<=4;line++){  //outer loop
//     for(int ch=1;ch<=j-line+1;ch++){ //inner loop
//         System.out.print(chr);
//         chr++;

//     }
//     System.out.println();
// }



//PATTERNS (II)
//7.print hollow rectangle pattern
// public static void hollowrect(int torows, int tocolumns){
//         //outer loop
//     for(int i=1; i<=torows; i++){
//         //inner colums
//         for(int j=1;j<=tocolumns;j++){
//             //cell-(i,j)   current position inside the rectangle grid that the program is processing.
//             // (i, j) = current cell at row i and column j.
//             if(i == 1 || i == torows || j==1 || j==tocolumns){     //first row,last row,first column,lastcolumn
//                 //condition in if statement for boundary cells
//                 System.out.print("*");
//             }else{
//                 System.out.print(" ");
//             }
//         }
//         System.out.println();
//     }

// }


// public static void main(String[] args) {
//         Scanner sc =new Scanner(System.in);
//         System.out.println("enter no .of rows");
//         int torows=sc.nextInt();
//           System.out.println("enter no .of columns");
//         int tocolumns=sc.nextInt();


//     hollowrect(torows,tocolumns);



//8.inverted and rotated half pyramid
// public static void invertrotatedhalfpyramid(int rows){
//         //outer loop
//      for(int i=1; i<=rows; i++){    //rows=lines
//         //inner loop to print the spaces
//         for(int j=1; j<=rows-i; j++){           //for first iteration rows are 4 so it will be4-1 =3 spaces 
//             System.out.print(" ");
//                 }
//         //3rd to print stars that is equal to row no. that is i
//             for(int j=1;j<=i;j++){
//                 System.out.print("*");
//             }
//             System.out.println();
//             }

// }


// public static void main(String[] args) {
//         Scanner sc =new Scanner(System.in);

//          System.out.println("enter no .of rows");
//         int rows=sc.nextInt();

//     invertrotatedhalfpyramid(rows);


//9.inverthalfpyramidnum
// public static void inverthalfpyramidnum(int n){   // n is my total lines that is 5
//         //outer loop
//      for(int i=1; i<=n; i++){  
//         for(int j=1; j<=n-i+1;j++){
//             System.out.print(j+" ");
//         }

//         System.out.println();




//      }}


// public static void main(String[] args) {
//         Scanner sc =new Scanner(System.in);

//          System.out.println("enter no .of lines or rows that is n");
//         int n=sc.nextInt();


//     inverthalfpyramidnum(n);



//10.floyds triangle   same as abcd question in pattern 1
// public static void floydstriangle(int n){   // n is my total lines that is 5
//         //outer loop
//         int counter=1;
//      for(int i=1; i<=n; i++){
//         for(int j=1;j<=i;j++){
//             System.out.print(counter+" ");
//             counter++;
//         }
//   System.out.println();

//      }}  

// public static void main(String[] args) {
//         Scanner sc =new Scanner(System.in);
        
//          System.out.println("enter no .of lines or rows that is n");
//         int n=sc.nextInt();


//     floydstriangle(n);



//11.0-1 triangle pattern
// public static void zeroonetriangle(int n){    // n is my total lines that is 5
//         //outer loop
//      for(int i=1; i<=n; i++){
//         for(int j=1;j<=i;j++){
//             if((i+j)%2 == 0){     // if the sum of (i+j == even than print 1 )
//                 System.out.print(1);
//             }else{
//                 System.out.print(0);
//             }
//         }
//         System.out.println();

//      }}



// public static void main(String[] args) {
//         Scanner sc =new Scanner(System.in);
        
//          System.out.println("enter no .of lines or rows that is n");
//         int n=sc.nextInt();

//         zeroonetriangle(n);

//12.butterfly pattern
// public static void butterfly(int n){   // for n=4
//         //outer loop
//      for(int i=1; i<=n; i++){
//         //inner loop to print the star
//         for(int j=1;j<=i;j++){
//             System.out.print("*");
//         }
//         //inner loop to print spaces
//         for(int j=1;j<=2*(n-i);j++){
//             System.out.print(" ");
//         }
//         //inner loop to print star
//         for(int j=1;j<=i;j++){
//             System.out.print("*");
//         }
//         System.out.println();
//      }
//      //second half
//          //outer loop
//      for(int i=n; i>=1; i--){
//          //inner loop to print the star
//          for(int j=1;j<=i;j++){
//              System.out.print("*");
//          }
//          //inner loop to print spaces
//          for(int j=1;j<=2*(n-i);j++){
//              System.out.print(" ");
//          }
//          //inner loop to print star
//          for(int j=1;j<=i;j++){
//              System.out.print("*");
//          } 
//          System.out.println();
     
//       }
//       }










































// public static void main(String[] args) {
//         Scanner sc =new Scanner(System.in);
        
//          System.out.println("enter no .of lines or rows that is n");
//         int n=sc.nextInt();

//         butterfly(n);




//13.solid rhombus pattern
// public static void solidrhombus(int n){   // for n=5
//         //outer loop
//      for(int i=1; i<=n; i++){
//         //inner loop for spaces
//         for(int j=1;j<=(n-i);j++){
//             System.out.print(" ");
//         }
//         //inner loop for star printing
//         for(int j=1;j<=n;j++){
//             System.out.print("*");
//         }
//         System.out.println();

//      }}


// public static void main(String[] args) {
//         Scanner sc =new Scanner(System.in);
        
//          System.out.println("enter no .of lines or rows that is n");
//         int n=sc.nextInt();

//         solidrhombus(n);


//14.hollow rhombus
// public static void hollowrhombus(int n){   // for n=5
//         //outer loop
//      for(int i=1; i<=n; i++){
//         //inner loop for spcaes
//         for(int j=1;j<=(n-i);j++){
//             System.out.print(" ");
//         }
//         //hollow rectangle code for inner loop  to print stars
       
//         for(int j=1;j<=n;j++){
//             //cell-(i,j)
//             if(i == 1 || i == n || j==1 || j==n){
//                 //condition in if statement for boundary cells
//                 System.out.print("*");
//             }else{
//                 System.out.print(" ");
//             }
//         }
//         System.out.println();
//     }


//      }
// public static void main(String[] args) {
//         Scanner sc =new Scanner(System.in);
        
//          System.out.println("enter no .of lines or rows that is n");
//         int n=sc.nextInt();

//         hollowrhombus(n);























































































//15.diamond pattern
// public static void diamond(int n){   // for n=4
//         //outer loop
//      for(int i=1; i<=n; i++){
//         //inner loop for spaces
//         for(int j=1;j<=(n-i);j++){
//             System.out.print(" ");
//         }
//         // inner loop for star print
//         for(int j=1;j<=(2*i-1);j++){   //2i-1 represented as odd number in math
//             System.out.print("*");
//         }
//         System.out.println();

//      }
//      //second half
//        //outer loop
//      for(int i=n; i>=1; i--){
//         //inner loop for spaces
//         for(int j=1;j<=(n-i);j++){
//             System.out.print(" ");
//         }
//         // inner loop for star print
//         for(int j=1;j<=(2*i-1);j++){
//             System.out.print("*");
//         }
//         System.out.println();

//       }
//  }

























// public static void main(String[] args) {
//         Scanner sc =new Scanner(System.in);
        
//          System.out.println("enter no .of lines or rows that is n");
//         int n=sc.nextInt();

//         diamond(n);
//     }}
