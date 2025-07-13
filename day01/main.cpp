#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    string s;
    int ans = 0;
    unordered_map<string, int> m{
        {"one", 1}, {"two", 2},   {"three", 3}, {"four", 4}, {"five", 5},
        {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9},
    };
    while (cin >> s) {
        int a = -1, b = -1;
        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (isdigit(c)) {
                b = c - '0';
                if (a == -1) a = c - '0';
            } else {
                for (int j = 3; j < 6; j++) {
                    if (i + j > s.length()) break;
                    string x = s.substr(i, j);
                    if (m.count(x)) {
                        b = m[x];
                        if (a == -1) a = m[x];
                    }
                }
            }
        }
        ans += a * 10 + b;
    }
    cout << ans << endl;
}