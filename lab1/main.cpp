#include <iostream>
#include <string>
#include <vector>
#include <csignal>
#include <ctime>
#include <cmath>
#include <gmpxx.h>

std::vector<mpz_class> pars (std::string inputStr){
    std::vector<mpz_class> n;
    bool strN2 = false;
    mpz_class tmp;
    tmp = 0;
    
    for(std::string::iterator i = inputStr.begin(); i != inputStr.end(); ++i){
        if (*i == '='){
            tmp = 0;
            ++i;
            while (*i != ','){ 
                tmp = tmp * 10 + (*i) - '0';
                ++i;
            }
            n.push_back(tmp);
        }
    }
    return n;
}

using namespace std;

int main(){
    mpz_class number, result;
    number = "3302022959000306046128783870517426861536127416885126746405163395921117861821121029527442053342211074722025278666410267389648339529546822960355263493733516389988478563166173570125125320373840042467197427715570566783354934876492962376348888456514955245307546351321990013280137573736294484549777438046907147746082497547574721415593280178417596118368966005440070935516884807614630932600250786098413254455580028740515858031572232760606988105994915916825321411634327591";
    vector<mpz_class> n;
    string tmpStr;
    string numStr("\0");

    while (cin >> tmpStr){
        numStr = numStr + tmpStr;
    }
    n = pars(numStr);
    for(unsigned i = 0; i < n.size(); ++i){
        mpz_gcd(result.get_mpz_t(), n[i].get_mpz_t(), number.get_mpz_t());
        if(result != 1 ){ //&& i != variant
            cout << "number #1: " << result << endl;
            cout << "number #2: " << number / result << endl;
            break;
        }
    }
    return 0;
}
