/**
 * 2_Loops_and_Logic.cpp
 *
 * Author: Justin Petluk
 * Date: April 29, 2020
 */

#include<iostream>

//I'm just going to comment this out so you can see what functions are used by the standard namespace
//using namespace std;

//argc (ARGument Count)
//argv(ARGument Vector) an array of character vectors from 0 to argc-1
int main(int argc, char **argv){

    //https://en.cppreference.com/w/cpp/language/types
    int integer = 10; //default integer
    short short_integer = 32767; //max number both positive and negative 2^16
    unsigned short short_unsigned_int = 65535; //max number (only positive) 2^16
    long long_int = 2147483647; //2^32

    //Here's our decimal place numbers. float stands for floating point number
    //it's called that by how it's designed to work underneith the system. the deciaml can "float" around
    float decimal_num = 3.14159265; //2^32 
    double longer_decimal = 3.14159265359; //2^64
    long double very_long_decimal = 3.14159265358979323846; //2^128


    bool True = true;
    bool False = false;
    //please don't redefine variables inside of the same scope.
    True = 2 > 1;
    False = 1 > 2;

    //http://www.cplusplus.com/doc/tutorial/arrays/
    //a string is a string of characters in an array. We can design one!
    std::string word = "Hello";
    char letters [10]; //we can define it, without assigning it. This an array of 10 spaces
                       // with nothing inside of it. Arrays are not dynamic. Just like numpy arrays!

    letters[0] = 'a'; //normally characters are expressed with single quotes
    letters[1] = 'b';

    // let's create a for loop to finish filling the array
    // a common debate: 
    //https://stackoverflow.com/questions/24853/c-what-is-the-difference-between-i-and-i
    //First section initializes a value, second is a logic operateor and last is an increment operator
    //the second and third part execute after each cycle of the loop
    for(int i=2; i < 10; i++){
        //http://www.asciitable.com/
        //for more information on incrementing letters
        letters[i] = i+97; //because ascii 97 is 'a' we start at letter 'c' (99)
    }
    //NOTE: i doesn't exist at this point.

    //unlike python, we must define how we want to print our arrays and vectors.
    //this also to view it we must use a loop
    for(int i=0; i < 10; i++){
        //when you cout<< multiple variables, you must << again. (different datatypes cannot be within the same <<)
        std::cout<<letters[i] //this prints out a number
                 <<' ';       //this prints out a space
    }
    std::cout<<'\n'; //same as endl

    //while loops
    int loop_limit = 10;
    int counter = 0;
    while(counter < loop_limit){
        std::cout<<counter<<' '<<std::endl;
        counter += 1; //adds 1 to counter
    }
    //do while
    loop_limit = 20;
    do{
        std::cout<<counter<<' '<<std::endl;
        counter += 1; //adds 1 to counter 
    }
    while(counter < loop_limit);

    return 0;
}
