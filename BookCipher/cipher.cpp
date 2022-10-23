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

int p, n, r, c;
char rule;
string xml;
vector<string> s;
unordered_map<char,ii> pos;

signed main() {
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  cin >> p >> n;
  scanf("%lld,%lld\n",&r,&c);
  cin >> rule;
  s = vector<string>(p+2);
  for (int i = 1; i <= p; i++) cin >> s[i];
  cin.ignore();
  for (int i = 1; i <= n; i++) {
    string row; getline(cin,row);
    xml += row;
  }
  bool tag = 0;
  vector<vector<char>> grid(r+2,vector<char>(c+2));
  for (int i = 0, j = 0; i < xml.length() && j < r*c; i++) {
    if (xml[i] == '<') {
      string curTag;
      while (i < xml.length() && xml[i] != '>') {
        curTag += xml[i++];
      }
    }
    else {
      int curR = j/c+1;
      int curC = j%c+1;
      grid[curR][curC] = xml[i];
      j++;
    }
  }
  for (int i = 1; i <= r; i++) {
    for (int j = 1; j <= c; j++) {
      if (rule == 'S' && pos.count(grid[i][j])) continue;
      pos[grid[i][j]] = {i,j};
    }
  }
  for (int i = 1; i <= p; i++) {
    string res;
    bool good = 1;
    for (int j = 0; j < s[i].length(); j++) {
      if (!pos.count(s[i][j])) {
        good = 0;
        break;
      }
      if (j) res += ",";
      auto [row,col] = pos[s[i][j]];
      res += to_string(row)+","+to_string(col);
    }
    if (good) cout << res << '\n';
    else cout << "0\n";
  }
  return 0;
}
