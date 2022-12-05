#include <iostream>
#include <algorithm>

using namespace std;

bool checkArithmetic(int arr[], int arrSize) {
    bool isArithmetic = true;
    int firstDifference = arr[1] - arr[0];
    for (int i=0; i<arrSize-1; i++) {
            if (arr[i+1] - arr[i] != firstDifference) {
                isArithmetic = false;
                break;
        }
    }
    return isArithmetic;
}

int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        int m, firstDifference;
        bool isArithmetic, isSorted;
        cin >> m;
        int sequence[m];
        for (int j=0; j<m; j++) {
            cin >> sequence[j];
        }

        isArithmetic = checkArithmetic(sequence, m);
        if (isArithmetic) {
            cout << "arithmetic" << endl;
        } else {
            int sequenceSorted[m];
            copy(sequence, sequence+m, sequenceSorted);
            sort(sequenceSorted, sequenceSorted + m);
            isArithmetic = checkArithmetic(sequenceSorted, m);
            if (isArithmetic) {
                cout << "permuted arithmetic" << endl;
            }
            else {
                cout << "non-arithmetic" << endl;
            }
        }
    }

    return 0;
}
