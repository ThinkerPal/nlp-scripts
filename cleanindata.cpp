#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <locale>
#include <codecvt>
using namespace std;
string strip_punct(string& inp){
    auto to = begin(inp);   
    for (auto from : inp)
        if (!ispunct(from)) 
            *to++ = from;
    inp.resize(distance(begin(inp), to));
    return inp;
}
size_t strlen_utf8(const std::string& str) {
	std::size_t length = 0;
	for (char c : str) {
		if ((c & 0xC0) != 0x80) {
			++length;
		}
	}
	return length;
}

int main () {
    cin.tie(0);
    setlocale(LC_ALL, "");
    string filename, SOURCE, TARGET, PATH, a, b="";
    u16string g, h;
    cout<<"What is the name of the file, Source Language, Target Language IDs and the Path to the main folder?\n";
    cin>>filename>>SOURCE>>TARGET>>PATH;
    ifstream src_og, trg_og;
    ofstream cleaned_src, cleaned_trg;
    string ROOT_PATH=PATH+"/"+filename+"."+SOURCE+"-"+TARGET+".";
    src_og.open(ROOT_PATH + SOURCE);
    trg_og.open(ROOT_PATH+TARGET);
    cleaned_src.open(PATH + "/cleaned." + SOURCE);
    cleaned_trg.open(PATH + "/cleaned."+TARGET);
    wstring_convert<codecvt_utf8<char32_t>, char32_t> cvt;
    
    while (getline(src_og, a)){
        getline(trg_og, b);
        a=strip_punct(a);
        b=strip_punct(b);
        // h = toUTF8(b);
        if (a.size() > 30 && strlen_utf8(b) > 7){
            cleaned_src << a << "\n";
            cleaned_trg << b <<"\n";
        }
    }
    cout<<"Done\n";
    src_og.close();
    trg_og.close();
    cleaned_src.close();
    cleaned_trg.close();
    return 0;
}