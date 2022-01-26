class a{
    int main(){
        try {
            int[] myNumbers = {1, 2, 3};
            System.out.println(myNumbers[10]);
        }
        catch (Exception e) {
            System.out.println("Something went wrong.");
         }
        catch(ArrayIndexOutOfBoundsException | ArithmeticException exp) {
             System.out.println("Warning: Enter inputs as per instructions ");
          }

   }

}