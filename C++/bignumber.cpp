#include <stack>
#include <sstream>
#include <iostream>

using namespace std;

//声明区
string add(string ,string);
string subtract(string , string);
string multiply(string , string);
string divide(string ,string);
string pow(string ,int);



bool isNegative(string a){//检验是不是负数
	return a[0] == '-';
}

bool isPositive(string a){//检验是不是正数
	return !isNegative(a);
}

bool equals(string a, const long long& b) {
	return a == to_string(b);
}

bool equals(string a, string b) {
	return a == b;
}

string setString(string& Str, string newStr) {
	Str = newStr;
	return Str;
}

string trimLeadingZeros(string a) {
	string b = a;
	if (b.find_first_not_of('0') != string::npos) {
		setString(b, b.erase(0, b.find_first_not_of('0')));
	}
	return b;
}

bool operator==(string b1, string b2) {
	return equals(b1, b2);
}

bool operator>(string b1, string& b2) {
	if (isNegative(b1) || isNegative(b2)) {
		if (isNegative(b1) && isNegative(b2)) {
			string bt = b2;
			b1.erase(0, 1);
			bt.erase(0, 1);
			return b1 < bt;
		}
		else {
			return !(isNegative(b1) && !isNegative(b2));
		}
	}
	b1 = trimLeadingZeros(b1);
	auto c = string(b2);
	c = trimLeadingZeros(c);
	if (b1 == c) {
		return false;
	}
	if (b1.size() > c.size()) {
		return true;
	}
	else if (c.size() > b1.size()) {
		return false;
	}
	else {
		for (unsigned int i = 0; i < b1.size(); ++i) {
			if (b1[i] == static_cast<unsigned int>(c[i] - '0')) {
				continue;
			}
			return b1[i] > static_cast<unsigned int>(c[i] - '0');
		}
	}
	return false;
}

bool operator<(string b1, string b2) {
	return !(b1 == b2) && !(b1 > b2);
}

bool operator>=(string b1, const string& b2) {
	return b1 > b2 || b1 == b2;
}

bool operator<=(string b1, string& b2) {
	return b1 < b2 || b1 == b2;
}

string operator-(string b1, int num){
	return subtract(b1, to_string(num));
}

string opposite(string a) {//置反
	if (a[0] == '-') {
		a.erase(0, 1);//str.erase(x, y):擦除函数,str为string类型,将字符串srt从x开始到y的部分给去掉,左开右闭
	}
	else {//begin():string对象的起始指针
		a.insert(a.begin(), '-');//str.insert(x,"aaa")向str的x位置插入aaa
	}
	return a;
}

extern"C" __declspec(dllexport) string add(string a, string b) {//加
	string b1 = b > a ? b : a;
	string b2 = b > a ? a : b;
	if (isNegative(b1) || isNegative(b2)) {//判断b1，b2中是否有负数
		if (isNegative(b1) && isNegative(b2)) {//判断b1，b2是否都是负数
			return opposite(add(opposite(b1), opposite(b2)));
		}
		else if (isNegative(b1) && !isNegative(b2)) {//若b1负,b2正
			return opposite(subtract(opposite(b1), b2));
		}
		else {
			return opposite(subtract(opposite(b2), b1));//若b1正,b2负
		}
	}
	string results;
	int carry = 0;
	int diff = int(b1.size() - b2.size());
	for (int i = 0; i < diff; ++i) {
		b2.insert(b2.begin(), '0');
	}
	for (int i = int(b1.size() - 1); i >= 0; --i) {
		int sum = (b1[i] - '0') + (b2[i] - '0') + carry;
		carry = 0;
		if (sum <= 9 || i == 0) {
			results.insert(0, to_string(sum));
		}
		else {
			results.insert(0, to_string(sum % 10));
			carry = 1;
		}
	}
	return results;
}

