#include <iostream>
#include <iomanip>
#include <stack>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <vector>
#include <utility>
#include <algorithm>
#include <numeric>
#include <string>
#include <cmath>
#include <random>
#include <sstream>
#include <string.h>
#include <assert.h>
using namespace std;

#define fi first
#define se second
#define int long long

typedef pair<int,int> li;

mt19937 rng;

const int INF = 1e15;
int b;
vector<int> m;
vector<string> res;
vector<vector<int>> val;
vector<vector<string>> name;
vector<unordered_map<int, int>> memo;

int dp(int idx, int budget) {
    if(idx > 5) return budget;
    if (memo[idx].count(budget)) return memo[idx][budget];
    int ret = INF;
    for (int i = 1; i <= m[idx]; i++){
        if (budget < val[idx][i]) continue;
        ret = min(ret,dp(idx + 1, budget - val[idx][i]));
    }
    return memo[idx][budget] = ret;
}

void bt(int idx, int budget) {
    if (idx > 5) return;
    for(int i = 1; i <= m[idx]; i++) {
        if (budget < val[idx][i]) continue;
        if (dp(idx, budget) == dp(idx + 1, budget - val[idx][i])){
            res.push_back(name[idx][i]);
            bt(idx + 1, budget - val[idx][i]);
            return;
        }
    }
}

signed main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> b;
    m = vector<int>(5 + 2);
    val = vector<vector<int>>(5 + 2);
    name = vector <vector<string>>(5 +2);
    for(int i = 1; i <= 5; i++){
        cin >> m[i];
        val[i] = vector<int>(m[i] + 2);
        name[i] = vector<string>(m[i] + 2);
        
        for(int j=1; j <= m[i]; j++){
            cin >> name[i][j] >> val[i][j];
        }
    }
    
    memo = vector<unordered_map<int, int>>(5+2);
    
    bt(1,b);
    
    for(auto i : res) cout << i << '\n';
    
    return 0;
}
