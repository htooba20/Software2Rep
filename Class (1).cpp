#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

struct Student {
	string name;
	double gpa;
	int id;
	Student *next;
};



int main()
{
	string user;
	cout << " Are you a student or Admin ? "; 
	getline(cin, user); 
	string student;
	string admin;
	string name;
	int Password;
	int ID;
	int ADPASS;
	int Pos = 123;

	if (user == student)
	{
		cout << " Enter your name " << endl;
		getline(cin, name);
		cout << " Now enter your Password " << endl;
		// Password is ID
		cin >> Password;
			if (Password == ID) 
		{  

				// call function to display info
				cout << " Would you like to exit ? " << endl;
				char Ans; 
				cin >> Ans;
				if (Ans == 'Y' || Ans == 'y')
				{
					// Call function to terminate 
				}
		}
		


	}
	if (user == admin)
	{
		cout << " Enter Your Password" << endl; 
		cin >> ADPASS;

		if (ADPASS = Pos)
		{
			// call function to display info

			cout << " Would you like to exit or change ? " << endl;
			char answ;
			cin >> answ);
			if ( answ = 'Exit' )
				//call function to terminate 
			if (answ = 'Cha')
				//call function to change


		}


	}
	
}
