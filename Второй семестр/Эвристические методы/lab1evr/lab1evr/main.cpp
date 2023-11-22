#include <string>
#include <iostream>
#include <cmath>
using namespace std;

int n=4;// количество процессов
int nagr[4]={0};
int m=10;
int mas[8]={0};

void sort(){
    int temp;
    for (int i = 0; i < m - 1; i++) {
        for (int j = 0; j < m - i - 1; j++) {
            if (mas[j] < mas[j + 1]) {
                // меняем элементы местами
                temp = mas[j];
                mas[j] = mas[j + 1];
                mas[j + 1] = temp;
            }
        }
    }
}


void show(int *nagr,int n){
     for(int i=0;i < n;i++){
        cout<<nagr[i]<<" ";
    }
}

void fillnagr(int *nagr,int n){
     for(int i=0;i < n;i++){
        nagr[i]=0;
    }
}

void task1(){
    int temp,copy=999,time=0;
    fillnagr(nagr,n);
    for(int i=0;i<m;i++){
        cout<<i+1<<":";
        cin>>mas[i];
    }
    
    sort();
    
    for(int i=0;i<m;i++){
        cout<<mas[i]<<" ";
    }
    
    for(int i=0;i<m;i++){
        cout<<endl;
        show(nagr,n);
        copy=999;
        for(int j=0;j<n;j++){
                if(nagr[j]<copy){
                        copy=nagr[j];
                        time=j;
                }
        }
        nagr[time]=copy+mas[i];
    }
    int c=nagr[0];
    for(int i=0;i<n;i++){
        if(nagr[i]>c && nagr[i]!=0)
            c=nagr[i];
    }
    cout<<endl;
    cout<<"-----------------"<<endl;
    show(nagr,n);
    cout<<" max:"<<c<<endl<<"-----------------"<<endl;
}

void task2(){
    int temp,copy=999,time=0;
    fillnagr(nagr,n);
    for(int i=0;i<m;i++){
        cout<<i+1<<":";
        cin>>mas[i];
    }
    sort();
    
    for(int i=0;i<m;i++){
        cout<<mas[i]<<" ";
    }
    //  //  //  //  //  //  //  // Первый шаг
    int mas1[m/2];fillnagr(mas1, m/2);
    int mas2[m/2];fillnagr(mas2, m/2);

    int sum1=0;int s1=0;
    int sum2=0;
    
    mas1[0]=mas[0];
    sum1=sum1+mas[0];
    
    for(int i=1;i<m;i++){
        s1=0;
       
        if(sum1<=sum2){
            for(int j=0;j<m/2;j++){
                if(mas1[j]==0){
                    mas1[j]=mas[i];
                    sum1=sum1+mas[i];
                    s1=1;
                    break;
                  
                }
            }
        }
        
        if(sum1>sum2 && s1==0){
                for(int j=0;j<m/2;j++){
                    if(mas2[j]==0){
                        mas2[j]=mas[i];
                        sum2=sum2+mas[i];
                        break;
                        
                    }
                }
        }
    }

    //  //  //  //  //  //  //  // Второй шаг
    for(int i=0;i<m/2;i++){
        cout<<endl;
        show(nagr,n);
        copy=999;
        for(int j=0;j<n/2;j++){
                if(nagr[j]<copy){
                        copy=nagr[j];
                        time=j;
                }
        }
        nagr[time]=copy+mas1[i];
    
    }
    
    //  //  //  //  //  //  //  // Второй шаг
    for(int i=0;i<m/2;i++){
        cout<<endl;
        show(nagr,n);
        copy=999;
        
        for(int j=n/2;j<n;j++){
                if(nagr[j]<copy){
                        copy=nagr[j];
                        time=j;
                }
        }
        nagr[time]=copy+mas2[i];
    }
    
    //  //  //  //  //  //  //  //
    
    int c=nagr[0];
    for(int i=0;i<n;i++){
        if(nagr[i]>c && nagr[i]!=0)
            c=nagr[i];
    }
    cout<<endl;
    cout<<"-----------------"<<endl;
    show(nagr,n);
    cout<<" max:"<<c<<endl<<"-----------------"<<endl;
}



int main() {
    task1();
    task2();
    return 0;
}



//void task3(){
//   // bool isPowerOfTwo = m && !(m & (m - 1));
//
//   // int temp;
//    //int copy=999;
//    //time=0;
//        fillnagr(nagr,n);
//        for(int i=0;i<m;i++){
//            cout<<i+1<<":";
//            cin>>mas[i];
//        }
//        sort();
//
//        for(int i=0;i<m;i++){
//            cout<<mas[i]<<" ";
//        }
//        //  //  //  //  //  //  //  // Первый шаг
//        int mas1[m/2];fillnagr(mas1, m/2);
//        int mas2[m/2];fillnagr(mas2, m/2);
//
//        int sum1=0;int s1=0;
//        int sum2=0;
//
////        mas1[0]=mas[0];
////        sum1=sum1+mas[0];
//
//        for(int i=0;i<m;i++){
//            s1=0;
//
//            if(sum1<=sum2){
//                for(int j=0;j<m/2;j++){
//                    if(mas1[j]==0){
//                        mas1[j]=mas[i];
//                        sum1=sum1+mas[i];
//                        cout<<"Первая сумма:"<<sum1;
//                        s1=1;
//                        break;
//
//                    }
//                }
//            }
//
//            if(sum1>sum2 && s1==0){
//                    for(int j=0;j<m/2;j++){
//                        if(mas2[j]==0){
//                            mas2[j]=mas[i];
//                            sum2=sum2+mas[i];
//                            cout<<"Вторая сумма:"<<sum2;
//                            break;
//                        }
//                    }
//            }
//        }
//        cout<<" | ";
//        show(mas1,m/2);
//        cout<<" | ";
//        show(mas2,m/2);
//        // // // // // Второй шаг
//        int mas11[2][m/2];//fillnagr(mas11, m/4);
//        int mas12[2][m/2];//fillnagr(mas12, m/4);
//
//        sum1=0;s1=0;
//        sum2=0;
//
//    // // // // // Третий шаг
//    for(int i=0;i<m/2;i++){
//        s1=0;
//
//        if(sum1<=sum2){
//            for(int j=0;j<m/2;j++){
//                if(mas1[j]==0){
//                    mas11[j]=mas1[i];
//                    sum1=sum1+mas1[i];
//                    cout<<"Первая сумма:"<<sum1;
//                    s1=1;
//                    break;
//
//                }
//            }
//        }
//
//        if(sum1>sum2 && s1==0){
//                for(int j=0;j<m/2;j++){
//                    if(mas12[j]==0){
//                        mas12[j]=mas1[i];
//                        sum2=sum2+mas1[i];
//                        cout<<"Вторая сумма:"<<sum2;
//                        break;
//                    }
//                }
//        }
//    }
//    cout<<" | ";
//    show(mas11,m/4);
//    cout<<" | ";
//    show(mas12,m/4);
//
//     //конец if
////    }
////    else {
////        cout<<"Ошибка! Не степень двойки"<<endl;
////    }
//}
