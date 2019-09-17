#include<ios>
#include<iostream>
#include<vector>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;

// read file protoype 
void main()
{

	fstream input_file; // object to write on file
	//vectors
	vector <string> data;
	vector<string> first_name;
	vector<string> last_name;
	vector<string> student_id;
	vector<string> course;
	vector<vector<string>> main_vec;


	// filestream variables
	fstream file;
	string word, filename;

	// filename of the file to read
	filename = "student_info.txt";

	// open filename ////////
	file.open(filename.c_str());

	// this while look keeps looping untill there is no more txt to read from
	while (file >> word)
	{
		// a word is read and assigned to the variable word; then it's pushed into a vector.
		//the format of the database is a 2 dimensioanl vector. the format of the grid is based on colums as follows
		// ID FIRST NAME LAST_NAME COURSE#

		student_id.push_back(word);
		file >> word;
		first_name.push_back(word);
		file >> word;
		last_name.push_back(word);
		file >> word;
		course.push_back(word);

	}

	// once all the id's, names, and course numbers are pushed into their corresponding vectors. the vetors it' self are pushed into a 2d vector to make a table
	main_vec.push_back(student_id);
	main_vec.push_back(first_name);
	main_vec.push_back(last_name);
	main_vec.push_back(course);



	/*use this code to test the vectors.....
	for (int i = 0; i < student_id.size(); i++)
	{
	cout << "|" << student_id[i] << "|" << endl;

	}*/

	//2d vector test..... use the following code to test in 2 dimensions....
	/*cout << "2d vec test" << endl;
	int main_vec_size = main_vec.size();
	cout << "main_vec size is" << main_vec_size << endl;

	for (int col = 0; col < main_vec.size(); col++)
	{
		
		for (int row = 0; row < main_vec[col].size(); row++)
		{
			cout << main_vec[col][row] << " ";
			
		}
		cout << endl;
	}*/
	

	system("pause");
	
}