#ifndef FUNCTIONS_AND_CLASSES
#define FUNCTIONS_AND_CLASSES
// from: https://stackoverflow.com/questions/1653958/why-are-ifndef-and-define-used-in-c-header-files
/**
"Those are called #include guards.
Once the header is included, it checks if a unique value (in this case HEADERFILE_H) is defined. Then if it's not defined, it defines it and continues to the rest of the page.
When the code is included again, the first ifndef fails, resulting in a blank file.
That prevents double declaration of any identifiers such as types, enums and static variables."
 */

//here we will see why abstracting classes into a header becomes useful.


//<string.h> is the old C header. C++ provides <string>, and then it should be referred to as std::string
#include <string>

//if you do not use namesapce, you need to define the class with classname:: before you use it.

//void is a function that does things but does not return things
void say_hello(); //this is a helper function that can be called outside of defining a class


class hm_random{ //homemade random
    
    public: //public functions and variables are defined for the user
        hm_random(){this->seed = 3.14159265;} //constructor (you create the object). You can define these 
                                              //in the .cpp or here. .cpp is better practice
        ~hm_random(){}; //destructor (only good for if you declare something on the heap (user defined veriable in memory))
        
        int psudo_random(int new_seed);//we can define this null by defualt!
                                                                                  //this gives us a case where if it is null, we ignore it
                                                                                  // or when it IS defined, we can assign it! This is better than
                                                                                  // requiring it to have a value (like the first start and end range)
        
        //lets define some setters and getters for the seed!
        // Setters and getters allow the variable to be more robust
        // through an abstraction. For more complex settings, we can 
        // account for unnasigned variables or get more complex  
        void set_seed(double);
        double get_seed();

    private: //private variables are defined to help you to acheive
             // the goal of the class with the funcitionality, but
             // hide it from the user. This is because the hidden stuff may
             // be too complex for the actual use. This is called abstraction
        double seed;


    protected:// when we get further into inheritance, protected becomes important
              /*
              https://docs.microsoft.com/en-us/cpp/cpp/protected-cpp?view=vs-2019
                "Protected can be used by the following:
                Member functions of the class that originally declared these members.
                Friends of the class that originally declared these members.
                Classes derived with public or protected access from the class that originally declared these members.
                Direct privately derived classes that also have private access to protected members."
              */
        void leave_this_for_later();


}; //<<< Don't forget to put a semicolon after a class!


#endif
