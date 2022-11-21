#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    string description, name;
    unordered_set <string> onBuilding;

    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> description >> name;
        if (onBuilding.find(name) == onBuilding.end()) {
            if (description == "exit") {
                cout << name << " exited (ANOMALY)" << endl;
            } else {
                cout << name << " entered" << endl;
                onBuilding.insert(name);
            }
        }
        else {
            if (description == "entry") {
                cout << name << " entered (ANOMALY)" << endl;
            } else {
                cout << name << " exited" << endl;
                onBuilding.erase(name);
            }
        }
    }

    return 0;
}
