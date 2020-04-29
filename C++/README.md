# Lessons
How to install:
For Windows:
	http://www.mingw.org/wiki/Getting_Started
You should follow the instructions. Performa basic install, default packages and such sould be fine.

Mac: 
	xcode-select --install

Linux:
	sudo apt update
	sudo apt install build-essential

These should provide you with the commands neccesary to compile c++. We will be using g++ to compile our programs. This link explains it nicely.
https://www.freelancinggig.com/blog/2017/11/10/difference-gcc-g/


If it works, you should type g++ and it should say there's no input file...

g++ 1_Hello_World.cpp -o HelloWorld

So to run the executable, just type: ./HelloWorld.exe or just ./HelloWorld