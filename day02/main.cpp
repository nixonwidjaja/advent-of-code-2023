#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    string line;
    int ans = 0, count = 1;
    while (getline(cin, line)) {
        istringstream iss(line);
        string s, t;
        int b = 0, g = 0, r = 0, add = count;
        while (iss >> s >> t) {
            if (t.find(':') != string::npos) {
                continue;
            } else if (t.find(',') != string::npos) {
                int x = stoi(s);
                if (t == "blue,") {
                    b = max(b, x);
                } else if (t == "green,") {
                    g = max(g, x);
                } else {
                    r = max(r, x);
                }
            } else {
                int x = stoi(s);
                if (t.find("blue") != string::npos) {
                    b = max(b, x);
                } else if (t.find("green") != string::npos) {
                    g = max(g, x);
                } else {
                    r = max(r, x);
                }
            }
        }
        ans += b * g * r;
    }
    cout << ans << endl;
}