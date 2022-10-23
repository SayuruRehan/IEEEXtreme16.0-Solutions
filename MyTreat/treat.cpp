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

const int N = 1e4;
int n, m;
vector<int> inDeg, outDeg, dsu, debt, good;
vector<ii> edges;
vector<vector<string>> tmp;
unordered_map<string,int> idx;

int find(int x) {
  if (dsu[x] == x) return x;
  return dsu[x] = find(dsu[x]);
}

void merge(int a, int b) {
  a = find(a); b = find(b);
  if (a == b) return;
  dsu[b] = a;
  debt[a] += debt[b];
  good[a] += good[b];
}

int getIdx(string s) {
  if (!idx.count(s)) idx[s] = ++n;
  return idx[s];
}

signed main() {
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int tc; cin >> tc;
  while (tc--) {
    cin >> m;
    inDeg = outDeg = vector<int>(N+2);
    tmp = vector<vector<string>>(N+2);
    n = 0; idx.clear(); edges.clear();
    for (int i = 1; i <= m; i++) {
      string name; cin >> name;
      int deg; cin >> deg;
      int u = getIdx(name);
      for (int j = 1; j <= deg; j++) {
        string s; cin >> s;
        int v = getIdx(s);
        inDeg[v]++; outDeg[u]++;
        edges.push_back({u,v});
      }
    }
    dsu = debt = good = vector<int>(N+2);
    for (int i = 1; i <= n; i++) {
      dsu[i] = i;
      debt[i] = max((int)0,inDeg[i]-outDeg[i]);
      good[i] = (debt[i] == 0);
    }
    for (auto [u,v] : edges) merge(u,v);
    set<int> roots;
    for (int i = 1; i <= n; i++) roots.insert(find(i));
    int numOfEdges = 0, numOfDays = 0;
    for (int i : roots) {
      numOfEdges += debt[i];
      numOfDays = max(numOfDays, (debt[i]+good[i]-1)/good[i]);
    }
    cout << numOfEdges << " " << numOfDays << '\n';
  }
  return 0;
}
