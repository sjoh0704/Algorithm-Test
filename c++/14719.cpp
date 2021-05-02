//1110
#include<iostream>
#include<algorithm>
#define MAX 501
using namespace std;
int H, W;
int area[MAX] = { 0 };
int rain[MAX] = { 0 };
int main() {
	cin >> H >> W;
	for (int i = 1; i <= W; i++)
		cin >> area[i];
	
	int large_index = 1;
	for (int i = 2; i <= W; i++)
		if (area[large_index] < area[i])
			large_index = i;


	//¿ÞÂÊ
	int left_max = area[1];
	for (int i = 2; i < large_index; i++) {
		if (area[i] <= left_max) {
			rain[i] = left_max - area[i];
		}
		else {
			left_max = area[i];
		}
	}
	int right_max = area[W];
	for (int i = W; i > large_index; i--) {
		if (area[i] <= right_max) {
			rain[i] = right_max - area[i];
		}
		else {
			right_max = area[i];
		}
	}
	int total = 0;

	for (int i = 2; i < W; i++)
		total += rain[i];
	cout << total << endl;
	

	return 0;
}