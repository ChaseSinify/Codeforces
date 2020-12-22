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
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef long double ld;

int main(){
    int probs, res = 0;
    scanf("%d", &probs);
    for(int j=0; j < probs; j++){
        int x, y, z; scanf("%d%d%d", &x,&y,&z);
        if(x+y+z>=2){res++;}
    }
    printf("%d", res);
}