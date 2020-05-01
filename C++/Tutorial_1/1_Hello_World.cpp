/**
 * Hello_World.cpp
 *
 * Author: Justin Petluk
 * Date: April 29, 2020
 */
/*MULTI 
LINE 
COMMENT*/
// SINGLE LINE COMMENT

#include <iostream> //This includes input/output stream.
                    //It's used for files and printing.

using namespace std; //we use the standard namespace.
                     // a namespace is a SCOPE for where things exist.

//Every program must have a main function. This function is the core
//of where everything meets and is executed in a program. We'll explain functions later.
int main() {
    //cout is a c++ function that prints (out) to the terminal
    cout << "Hello, World!\n"; // We must end every line with a semicolon ;
    cout << "Hello World 2! \n";

    string hello = "Hello World\n"; //Here we assign a string type to variable hello
    cout << hello; // Prints Hello World.

    bool input; //Let's define a variable. 
                //We must state what type it is so the compiler can allocate memory for it.
    
    cout << "Please Enter 0 or 1.\n";

    cin >> input; // Here we use cin similarly to cout, but assign a variable using cin and user input. C input.

    cout << std::boolalpha << input; //User must provide an appropriate input. It should be a boolean.
    // Just a note (I just found out, bool alpha just displays it as 'true' or 'false', otherwise it just prints 0 or 1)

    cout << "\nNotice 1 is true, and 0 is false";

   return 0; // That same logic is why we return 0. 
             //This means that main exits succesfully! It returns no errors! It's false!
}

/*
Ok, I'm keeping this simple to show how this can compile, so we can get onto more fun stuff later.
To compile the code, you must do what the README.md in the C++/ directory says.

if it works, you should type g++ and it should say there's no input file...
So let's give it an input file!!!

g++ 1_Hello_World.cpp -o HelloWorld
-o means Output, it specifies the name of the executable we create!

So to run the executable, just type: ./HelloWorld.exe or just ./HelloWorld
(or double click it in the file manager.)

Congrats! You just compiled and executed your first c++ program!
Let's get going on some more cool things!
*/