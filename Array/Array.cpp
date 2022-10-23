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
#include <string.h>
#include <assert.h>
using namespace std;

#define fi first
#define se second
#define int long long

typedef pair<int,int> ii;

mt19937 rng;

const int MOD = 1e9+7;
int n, m, p;
vector<vector<ii>> lst;

struct BIT {
  vector<int> a, bit;

  BIT(int n) {
    a = bit = vector<int>(n+2);
  }

  void update(int x, int val) {
    for (int i = x; i <= n; i += i&-i) bit[i] += val-a[x];
    a[x] = val;
  }

  int query(int l, int r) {
    int ret = 0;
    for (int i = r; i; i -= i&-i) ret += bit[i];
    for (int i = l-1; i; i -= i&-i) ret -= bit[i];
    return ret;
  }
};

signed main() {
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  cin >> n >> m >> p;
  // lst = vector<vector<ii>>(n+2);
  for (int i = 1; i <= m; i++) {
    int l, r, k; cin >> l >> r >> k;
    // lst[r].push_back({l,k});
  }
  for (int i = 1; i <= n; i++) cout << "0 ";
  cout << '\n';
  // auto sum = BIT(n);
  // for (int rg = 1; rg <= n; rg++) {
  //   sort(lst[rg].rbegin(),lst[rg].rend());
  //   for (auto [lf,sum] : lst[rg]) {
  //     int curSum = sum.query(lf,rg);
      
  //   }
  // }
  return 0;
}

int p = 7
[2 3] = 3
0 0 3 0 0

p = 19
[2 7] = 15
[5 19] = 0
[3 6] = 1
[6 9] = 1
[7 19] = 17
0 0 0 0 0 0 15 0 0 0 0 0 0 0 0 0 0 0 4 0 
