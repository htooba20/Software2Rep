#include<ios>
#include<iostream>
#include<vector>
#include<fstream>
#include<string>
#include<algorithm>
#include<sstream>

using namespace std;
void search_Student_ID_display(vector<vector <string> > two_dimensional_vector, string student_id);
vector<int> search_Student_ID(vector<vector <string> > two_dimensional_vector, string student_id);
int get_grade(vector<vector <string> > two_dimensional_vector, string student_id);


// read file protoype 
int main()
{

	fstream input_file; // object to write on file
						//vectors
	vector <string> data;
	vector<string> first_name;
	vector<string> last_name;
	vector<string> student_id;
	vector<string> course;
	vector<string> grade;
	vector<string> course_2;
	vector<string> grade_2;
	vector<vector<string>> main_vec;


	// filestream variables
	fstream file;
	string word, filename, filename_2;

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
		file >> word;
		grade.push_back(word);
		file >> word;
		course_2.push_back(word);
		file >> word;
		grade_2.push_back(word);

	}

	// once all the id's, names, and course numbers are pushed into their corresponding vectors. the vetors it' self are pushed into a 2d vector to make a table
	main_vec.push_back(student_id);
	main_vec.push_back(first_name);
	main_vec.push_back(last_name);
	main_vec.push_back(course);
	main_vec.push_back(grade);
	main_vec.push_back(course_2);
	main_vec.push_back(grade_2);

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
	string key = "id2";
	/* search_Student_ID(main_vec, key);*/
	/*cout << main_vec[0][0] << endl;
		cout << main_vec[0][1] << endl;
		*/


		cout << "end of test of vec" << endl;
	/*	cout << main_vec[1][5] << endl;*/
		search_Student_ID_display(main_vec, key);

		cout << "grade test" << endl;
		cout << get_grade(main_vec, key);

		
	

	system("pause");
	return 0;
}


vector<int> search_Student_ID(vector<vector <string> > two_dimensional_vector, string student_id)
{
	vector <int> rowl;
	vector<int>col;
	vector<int> temp;

	for (int row = 0; row < 1; row++)
	{
		for (int col = 0; col < two_dimensional_vector[row].size(); col++)

		{
			if (two_dimensional_vector[row][col] == student_id)
			{
				/*cout << "cordinates" << row << " " << col << endl;
				cout << two_dimensional_vector[row][col] << " ";*/

				//this loop will display the information.
				temp.push_back(row);
				temp.push_back(col);

			}

		}
	}
	
	return temp;
}

int get_grade(vector<vector <string> > two_dimensional_vector, string student_id)
{
	vector<int> cordinate = search_Student_ID(two_dimensional_vector, student_id);
	int id_cordinate = cordinate[1];
	string string_grade = two_dimensional_vector[4][id_cordinate];// row 4 becuase of location of grade

	//object fom class stringstream
	stringstream grade_transfomation(string_grade);
	//object has the value from grade and nos stream it to grade variable
	int grade = 0;
	grade_transfomation >> grade;

	return grade;

}

void search_Student_ID_display(vector<vector <string> > two_dimensional_vector, string student_id)
{
	// this function will search for an id number and display the information associated with that ID
	//the function takes in a 2d vector and a string that used as a key to find the id.
	// the following loops will transverse the vector looking for the key word.

	for (int row = 0; row < 1; row++)
	{
		for (int col = 0; col < two_dimensional_vector[row].size(); col++)

		{
			if (two_dimensional_vector[row][col] == student_id)
			{
				/*cout << "cordinates" << row << " " << col << endl;
				cout << two_dimensional_vector[row][col] << " ";*/

				//this loop will display the information.
			
				for (int i = 0; i < two_dimensional_vector.size(); i++)
				{

					cout << two_dimensional_vector[i][col] << " ";
				}
			}

		}
	}
	cout << endl;
}

