/**
 * 2_Functions.cpp
 *
 * Author: Justin Petluk
 * Date: May 8, 2020
 */

#include<iostream>

#include"3_functions_and_Classes.h"
#include<ctime>

using namespace std;


// In C++ when functions are defined, they must be defined 
// This is called a header. These headers can be defined in a single line
// and in a new file. I find headers are an exelent way to plan out your classes!

// The type before the function is the type that is going to be returned from the function

//You can create a header function called a prototype:
int add(int, int); //You can define a function that takes in nameless variables

//or you can define the names of the variables being passed in
int subtract(int num_1, int num_2);

//you can also add default values!
double divide(int numerator, int denomonator=1); //notice we pass in integers, but it should return a float/double

//Note that typically you define headers in a header file. This is really good for defining classes!
//Please check out the header file!!! (.h)
//we still must define the say_hello from the .h which will happen here
void say_hello(){
    std::cout<<"HELLO!";
}

//normally a class will have it's own dedicated .cc or .cpp section.
//but for now, this little section will act as if there is

void hm_random::set_seed(double value){
    this->seed = value; //this accesses the class's variable.
}
double hm_random::get_seed(){
    return this->seed;
}

int hm_random::psudo_random(int new_seed=0){ //NOTE that we can define defualt values here! We use 0, which often defaults to 0
    /* Here we will define a Linear Congrunetial Generator whcih generates a random integer number. 
     * The equation follows :
     */
    int temp_seed = 42;
    int var = 0;

    if (new_seed == 0){
        temp_seed = this -> seed;
    }
    else{
        temp_seed = new_seed;
    }
    temp_seed = (420 * temp_seed + 93) % 92;

    return temp_seed; // a REALLY big number
}

// once these prototypes are defined, you can access them anywhere after they are defined.
// Imagine them like global variables. 
// but these prototypes must be defined if you want to do this. 
// If you do not prototype, the functions are defined and can only be called in order.
// so if add was defined and written as a complete function before subtract,
// subtract could call add, but add could not call subtract.

//now we can define the functions! we can now define the names of the integer variables
int add(int num_1, int num_2){
    return num_1 + num_2;
}

int subtract(int num_1, int num_2){
    return num_1 - num_2;
}

double divide(int numerator, int denomonator){ // If we defined the names before, they must be the same
    return numerator / denomonator;
}



int main(){

    double result; //we will use this as a temperary variable across all those functions

    result = add(1,2); //note that doubles can contain integers
    //but when doubles are converted to integers, the floating point is lost and not rounded
    //for example stoi(3.1415) -> 3 (string to int)
    std::cout<<"Add: "<<result<<'\n';

    result = subtract(result, 5);
    std::cout<<"Subtract: "<<result<<'\n';

    result = divide(5,2);
    std::cout<<"Divide: "<<result<<'\n';

    hm_random random = hm_random();

    int random_number = random.psudo_random();
    std::cout<<"First Test: "<<random_number<<'\n';

    random_number = random.psudo_random(12345);
    std::cout<<"First Seed: "<<random_number<<'\n';

    //Let's feed the random number into the random number!
    std::cout<<"First random in random: "<<random_number<<'\n';
    random_number = random.psudo_random(random_number);
    std::cout<<random_number<<'\n';


    std::cout<<"\nFirst 20 random with random feeding into itself\n";
    for (int i = 0; i < 20; i++){
        random_number = random.psudo_random(random_number);
        std::cout<<random_number<<", ";
    }

    //notice how the numbers repeat? this is the whole problem with psudo random numbers...
    // Its random, generally until we see a pattern. We just use very large numbers and a long
    // sequence in order to make it seem random, "psudo random"
    
    //often, time is used because the seed will never repeat itself.
    std::time_t result_time = std::time(nullptr) % 20 + 2; // we add 1 because mod is 0-19, so adding 1 leaves 1-20.
                                                           //this is because if we multiply everything by 0, we will get the
                                                           //same number for every iteration that loop (due how multiplication drives the RNG)
    //let's just add a new multiplier to our random number each iteration and see
    //with this, we will see the same number over and over again, every time we execute.
    std::cout<<"\nRandom with time and iteration\n";
    for (int i = 1; i < 10; i++){
        random_number = random.psudo_random(result_time+i*random_number);
        std::cout<<random_number<<", ";
    }

    //let's make a very large random number!
    std::cout<<"\nVery Large random number!\n";
    for (int i = 1; i <= random_number; i += i){ //notice increment does not have to be + 1!
        random_number *= random.psudo_random(result_time + i);
    }
    std::cout<<random_number*-1; //Tbh I don't know why it results in negative... that's your job to figure out lol
    
}