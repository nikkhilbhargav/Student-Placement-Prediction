#include <iostream>
using namespace std;

bool palindrome(string str, int i, int j) {
    // Base case: crossed pointers → palindrome
    if (i >= j) return true;

    // If mismatch → not palindrome
    if (str[i] != str[j]) return false;

    // Recursive check inward
    return palindrome(str, i + 1, j - 1);
}

int main() {
    string str;
    cin >> str;

    if (palindrome(str, 0, str.size() - 1)) {
        cout << "true";
    } else {
        cout << "false";
    }

    return 0;
}
