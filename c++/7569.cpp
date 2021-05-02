#include<iostream>
#include<queue>
#include<vector>
using namespace std;
#define MAX 100
int N, M, H;
int map[MAX][MAX][MAX];
int visited[MAX][MAX][MAX] = {0,};
queue<pair<int, pair<int, int>>> q;
queue<int> cnt;
int dx[6] = { 0, 1, 0, -1, 0, 0};
int dy[6] = { 1, 0, -1, 0, 0, 0 };
int dz[6] = { 0, 0, 0, 0, 1, -1 };

int bfs() {
	int cx, cy, cz;
	pair<int, pair<int, int>> tmp;

	
	int answer = -1;
	while (!q.empty()) {
		

		tmp = q.front(); q.pop();
		cz = tmp.first;
		cy = tmp.second.first;
		cx = tmp.second.second;
		
		int cc = cnt.front();cnt.pop();
		answer = cc;
		/*cout << cz << ", " << cy << ", " << cx << ", " << endl;*/
		for (int i = 0; i < 6; i++) {
			int nx = cx + dx[i];
			int ny = cy + dy[i];
			int nz = cz + dz[i];
			if(0<=nx&&nx<M&& 0 <= ny && ny < N&& 0 <= nz && nz < H)
				if (map[nz][ny][nx] == 0 && visited[nz][ny][nx] == 0) {
					visited[nz][ny][nx] = 1;
					map[nz][ny][nx] = 1;
					q.push(make_pair(nz, make_pair(ny, nx)));
					//cout << nz << ", " << ny << ", " << nx << ", " << endl;
					cnt.push(cc + 1);
				}
		}

	//for (int k = 0; k < H; k++)
	//		for (int i = 0; i < N; i++) {
	//			for (int j = 0; j < M; j++)
	//				cout << map[k][i][j];
	//			cout << endl;
	//		}
	//	cout << endl;

	}
	for (int k = 0; k < H; k++)
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++)
				if (map[k][i][j] == 0)
					return -1;
		}
	
	return answer;
}

int main() {

	cin >> M >> N >> H;

	for (int k = 0; k < H; k++)
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
			{
				cin >> map[k][i][j];
				if (map[k][i][j] == 1)
				{
					q.push(make_pair(k, make_pair(i, j)));
					visited[k][i][j] = 1;
					cnt.push(0);
				}
			}
	

	int answer = bfs();


	cout << answer << endl;

	return 0;
}