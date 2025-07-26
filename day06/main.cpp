#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    string time, dist;
    getline(cin, time);
    getline(cin, dist);
    istringstream iss_time(time), iss_dist(dist);
    string t, d, tt = "", dd = "";
    int ans = 0;
    while (iss_time >> t && iss_dist >> d) {
        if (t == "Time:") continue;
        tt += t;
        dd += d;
    }
    ll t_int = stoll(tt), d_int = stoll(dd);
    for (ll i = 1; i < t_int; i++) {
        if (d_int < i * (t_int - i)) {
            ans++;
        }
    }
    cout << ans << endl;
}