#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <algorithm>
using namespace std;

inline std::string trim(const std::string &s){
	auto wsfront=std::find_if_not(s.begin(),s.end(),[](int c){return std::isspace(c);});
	auto wsback=std::find_if_not(s.rbegin(),s.rend(),[](int c){return std::isspace(c);}).base();
	return (wsback<=wsfront ? std::string() : std::string(wsfront,wsback));
}
int main () {
	cin.tie(0);
	ifstream src, trg;
	src.open("/home/thinkerpal/Desktop/project/data/act-multiun/cleaned.en");
	trg.open("/home/thinkerpal/Desktop/project/data/act-multiun/untokened_cleaned.zh");
	fstream combined, reversed , newsrc, newtrg;
	combined.open("/home/thinkerpal/Desktop/project/data/act-multiun/notok.combined");
	reversed.open("/home/thinkerpal/Desktop/project/data/act-multiun/notok.reversed");
	newsrc.open("/home/thinkerpal/Desktop/project/data/act-multiun/notok.en");
	newtrg.open("/home/thinkerpal/Desktop/project/data/act-multiun/notok.zh");
	string a, b;
	while (getline(src, a)){
		getline(trg, b);
		trim(a);
		trim(b);
		if (a == "" || b == "" || a == " " || b == " ") continue;
		else{
		newsrc<<a<<"\n";
		newtrg<<b<<"\n";
		combined<<a<<" ||| "<<b<<"\n";
		reversed<<b<<" ||| "<<a<<"\n";
		}
	}
	src.close();
	trg.close();
	combined.close();
	reversed.close();
	cout<<"Done"<<endl;
	return 0;
}
