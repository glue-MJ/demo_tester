#include <iostream>

int factorial(int i){
    if (i == 1)
        return i;
    else
        return i * factorial(i - 1);
}

int main(){
    int j = factorial(10);

    std::cout<<j<<std::endl;

    return 0;
}