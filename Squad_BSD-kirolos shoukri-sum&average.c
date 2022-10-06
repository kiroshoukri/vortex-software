#include <stdio.h>
#include <stdlib.h>

int main(){

    double num1;
    double num2;
    double num3;
    double sum;
    double avg; 

    printf("Enter first number: ");
    scanf("%lf", &num1);
    printf("Enter second number: ");
    scanf("%lf", &num2);
    printf("Enter third number: ");
    scanf("%lf", &num3);

    sum = num1 + num2 + num3;
    avg = sum /3;

    printf("answer: %f\n", sum);
    printf("answer: %f", avg);

    return 0;
}
