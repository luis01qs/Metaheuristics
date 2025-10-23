# include <bits/stdc++.h>
# include <filesystem>
# define ll long long
# define nl "\n"

using namespace std;

// The first is the weight and the second is the revenue
// First read number of elements, then the capacity of knapsack
bool comp_minimum_weight(const pair<ll, ll> &a, const pair<ll, ll> &b)
{
    return a.second < b.second; // <-- corregido: comparar por peso (segundo)
}

bool comp_maximum_revenue(const pair<ll, ll> &a, const pair<ll, ll> &b)
{
    return a.first > b.first; // <-- corregido: comparar por beneficio (primero)
}

bool comp_maximum_proportion(const pair<ll, ll> &a, const pair<ll, ll> &b)
{
    return a.first * b.second > b.first * a.second; // <-- corregido: beneficio/peso
}

pair<ll, string> calculate(ll w, vector<pair<ll, ll>> &elements, string name)
{
    if( name == "minimo peso        ") sort(elements.begin(), elements.end(), comp_minimum_weight);
    else if (name == "maximo valor       ") sort(elements.begin(), elements.end(), comp_maximum_revenue);
    else sort(elements.begin(), elements.end(), comp_maximum_proportion);

    ll res = 0;
    for(auto &[revenue, weight] : elements) // <-- corregido: first=beneficio, second=peso
    {
        if( w >= weight )
        {
            w -= weight;
            res += revenue;
        }
    }

    return {res, name};
}

vector<string> names = {"minimo peso        ", "maximo valor       ", "maxima proporcion  "};
void process(int &n, ll &w, vector<pair<ll, ll>> &elements)
{
    pair<ll, string> ans = {0ll, ""};
    for( auto &e : names )
    {
        pair<ll, string> res = calculate(w, elements, e);
        cout << res.second << " " << res.first << nl; 

        if(res.first > ans.first) ans = res;
    }

    cout << "Maximo encontrado con " << ans.second << nl << nl;
    cout << "####################################################";
    cout << nl;
}

void read_files(string folder_path)
{
    for( const auto &entry : filesystem::directory_iterator(folder_path))
    {
        if(entry.is_regular_file() && entry.path().extension() == ".txt")
        {
            string fileName = entry.path().string();
            freopen(fileName.c_str(), "r", stdin);

            int n;
            ll w;
            cin>>n>>w;

            vector<pair<ll, ll>> elements(n);
            for(auto &e:elements) cin>>e.first>>e.second;

            cout << fileName << nl;
            process(n, w, elements);

            fclose(stdin);
        }
    }
}

int main()
{
    read_files("./KP-instancias");

    return 0;
}

