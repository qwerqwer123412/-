#include <iostream>

using namespace std;


int N;
int result[6];

bool check(int d[][2], int index, int num) {
    if (d[index][0] == num || d[index][1] == num) {
        return true;
    }
    return false;
}

void solve(int d[][2]) {
    int count = 0;

    for (int i = 1; i < 6; ++i) {
        for (int j = 0; j < N; ++j) {

            if (check(d, j, i)) {
                count++;
            } else {
                result[i] = max(result[i], count);
                count = 0;
            }
        }
        result[i] = max(result[i], count);
        count = 0;
    }
}

int findMax() {
    int max_value = result[0];
    for (int i = 1; i < 6; i++) {
        max_value = max(max_value, result[i]);
    }
    return max_value;
}

int main() {

    cin >> N;
    int d[N][2];


    fill(&result[0], &result[5], 0);
    for (int i = 0; i < N; ++i) {
        int a, b;
        cin >> a >> b;
        d[i][0] = a;
        d[i][1] = b;
    }
    solve(d);

    int max_value = findMax();
    for (int i = 1; i < 6; ++i) {
        if (result[i] == max_value) {
            cout << result[i] << " " << i;
            break;
        }

    }

}