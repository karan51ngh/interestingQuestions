//naive
#include <iostream>
#define long_MAX 10000000000
using namespace std;
void solved();
long minCost(long, long, long, long, long, long, long);
long min(long, long, long);
signed main()
{
    long T;
    cin >> T;
    while (T--)
    {
        solved();
    }
}
void solved()
{
    long N, E, H, A, B, C;
    cin >> N >> E >> H >> A >> B >> C;
    long ans = minCost(N, E, H, 0, A, B, C);
    if (ans >= long_MAX) //dont forget
        cout << -1 << endl;
    else
        cout << ans << endl;
}
long minCost(long N, long E, long H, long cost, long A, long B, long C)
{
    // cout << "Hello There\n";
    long ***mtx = new long **[N + 1];
    for (long i = 0; i <= N; i++)
    {
        mtx[i] = new long *[E + 1];

        for (long j = 0; j <= E; j++)
        {
            mtx[i][j] = new long[H + 1];
        }
    }
    // cout << "Declared There\n";
    for (int i = 0; i <= N; i++)
    {
        for (int j = 0; j <= E; j++)
        {
            for (int k = 0; k <= H; k++)
            {
                if (i == 0)
                {
                    mtx[i][j][k] = 0;
                }
                // else if (j < 0 || k < 0)
                // {
                //     mtx[i][j][k] = long_MAX;
                // }
                else
                {
                    long flag0, flag1, flag2;
                    flag0 = flag1 = flag2 = 0;
                    if (j - 2 < 0)
                        flag0 = long_MAX;
                    else
                        flag0 = A + mtx[i - 1][j - 2][k];
                    if (k - 3 < 0)
                        flag1 = long_MAX;
                    else
                        flag1 = B + mtx[i - 1][j][k - 3];
                    if (j - 1 < 0)
                        flag2 = long_MAX;
                    else
                        flag2 = C + mtx[i - 1][j - 1][k - 1];
                    if (k - 1 < 0)
                        flag2 = long_MAX;

                    // mtx[i][j][k] = min(A + mtx[i - 1][j - 2][k], B + mtx[i - 1][j][k - 3], C + mtx[i - 1][j - 1][k - 1]);
                    mtx[i][j][k] = min(flag0, flag1, flag2);
                }
            }
        }
    }
    return mtx[N][E][H];
}
long min(long a, long b, long c)
{
    long x = a;
    if (x > b)
        x = b;
    if (x > c)
        x = c;
    return x;
}