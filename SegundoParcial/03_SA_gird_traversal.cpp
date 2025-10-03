# include <bits/stdc++.h>
# define ll long long
# define nl '\n'

using namespace std;

const int INF = 1e9;

float T = 100;
float alpha = 0.95;
int n, m, res, res_pos_x, res_pos_y;
vector<vector<int>> grid;
vector<vector<bool>> vis;

// UDRL
vector<pair<int, int>> mov = {{1, 0},{-1, 0},{0, 1},{0, -1}};

// Corners
//vector<pair<int, int>> mov = {{1, 1},{-1, 1},{1, -1},{-1, -1}};

// 8
//vector<pair<int, int>> mov = {{1, 0},{-1, 0},{0, 1},{0, -1},{1, 1},{-1, 1},{1, -1},{-1, -1}};

// Around
//vector<paIir<int, int>> mov = {{1, 0},{-1, 0},{0, 1},{0, -1},{1, 1},{-1, 1},{1, -1},{-1, -1},{2, 0},{-2, 0},{0, 2},{0,-2}};

bool inside(int x, int y)
{
    return (x >= 0 && x < n && y >= 0 && y < m);
}

void path(int x, int y)
{
    if(T < 0.01) return;

    vis[x][y] = true;

    if(res > grid[x][y])
    {
        res = grid[x][y];
        res_pos_x = x;
        res_pos_y = y;
    }

    
    int next = -1;
    int actual = INF;
    for(int i=0;i<mov.size();++i)
    {
        pair<int, int> e = mov[i];
        if(inside(x + e.first, y + e.second) && !vis[x + e.first][y + e.second])
        {
            if(grid[x + e.first][y + e.second] < actual)
            {
                next = i;
                actual = grid[x + e.first][y + e.second];
            }
        }
    }

    if(actual < grid[x][y])
    {
        T *= alpha;
        path(x + mov[next].first, y + mov[next].second);
    }

    float random = (rand())/float(RAND_MAX);
    if(random < exp((grid[x][y] - actual) / T))
    {
        T *= alpha;
        path(x + mov[next].first, y + mov[next].second);
    }

    T *= alpha;
    path(x, y);
}

void read()
{
    cin>>n>>m;
    grid.resize(n, vector<int>(m, 0));
    vis.resize(n, vector<bool>(m, 0));
    for(auto &e:grid) for(auto &u:e) cin>>u;
}

int main()
{
    freopen("input.txt", "r", stdin);
    read();
    srand(time(NULL));
    int x = 5;
    int y = 5;

    res = INF;
    res_pos_x = -1;
    res_pos_y = -1;
    path(x, y);

    cout << "From the initial position of (" << x+1 << "," << y+1 << ") we got the best solution:" << endl;
    cout << "Answer: " << res << " in position (" << res_pos_x+1 << "," << res_pos_y+1 << ")." << endl;

    return 0;
}
