#include<iostream>
#define MAX 100
using namespace std;
int N;
char area[MAX][MAX];
bool visited[MAX][MAX];
bool visited2[MAX][MAX];
int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, 1, -1};
void dfs(int y, int x, char target) {
	if (visited[y][x])
		return;

	visited[y][x] = true;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (0 <= nx && nx < N && 0 <= ny && ny < N && area[ny][nx]==target) 
			dfs(ny, nx, target);
	}
}
void dfs2(int y, int x, char target) {
	if (visited2[y][x])
		return;

	visited2[y][x] = true;
	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (0 <= nx && nx < N && 0 <= ny && ny < N) {
			if (target == 'B' && 'B' == area[ny][nx])
				dfs2(ny, nx, 'B');
			else if ((target == 'R'||target == 'G') && ('G' == area[ny][nx] || 'R' == area[ny][nx])) {
				dfs2(ny, nx, 'G');
				dfs2(ny, nx, 'R');
			}
		}
	}
}
int main() {
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N;j++)
			cin >> area[i][j];

	int normal_cnt = 0;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N;j++)
			if (!visited[i][j]) {
				dfs(i, j, area[i][j]);
				normal_cnt++;
			}

	cout << normal_cnt<<" ";


	int innormal_cnt = 0;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N;j++)
			if (!visited2[i][j]) {
				dfs2(i, j, area[i][j]);
				innormal_cnt++;
			}

	cout << innormal_cnt;

	return 0;
}