extern"C" __declspec(dllexport) string subtract(string a, string b) {//减
	string b1 = a, b2 = b;
	if (isNegative(b1) || isNegative(b2)) {//判断b1，b2中是否有负数
		if (isNegative(b1) && isNegative(b2)) {//判断b1，b2是否都是负数
			return opposite(add(opposite(b1), opposite(b2)));
		}
		else if (isNegative(b1) && !isNegative(b2)) {//若b1负,b2正
			return opposite(add(opposite(b1), b2));
		}
		else {
			return add(opposite(b2), b1);//若b1正,b2负
		}
	}
	string results;
	int n = 0, p = 0;
	bool takeOffOne = false, shouldBeTen = false;

	if (b1 < b2) {
		//Negative answer
		string t = opposite(subtract(b2, a));
		for (unsigned int i = 1; i < t.length(); ++i) {
			if (t[i] != '0') break;
			t.erase(1, 1);
		}
		return t;
	}
	if (b1.size() - b2.size() > 1) {
		for (unsigned long i = 0; i < b1.size() - b2.size() - 1; ++i) {
			b2.insert(b2.begin(), '0');
		}
	}
	int i = int(b1.size() - 1);
	for (int j = int(b2.size() - 1); j >= 0; --j) {
		if (((b1[i] - '0') < (b2[j] - '0')) && i > 0) {
			n = char((b1[i] - '0') + 10);
			takeOffOne = true;
			if (j > 0 || b1[i - 1] != '0') {
				p = char((b1[i - 1] - '0') - 1);
				if (p == -1) {
					p = 9;
					shouldBeTen = true;
				}
				takeOffOne = false;
			}
			if (shouldBeTen) {
				int index = i - 1;
				for (int c = i - 1; (b1[c] - '0') == 0; --c) {
					b1[c] = static_cast<char>(p + '0');
					--index;
				}
				int t = (b1[index] - '0') - 1;
				b1[index] = static_cast<char>(t + '0');
			}
			b1[i - 1] = static_cast<char>(p + '0');
			shouldBeTen = false;
		}
		stringstream ss;
		if (((b1[i] - '0') == (b2[j] - '0'))) {
			ss << "0";
		}
		else {
			if (n <= 0) {
				ss << ((b1[i] - '0') - (b2[j] - '0'));
			}
			else {
				ss << (n - (b2[j] - '0'));
			}
		}

		results.insert(0, ss.str());
		--i;
		n = 0;
	}
	if (takeOffOne) {
		string number = "";
		for (int j = b1.length() - b2.length() - 1; j >= 0; --j) {
			if (b1[j] == '0') {
				number += "0";
				continue;
			}
			else {
				number.insert(number.begin(), b1[j]);
				int t = atoi(number.c_str());
				--t;
				b1.replace(0, number.size(), to_string(t));
				break;
			}
		}
	}
	while (i >= 0) {
		stringstream ss;
		if (i == 0) {
			if (b1[i] - '0' != 0) {
				ss << (b1[i] - '0');
				results.insert(0, ss.str());
			}
		}
		else {
			ss << (b1[i] - '0');
			results.insert(0, ss.str());
		}
		--i;
	}
	//当结果都是0的时候,只返回一个0
	if (results.find_first_not_of('0') == string::npos) {
		results = "0";
	}
	else if (results[0] == '0') {
		int index = results.find_first_not_of('0');
		results = results.substr(index, results.length() - 1);
	}
	return results;
}

extern"C" __declspec(dllexport) string multiply(string a, string b) {//乘
	string b1 = b > a ? b : a;
	string b2 = b > a ? a : b;
	if (isNegative(b1) || isNegative(b2)) {
		if (isNegative(b1) && isNegative(b2)) {
			return multiply(opposite(b1), opposite(b2));
		}
		else if (isNegative(b1) && !isNegative(b2)) {
			return opposite(multiply(opposite(b1), b2));
		}
		else {
			return opposite(multiply(opposite(b2), b1));
		}
	}
	if (b1 == "0" || b2 == "0") return 0;
	int carry = 0;
	int zeroCounter = 0;
	string b3 = "0";

	for (unsigned int i = 0; i < b1.size() - b2.size(); ++i) {
		b2.insert(b2.begin(), '0');
	}
	string rr;
	for (long long int j = int(b1.size() - 1); j >= 0; --j) {
		int val = ((b2[(b2.size() - 1)] - '0') * (b1[j] - '0')) + carry;
		carry = 0;
		if (val > 9 && j != 0) {
			carry = val / 10;
			rr.insert(0, to_string(val % 10));
		}
		else {
			rr.insert(0, to_string(val));
		}
	}
	if (zeroCounter > 0) {
		for (int x = 0; x < zeroCounter; ++x) {
			rr.append("0");
		}
	}
	++zeroCounter;
	b3 += string(rr);
	if (b3.find_first_not_of('0') != string::npos) {
		setString(b3, b3.erase(0, b3.find_first_not_of('0')));
	}
	else {
		//当结果都是0的时候,只返回一个0
		setString(b3, "0");
	}
	return b3;
}



extern"C" __declspec(dllexport) string divide(string a, string b) {//除
	if (b == "0") {
		cerr << "不能除 0!" << endl;
	}
	string b1 = a, b2 = b;
	bool sign = false;
	if (isNegative(b1) && isNegative(b2)) {
		opposite(b1);
		opposite(b2);
	}
	else if (isNegative(b1) && !isNegative(b2)) {
		opposite(b1);
		sign = true;
	}
	else if (!isNegative(b1) && isNegative(b2)) {
		opposite(b2);
		sign = true;
	}
	string quotient = "0";
	while (b1 >= b2) {
		b1 = subtract(b1, b2);
		quotient = add(quotient, "1");
	}
	if (sign) opposite(quotient);
	return quotient;
}

/*string pow(string a, int exponent) {
	if (exponent < 0) cerr << "指数还不支持为小于0" << endl;
	if (exponent == 0) return string("1");
	if (exponent == 1) return a;
	string result = "1", base = a;
	while (exponent) {
		if (exponent & 1) {
			result = multiply(result, base);
		}
		exponent >>= 1;
		base = multiply(base, base);
	}
	return result;
}*/

int main(){
    string a = "462898989";
    cout<<multiply(a, "5");
    return 0;
}