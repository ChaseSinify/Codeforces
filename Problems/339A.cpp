#include <bits/stdc++.h>
using namespace std;

#define PB push_back
#define F first
#define S second
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007

#define YES printf("YES")
#define NO printf("NO")

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef long double ld;

const int nax = 1e5+1;
char s[nax];
vector<char> res;
vector<char> nums;

int main(){
    int plus = 0;
    scanf("%s", s);
    // printf("%s", s);
    for(auto &c : string(s)){
        if(c == '+'){plus++;}
        else{nums.push_back(c);}
    }
    sort(nums.begin(), nums.end());
    for(auto &c : nums){
        res.push_back(c);
        res.push_back('+');
    }
    res.pop_back();
    printf("%s", string(res.begin(), res.end()).c_str());
}