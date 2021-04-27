#include<iostream> //10:03
#include<vector>
#include<algorithm>
#define MAX 1001
using namespace std;
int area[MAX] = { 0 };
int N;
vector<pair<int, int>> column;

bool compare(pair<int, int> a,pair<int, int> b) {
	if (a.second > b.second) {
		return true;
	}
	else
		return false;
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		int tmp, tmp2;
		cin >> tmp >> tmp2;
		column.push_back(make_pair(tmp, tmp2));
		area[tmp] = tmp2;
	}
	//큰값 찾기
	sort(column.begin(), column.end(), compare);
	int large_col = column[0].first;
	int large_val = column[0].second;
  

	//정렬하기 
	sort(column.begin(), column.end());

	int start = column[0].first;
	int end = column[column.size() - 1].first;

	//좌측
	int left_max = column[0].second;
	
	for (int i = column[0].first+1; i<large_col; i++) {
		if (area[i] == 0)
			area[i] = left_max;
		else {
			if (area[i] < left_max) {
				area[i] = left_max;
			}
			else {
				left_max = area[i];

			}
		}

	}

	//우측
	int right_max = column[column.size()-1].second;

	for (int i = column[column.size()-1].first -1; i > large_col; i--) {
		if (area[i] == 0)
			area[i] = right_max;
		else {
			if (area[i] < right_max) {
				area[i] = right_max;
			}
			else {
				right_max = area[i];

			}
		}

		

	}

	int total = 0;

	for (int i = start; i <= end; i++) {
		total += area[i];

		cout << area[i] << endl;

	}
		
	cout << total;

	
	return 0;
}