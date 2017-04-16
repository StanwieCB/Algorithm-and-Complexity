#include <iostream>
#include <fstream>

using namespace std;

#define N 15

int edge[N][N] = { 0 };
int vis[N] = { 0 };
int post[N] = { 0 };
int con[N] = { 0 };
int cnt = 1;
int num_of_con = 1;

void DFS1(int a);
void DFS2(int a);
void reverse();
int find_max();
void show();
void output(ofstream& ofs);

void main()
{
	ifstream inFile("input.txt");
	ofstream outFile("output.txt");
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			inFile >> edge[i][j];
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cout<< edge[i][j] <<" ";
		}
		cout << endl;
	}

	for (int i = 0; i != N; ++i)
	{
		if (vis[i] == 0)
			DFS1(i);
	}
	reverse();
	while (cnt > 1)
	{
		int t = find_max();
		DFS2(t);
		num_of_con++;
	}
	show();
	output(outFile);
	system("pause");
}

void DFS1(int a)
{
	vis[a] = 1;
	for (int i = 0; i != N; ++i)
	{
		if (vis[i] == 0 && edge[a][i] == 1)
			DFS1(i);
	}
	post[a] = cnt++;
}

void DFS2(int a)
{
	con[a] = num_of_con;
	cnt--;
	for (int i = 0; i != N; ++i)
	{
		if (con[i] == 0 && edge[a][i] == 1)
		{
			DFS2(i);
		}
	}
}
void reverse()
{
	for (int i = 0; i != N; ++i)
	{
		for (int j = 0; j < i; ++j)
		{
			int t = edge[i][j];
			edge[i][j] = edge[j][i];
			edge[j][i] = t;
		}
	}
}

int find_max()
{
	int max = -1; int position = -1;
	for (int i = 0; i != N; ++i)
	{
		if (post[i] > max && con[i] == 0)
		{
			max = post[i]; 
			position = i;
		}
	}
	return position;
}

void show()
{
	for (int i = 1; i != num_of_con; ++i)
	{
		cout << "strongly connected component" << i << ":\n";
		for (int j = 0; j != N; ++j)
		{
			if (con[j] == i)
				cout << (char)(65 + j)<< " ";
		}
		cout << "\n";
	}
}

void output(ofstream& ofs)
{
	for (int i = 1; i != num_of_con; ++i)
	{
		ofs << "strongly connected component [" << i << "]:\n";
		for (int j = 0; j != N; ++j)
		{
			if (con[j] == i)
				ofs << (char)(65 + j) << " ";
		}
		ofs << "\n";
	}
}