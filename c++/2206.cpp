#include<iostream>
#include<queue>
#include<vector>
#define MAX 1001
using namespace std;
int N;
int M;
int map[MAX][MAX];
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1};
int min_distance = 1000000;
void bfs() {
	bool visited[MAX][MAX] = { false };
	queue<pair<int, pair<int, int>>> q;
	
	q.push(make_pair(1, make_pair(1, 1)));
	
	visited[1][1] = true;
	while (!q.empty()) {
		pair<int, pair<int, int>> tmp = q.front();
		q.pop();
		int cy = tmp.first;
		int cx = tmp.second.first;
		int cc = tmp.second.second;

	/*	cout << cy << " " << cx << endl;*/
		if (min_distance <= cc)
			return;

		if (cy == N && cx == M) {
			if (min_distance > cc)
				min_distance = cc;
		}


		for (int i = 0; i < 4; i++) {
			int ny = cy + dy[i];
			int nx = cx + dx[i];
			if(1<=nx&&nx<=M && 1<=ny&&ny<=N)
				if (!visited[ny][nx]&&map[ny][nx]==0) {

					visited[ny][nx] = true;
					q.push(make_pair(ny, make_pair(nx, cc+1)));
					
				}
		}



	}

}
int main() {


	cin >> N >> M;
	char tmp;
	vector<pair<int, int>> num1;

	for(int i = 1; i<=N;i++)
		for (int j = 1; j <= M;j++) {
			cin >> tmp;
			map[i][j] = int(tmp) - 48;
			if (map[i][j] == 1)
				num1.push_back(make_pair(i, j));
		}

	/*for (int i = 1; i <= N;i++){
		for (int j = 1; j <= M;j++)
			cout << map[i][j];
			cout << endl;
		}*/

	for(int n =0; n<num1.size(); n++)
	{
		int i = num1[n].first;
		int j = num1[n].second;
		map[i][j] = 0;
		bfs();
		map[i][j] = 1;
	}
	if (min_distance == 1000000)
		cout << -1 << endl;
	else
		cout<< min_distance<<endl;
	

	return 0;
}