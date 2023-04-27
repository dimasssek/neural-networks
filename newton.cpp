#include <iostream>
#include <vector>
using namespace std;
double eps1 = 0.1, eps2 = 0.15, eps3 = 0.0000001;
int M = 10;
double x01 = 1.5, x02 = 1.5;
double A, B, d1, d2;


double F(double x1, double x2)
{
    return 3 * x1 * x1 + x2 * x2 -  x1 * x2 + x1;
}


double dFx1x1(double x1, double x2) 
{
    return (F(x1 + 2 * eps3, x2) - F(x1 + eps3, x2) - F(x1 + eps3, x2) + F(x1, x2)) / (eps3 * eps3);
}

double dFx1x2(double x1, double x2) 
{
    return (F(x1 + eps3, x2 + eps3) - F(x1 + eps3, x2) - F(x1, x2 + eps3) + F(x1, x2)) / (eps3 * eps3);
}

double dFx2x2(double x1, double x2) 
{
    return (F(x1, x2 + 2 * eps3) - F(x1, x2 + eps3) - F(x1, x2 + eps3) + F(x1, x2)) / (eps3 * eps3);
}

double gradFx1(double x1, double x2) 
{
    return (F(x1 + eps3, x2) - F(x1 - eps3, x2)) / (2 * eps3);
}

double gradFx2(double x1, double x2) 
{
    return (F(x1, x2 + eps3) - F(x1, x2 - eps3)) / (2 * eps3);
}

double norma(double a, double b) {
    double norma = sqrt(a * a + b * b);
    return norma;
}

double det(double** a) {
    double d;
    d = a[0][0] * a[1][1] - a[0][1] * a[1][0];
    return d;
}

void to_invers_matr(double** matr) {
    double tmp;
    tmp = matr[0][0];
    double deter = abs(det(matr));
    matr[0][0] = matr[1][1] / deter;
    matr[1][1] = tmp / deter;
    matr[0][1] = -(matr[0][1]) / deter;
    matr[1][0] = -(matr[1][0]) / deter;
}

bool is_positive_define_matr(double** a) {
    if (a[1][1] > 0 && det(a) > 0)
        return true;
    else return false;
}

void mult_matr_on_vector(double** a, double a1, double a2) {
    d1 = -(a[0][0] * a1 + a[0][1] * a2);
    d2 = -(a[1][0] * a1 + a[1][1] * a2);
}

void main()
{
    setlocale(LC_ALL, ".1251");
    double t, xk_next1 = x01, xk_next2 = x02, xk1 = x01, xk2 = x02, b[2][2];
    double** a;
    a = new double* [2];
    for (int i = 0; i < 2; i++)
        a[i] = new double[2];
    int k = 0, flag = 0;
    do {
        cout << "ИТЕРАЦИЯ " << k << ":" << endl;
        cout << "=======================" << endl;
        cout << "=======================" << endl;
        double grad1 = gradFx1(xk1, xk2);
        double grad2 = gradFx2(xk1, xk2);
        cout << "grad f(x01) = " << grad1 << endl;
        cout << "grad f(x02) = " << grad2 << endl;
        double norma_grad_k = norma(grad1, grad2);
        cout << "||gradf(x)|| = " << norma_grad_k << endl;
        if (norma_grad_k < eps1)
        {
            cout << "Так как ||gradf(x)|| <= " << eps1 << ", то вычисления окончены " << endl;
            break;
        }
        else cout << "Так как ||gradf(x)|| > " << eps1 << " продолжим вычисления " << endl;
        if (k >= M)
        {
            cout << "Так как k>=M, то вычисления окончены" << endl;
            break;
        }
        else cout << "Так как k<M, то продолжим вычисления" << endl;
        cout << "x(k) = (" << xk1 << "; " << xk2 << ")" << endl;
        a[0][0] = dFx1x1(x01, x02); a[0][1] = dFx1x2(x01, x02); a[1][0] = a[0][1]; a[1][1] = dFx2x2(x01, x02);
        cout << "Матрица H = ";
        cout << a[0][0] << " "; cout << a[0][1] << endl;
        cout << "            " << a[1][0] << " "; cout << a[1][1] << endl;
        cout << "det = " << det(a) << endl;
        to_invers_matr(a);
        if (is_positive_define_matr(a)) {

            mult_matr_on_vector(a, grad1, grad2);

            cout << "Матрица положительно определена" << endl;
            t = 1;
        }
        else
        {
            cout << "Матрица отрицательно определена" << endl;
            break;
        }
        cout << "d=(" << d1 << "; " << d2 << ")" << endl;

        cout << "t = " << t << endl;
        xk_next1 = xk1 + t * d1;
        xk_next2 = xk2 + t * d2;
        cout << "x(k+1) = (" << xk_next1 << "; " << xk_next2 << ")" << endl;
        if (norma(xk_next1 - xk1, xk_next2 - xk2) < eps2 && abs(F(xk_next1, xk_next2) - F(xk1, xk2)) < eps2)
        {
            cout << "||x(k+1)-x(k)|| = " << norma(xk_next1 - xk1, xk_next2 - xk2) << endl;
            cout << "|F(x(k+1))-F(x(k))| = " << abs(F(xk_next1, xk_next2) - F(xk1, xk2)) << endl;
            flag++;
        }
        else
            flag = 0;
        if (F(xk_next1, xk_next2) > F(xk1, xk2))
        {
            cout << "F(x(k+1))>F(x(k)) => функция начала возрастать => расчет окончен" << endl;
            xk_next1 = xk1;
            xk_next2 = xk2;
            break;
        }
        k++;
        xk1 = xk_next1;
        xk2 = xk_next2;
        cout << "Количество раз выполнения условий окончания: " << flag << endl;
        cout << endl;
    } while (flag != 2);
    double x1 = xk_next1;
    double x2 = xk_next2;
    double res = F(x1, x2);
    cout << "Ответ: " << endl;
    cout << "Точка локального минимума: x_min = (" << x1 << "; " << x2 << ")" << endl;
    cout << "Значение функции в точке: f(x_min) = " << res << endl;

}
