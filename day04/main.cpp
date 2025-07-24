#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    string line;
    ll ans = 0;
    vector<int> v(193, 1);
    int idx = 0;
    while (getline(cin, line)) {
        istringstream iss(line);
        string s;
        bool pass = false;
        unordered_set<int> sett;
        ll count = 0;
        while (iss >> s) {
            if (s == "Card" || s.back() == ':') {
                continue;
            }
            if (s == "|") {
                pass = true;
                continue;
            }
            int x = stoi(s);
            if (!pass) {
                sett.insert(x);
            } else if (sett.count(x)) {
                count++;
            }
        }
        for (int i = idx + 1; i < idx + 1 + count; i++) v[i] += v[idx];
        idx++;
    }
    for (int i = 0; i < idx; i++) ans += v[i];
    cout << ans << endl;
}