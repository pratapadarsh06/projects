// C++ implementation to create a file 
#include <bits/stdc++.h> 
using namespace std; 
int main(int argc,char *argv[]) 
{ 
char ch[20];
	// fstream is Stream class to both 
	// read and write from/to files. 
	// file is object of fstream class 
fstream file; 

// in out(write) mode 
// ios::out Open for output operations. 
file.open(argv[1],ios::out); 

// If no file is created, then file show error
if(!file) 
{ 
	cout<<"Error in creating file!!!"; 
	return 0; 
} 
cout<<"File created successfully."; 
// closing the file. 
file.close(); 

return 0; 
} 

