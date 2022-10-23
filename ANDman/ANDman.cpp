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

typedef pair<int,int> ii;

mt19937 rng;

const int MOD = 1e9+7;
int n, q, idx;
vector<int> w, ord, lf, rg;
vector<vector<int>> adj, pos;

int mul(int &a, int b) {
  a %= MOD, b %= MOD;
  a = (a*b)%MOD;
  return a;
}

int expo(int a, int b) {
  if (b == 0) return 1;
  int tmp = expo(a,b/2);
  tmp = mul(tmp,tmp);
  return (b&1 ? mul(tmp,a) : tmp);
}

int inv(int x) {
  return expo(x,MOD-2);
}

void dfs(int cur, int par) {
  ord.push_back(cur);
  lf[cur] = ord.size();
  for (int nx : adj[cur]) {
    if (nx == par) continue;
    dfs(nx,cur);
    ord.push_back(cur);
  }
  rg[cur] = ord.size();
}

signed main() {
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int tc; cin >> tc;
  while (tc--) {
    cin >> n;
    w = lf = rg = vector<int>(n+2);
    pos = vector<vector<int>>(n+2);
    for (int i = 1; i <= n; i++) cin >> w[i];
    for (int i = 1; i <= n-1; i++) {
      int u, v; cin >> u >> v;
      adj[u].push_back(v);
      adj[v].push_back(u);
    }
    idx = 0; ord.clear(); dfs(1,0);
    for (auto i : ord) cout << i << ' ';
    cout << '\n';
    cin >> q;
    
  }
  return 0;
}
