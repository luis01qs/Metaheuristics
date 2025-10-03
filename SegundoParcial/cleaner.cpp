#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    int n, m;
    cin>>n>>m;
    vector<vector<int>> a(n, vector<int>(m));
    for(int i=0;i<n;++i)
    {
        for(int j=0;j<m;++j)
        {
            cin>>a[i][j];
            if(j != m-1)
            {
                char c;
                cin>>c;
            }
        }
    }

    freopen("input.txt", "w", stdout);
    
    cout << n << " " << m << endl;
    for(auto &e:a)
    {
        for(auto &u:e) cout << u << " ";
        cout << endl;
    }
    cout << endl;

    return 0;
}
