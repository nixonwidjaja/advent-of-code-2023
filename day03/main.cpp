#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool is_symbol(const char c) { return c != '.' && !(c >= '0' && c <= '9'); }
bool is_star(const char c) { return c == '*'; }

void add_count(unordered_map<string, vector<int>>& count, int i, int j,
               int val) {
    if (val > 0) count[to_string(i) + ',' + to_string(j)].push_back(val);
}

int count_sum(const vector<string>& graph) {
    const int n = graph.size(), m = graph[0].size();
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int num = 0, L = m - 1, R = m - 1;
        for (int j = 0; j < m; j++) {
            if (graph[i][j] >= '0' && graph[i][j] <= '9') {
                num = num * 10 + graph[i][j] - '0';
                L = min(L, j);
            } else {
                R = j;

                bool can = false;
                if (L > 0 && is_symbol(graph[i][L - 1])) can = true;
                if (R < m && is_symbol(graph[i][R])) can = true;
                if (!can && i > 0) {
                    for (int k = max(L - 1, 0); k <= R; k++) {
                        if (is_symbol(graph[i - 1][k])) can = true;
                    }
                }
                if (!can && i < n - 1) {
                    for (int k = max(L - 1, 0); k <= R; k++) {
                        if (is_symbol(graph[i + 1][k])) can = true;
                    }
                }
                if (can && num > 0) {
                    ans += num;
                }
                L = m - 1;
                num = 0;
            }
        }
    }
    return ans;
}

int count_gear(const vector<string>& graph) {
    const int n = graph.size(), m = graph[0].size();
    unordered_map<string, vector<int>> count;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        int num = 0, L = m - 1, R = m - 1;
        for (int j = 0; j < m; j++) {
            if (graph[i][j] >= '0' && graph[i][j] <= '9') {
                num = num * 10 + graph[i][j] - '0';
                L = min(L, j);
            } else {
                R = j;

                bool can = false;
                if (L > 0 && is_star(graph[i][L - 1]))
                    add_count(count, i, L - 1, num);
                if (R < m && is_star(graph[i][R])) add_count(count, i, R, num);
                if (!can && i > 0) {
                    for (int k = max(L - 1, 0); k <= R; k++) {
                        if (is_star(graph[i - 1][k]))
                            add_count(count, i - 1, k, num);
                    }
                }
                if (!can && i < n - 1) {
                    for (int k = max(L - 1, 0); k <= R; k++) {
                        if (is_star(graph[i + 1][k]))
                            add_count(count, i + 1, k, num);
                    }
                }
                L = m - 1;
                num = 0;
            }
        }
    }
    for (const auto& [k, v] : count) {
        if (v.size() == 2) {
            ans += v[0] * v[1];
        }
    }
    return ans;
}

int main() {
    string s;
    vector<string> graph;
    while (cin >> s) {
        graph.push_back(s + '.');
    }
    cout << count_gear(graph) << endl;
}
