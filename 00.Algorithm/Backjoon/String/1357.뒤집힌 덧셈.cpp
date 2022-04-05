#include <iostream>
#include <string>
#include <algorithm>

int main() {
	std::string X, Y;
	int a;
	std::cin >> X >> Y;
	std::reverse(X.begin(), X.end());
	std::reverse(Y.begin(), Y.end());
	Y = std::to_string(stoi(X) + stoi(Y));
	std::reverse(Y.begin(), Y.end());

	std::cout << stoi(Y);
}