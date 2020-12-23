#include <bits/stdc++.h>
using namespace std;

#define PB push_back
#define F first
#define S second
#define INF (int)1e9
#define EPS 1e-9
#define PI 3.1415926535897932384626433832795
#define MOD 1000000007

#define si(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define ss(s) scanf("%s", s)
#define pi(x) printf("%d\n", x)
#define pl(x) printf("%lld\n", x)
#define ps(s) printf("%s\n", s)

#define YES printf("YES")
#define NO printf("NO")

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<ii> vii;
typedef long double ld;

const int nax = 1e5+1;

int main(){
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int T;
    scanf("%d", &T);
    for(int i=0; i<T*2; i+=2){
        int n; scanf("%d", &n);

        vi vec(n);
        for(int j = 0; j < n; j++){
            ll d; scanf("%lld", &d);
            vec[j] = d;
        }

        ll even=0, odd=0;
        for(int k = 0; k < vec.size(); k++){
            if(k % 2 == 0)
                even += vec[k];
            else
                odd += vec[k];
        }

        if(even >= odd){ // if even larger or equal (which eq doesnt matter), make odd 1s
            for(int k = 0; k < vec.size(); k++){
                if(k % 2 == 0)
                    cout << vec[k] << " ";
                else
                    cout << "1 ";
            }
        }else if(even < odd){ // else if even smaller, make even 1s
            for(int k = 0; k < vec.size(); k++){
                if(k % 2 == 0)
                    cout << "1 ";
                else
                    cout << vec[k] << " ";
            }
        }
        cout << endl;
    }
}