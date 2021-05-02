#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#define MAX 1001
using namespace std;
int area[MAX][MAX] = { 0 };
bool makeSquare(pair<int, int> start, pair<int, int> next, double& distance) {
	int distx = abs(start.first - next.first);
	int disty = abs(start.second - next.second);
	int dx[3] = { distx, disty, -distx };
	int dy[3] = { -disty, distx, disty };
	int nx = start.first;
	int ny = start.second;
	for (int i = 0; i < 3; i++) {

		nx += dx[i];
		ny += dy[i];
		if (0 <= nx && nx < MAX && 0 <= ny && ny < MAX) {
			if (area[ny][nx] != 1)
				return false;
		}
		else {
			return false;
		}

	}

	distance = sqrt(distx * distx + disty * disty);
	return true;
}
int main() {

	vector<pair<int, int>> pairs;
	int N;
	scanf("%d", &N);
	int a, b;
	for (int i = 0; i < N; i++) {
		scanf("%d %d", &a, &b);
		area[b][a] = 1;
		pairs.push_back(make_pair(a, b));
	}
	double max_distance = 0;
	for(int i =0; i<N;i++)
		for (int j = 0; j < N; j++) {
			double distance;
			if (makeSquare(pairs[i], pairs[j], distance))
				if (max_distance < distance)
					max_distance = distance;
		}
	printf("%.2f", max_distance * max_distance);


}