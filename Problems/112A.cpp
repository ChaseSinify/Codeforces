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
char s1[nax];
char s2[nax];

int main(){
    scanf("%s", &s1);
    scanf("%s", &s2);
    for(auto &c : s1){c=tolower(c);}
    for(auto &c : s2){c=tolower(c);}
    int x = strcmp(s1,s2);
    if(x == 0){printf("%d", 0);}
    else if(x > 0){printf("%d", 1);}
    else if(x < 0){printf("%d", -1);}
}