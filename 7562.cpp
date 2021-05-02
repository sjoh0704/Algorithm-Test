#include<iostream>
#include<queue>
#include<vector>
#define MAX 300
using namespace std;

int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int dy[8] = {-2, -1, 1, 2, 2, 1, -1, -2};

int solution() {
	int visited[MAX][MAX] = { 0 };
	int minimum_cnt = 10000000;
	int N, cx, cy, cc;
	pair<int, int> start, end;
	queue<pair<int, int>> q;
	queue<int> cnt;
	
	cin >> N;
	cin >> start.first >> start.second;
	cin >> end.first >> end.second;
	
	visited[start.second][start.first] = 1;
	q.push(make_pair(start.first, start.second));
	cnt.push(0);

	while (!q.empty()) {

		pair<int, int> tmp = q.front();
		q.pop();
		cx = tmp.first;
		cy = tmp.second;
		cc = cnt.front();
		cnt.pop();
	
		if (minimum_cnt < cc)
			continue;

		if (cx == end.first && cy == end.second) 
			if (minimum_cnt > cc) 
				minimum_cnt = cc;
		
		for (int i = 0; i < 8; i++) {
			int nx = cx + dx[i];
			int ny = cy + dy[i];
			if (0 <= nx && nx < N && 0 <= ny && ny < N) 
				if (visited[ny][nx]==0) {
					visited[ny][nx] = 1;
					q.push(make_pair(nx, ny));
					cnt.push(cc + 1);
			}

		}
		


	}	
	return minimum_cnt;
}

int main() {
	vector<int> answer;
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
		answer.push_back(solution());

	for (int i = 0; i < answer.size(); i++)
		cout << answer[i] << endl;

	return 0;
}