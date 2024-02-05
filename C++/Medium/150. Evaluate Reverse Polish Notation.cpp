class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> s;

        for (const std::string& x : tokens) {
            if (isOperator(x)) {
                int a = s.top();
                s.pop();
                int b = s.top();
                s.pop();
                s.push(performOperation(x, b, a));
            } else {
                s.push(std::stoi(x));
            }
        }
        return s.top();
    }

private:
    bool isOperator(const std::string& token) {
        return token == "+" || token == "*" || token == "-" || token == "/";
    }

    int performOperation(const std::string& op, int a, int b) {
        if (op == "+") return a + b;
        if (op == "*") return a * b;
        if (op == "-") return a - b;
        if (op == "/") return a / b;
        return 0;
    }
};    