#include <iostream>
#include <vector>

int averageValue(const std::vector<int>& nums) {
    if (nums.size() == 0) {
        return 0;
    }

    int sum = 0;
    for (int n : nums) {
        sum += n;
    }

    return sum / nums.size();
}

int main() {
    std::vector<int> values = {10, 20, 30, 41};
    std::cout << averageValue(values) << std::endl;
    return 0;
}

// Made with Bob
