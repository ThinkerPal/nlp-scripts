#include <iostream>
#include <fstream>
#include <string>
#include <time.h>
#include <random>
#include <set>
using namespace std;
int checker[5];
int main() {
    cin.tie(0);
    srand(time(0));
    // int totaLines=8508909, tmp;
    // int* alline = new int[totaLines];
    string filename, SOURCE, TARGET, PATH,a,b;
    cout<<"What is the name of the file, Source Language, Target Language IDs and the Path to the main folder?\n";
    cin>>filename>>SOURCE>>TARGET>>PATH;
    ifstream src_og, trg_og;
    string ROOT_PATH=PATH+"/"+filename+".";
    src_og.open(ROOT_PATH + SOURCE);
    trg_og.open(ROOT_PATH+TARGET);
    fstream foldSRC1, foldTRG1, foldCOMBINED1, foldREVERSED1, foldSRC2, foldTRG2, foldCOMBINED2, foldREVERSED2, foldSRC3, foldTRG3, foldCOMBINED3, foldREVERSED3, foldSRC4, foldTRG4, foldCOMBINED4, foldREVERSED4, foldSRC5, foldTRG5, foldCOMBINED5, foldREVERSED5;
    string TEST_PATH = PATH + "/results/test_";
    foldSRC1.open(TEST_PATH + "1." + SOURCE); 
    foldTRG1.open(TEST_PATH + "1." + TARGET); 
    foldCOMBINED1.open(TEST_PATH + "1.combined"); 
    foldREVERSED1.open(TEST_PATH + "1.reversed"); 
    foldSRC2.open(TEST_PATH + "2." + SOURCE); 
    foldTRG2.open(TEST_PATH + "2." + TARGET); 
    foldCOMBINED2.open(TEST_PATH + "2.combined"); // cleaned en zh /home/thinkerpal/Desktop/project/data/act-multiun
    foldREVERSED2.open(TEST_PATH + "2.reversed"); 
    cout<<TEST_PATH + "3." + SOURCE<<endl;
    foldSRC3.open(TEST_PATH + "3." + SOURCE);
    foldTRG3.open(TEST_PATH + "3." + TARGET);
    foldCOMBINED3.open(TEST_PATH + "3.combined");
    foldREVERSED3.open(TEST_PATH + "3.reversed");
    foldSRC4.open(TEST_PATH + "4." + SOURCE);
    foldTRG4.open(TEST_PATH + "4." + TARGET);
    foldCOMBINED4.open(TEST_PATH + "4.combined");
    foldREVERSED4.open(TEST_PATH + "4.reversed"); 
    foldSRC5.open(TEST_PATH + "5." + SOURCE);
    foldTRG5.open(TEST_PATH + "5." + TARGET); 
    foldCOMBINED5.open(TEST_PATH + "5.combined");
    foldREVERSED5.open(TEST_PATH + "5.reversed");
    // cout<<sizeof(alline)/sizeof(alline[0]);
    int tmp=0;
    while (getline(src_og, a)){
        getline(trg_og, b);
        // cout<<alline[i];
        
        if (tmp %5 == 0){
            // cout<<tmp<<"i ran\n";
            if (a == "" || b == "")continue;
            else{
                foldSRC1<<a<<" \n";
                foldTRG1<<b<<" \n";
                foldCOMBINED1<<a<<" ||| "<<b<<" \n";
                foldREVERSED1<<b<<" ||| "<<a<<" \n";
            }    // checker[tmp] ++;

        }else if (tmp%5 == 1){
            if (a == "" || b == "")continue;
            else{
                foldSRC2<<a<<" \n";
                foldTRG2<<b<<" \n";
                foldCOMBINED2<<a<<" ||| "<<b<<" \n";
                foldREVERSED2<<b<<" ||| "<<a<<" \n";
            }
            // checker[tmp] ++;
        }else if (tmp%5 == 2){
            if (a == "" || b == "")continue;
            else{
                foldSRC3<<a<<" \n";
                foldTRG3<<b<<" \n";
                foldCOMBINED3<<a<<" ||| "<<b<<" \n";
                foldREVERSED3<<b<<" ||| "<<a<<" \n";
                // checker[tmp] ++;
            }
        }else if (tmp%5 == 3){
            if (a == "" || b == "")continue;
            else{
                foldSRC4<<a<<" \n";
                foldTRG4<<b<<" \n";
                foldCOMBINED4<<a<<" ||| "<<b<<" \n";
                foldREVERSED4<<b<<" ||| "<<a<<" \n";
                // checker[tmp] ++;
            }
        }else if (tmp%5 == 4){
            if (a == "" || b == "")continue;
            else{
                foldSRC5<<a<<" \n";
                foldTRG5<<b<<" \n";
                foldCOMBINED5<<a<<" ||| "<<b<<" \n";
                foldREVERSED5<<b<<" ||| "<<a<<" \n";
            // checker[tmp] ++;
            }
        }
        tmp++;
        // alline[i] = tmp;
        // if (i%5000 == 0)cout<<"HEllo " << i<<" " <<tmp<<endl;
    }


    // delete[] alline;
    for (int i=0; i<5; i++){
        cout<<checker[i]<<endl;
    }
    return 0;
    foldSRC1.close(); foldTRG1.close(); foldCOMBINED1.close(); foldREVERSED1.close(); foldSRC2.close(); foldTRG2.close(); foldCOMBINED2.close(); foldREVERSED2.close(); foldSRC3.close(); foldTRG3.close(); foldCOMBINED3.close(); foldREVERSED3.close(); foldSRC4.close(); foldTRG4.close(); foldCOMBINED4.close(); foldREVERSED4.close(); foldSRC5.close(); foldTRG5.close(); foldCOMBINED5.close(); foldREVERSED5.close(); src_og.close(); trg_og.close();
}