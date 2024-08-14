

#include <stdio.h>
#include <string.h>


typedef struct {
   char name[100];
   double price;
   int quantity, sold;
} Dori; // Keyinchalik struct kalit so'zidan foydalanmaslik uchun typedef dan foydalanildi


void filter(Dori *dorilar, int len); // Dorilarni narx bo'yicha filterlaydigan funksiyaning declaration qismi


void view(Dori *dorilar, int len); // Dorilarning ro'yxatini ko'rsatadigan funksiyaning declaration qismi


void most_sold(Dori *dorilar, int len); // Eng ko'p sotilgan dorini ko'rsatadigan funksiyaning declaration qismi


void most_price(Dori *dorilar, int len); // Eng qimmat dorini ko'rsatadigan funksiyaning declaration qismi


void least_price(Dori *dorilar, int len); // Eng arzon dorini ko'rsatadigan funksiyaning declaration qismi


void least_to_most(Dori *dorilar, int len); // Dorilarni narx bo'yicha arzondan qimmatga filterlaydigan funksiyaning declaration qismi


int main() {
   Dori d1 = {"Parasetamol", 2000, 1000, 100};
   Dori d2 = {"Sitramon", 2000, 500, 10};
   Dori d3 = {"Kyupen", 3000, 700, 30};
   Dori d4 = {"Taylon hot", 10000, 600, 5};
   Dori d5 = {"Vinilin", 15000, 500, 60};
   Dori d6 = {"Spirt", 3000, 300, 70};
   Dori d7 = {"VragGrip", 6000, 400, 120};
   Dori d8 = {"Bol Nol", 4000, 600, 140};
   Dori d9 = {"Shprist", 5000, 800, 160};
   Dori d10 = {"Yodamarin", 15000, 300, 150};
   Dori d11 = {"Analgin", 3000, 6000, 30};
   Dori d12 = {"Sirop", 10000, 7000, 240};
   Dori d13 = {"Vitamin", 5000, 2000, 190};
   Dori d14 = {"Ketonal", 500, 800, 500};
   Dori d15 = {"Nol gripp", 2000, 1400, 540};
   Dori d16 = {"Omes", 4000, 12000, 600};
   Dori d17 = {"Natriy Xlor", 700, 2500, 320};
   Dori d18 = {"Novakeyin", 20000, 3000, 140};
   Dori d19 = {"Lidakeyin", 24000, 9000, 40};
   Dori d20 = {"Yodamarin", 5000, 3000, 190};
   Dori dorilar[] = {d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20}; // Barcha dorilar bir massivga joylandi
   int length = sizeof(dorilar) / sizeof(dorilar[0]);
   int n;
   printf("Menular ro'yxati:\n1 -> Narx bo'yicha filterlash\n2 -> Barcha dorilar ro'yxati\n3 -> Eng ko'p sotilgan dori\n4 -> Eng qimmat dori\n5 -> Eng arzon dori\n6 -> Arzondan qimmatga dorilar ro'yxati\nMenu kiriting: ");
   scanf("%d", &n);
   switch (n){ // Switch Case orqali Menu qismi shakllantirildi
       case 1: filter(dorilar, length); break;
       case 2: view(dorilar, length); break;
       case 3: most_sold(dorilar, length); break;
       case 4: most_price(dorilar, length); break;
       case 5: least_price(dorilar, length); break;
       case 6: least_to_most(dorilar, length); break;
       default: printf("Noto'g'ri raqam kiritildi. Dasturni qayta ishga tushuring va to'g'ri raqam kiriting!"); break;
   }
   return 0;
}


// Dorilarni narx bo'yicha filterlaydigan funksiya
void filter(Dori *dorilar, int len) {
   printf("Filterlash uchun narx kiriting: ");
   double price;
   scanf("%lf", &price);
   printf("Kiritilgan narx bo'yicha filterlangan dorilar:\n");
   printf("| %25s | %10s | %6s | %7s |\n", "NOM", "NARX", "QOLDIQ", "SOTILDI");
   for (int i = 0; i < len; i++){
       if (dorilar[i].price == price) {
           printf("| %25s | %10.2lf | %6d | %7d |\n", dorilar[i].name, dorilar[i].price, dorilar[i].quantity, dorilar[i].sold);
       }
   }
   printf("\n");
}


// Dorilarning ro'yxatini ko'rsatadigan funksiya
void view(Dori *dorilar, int len){
   printf("Barcha dorilar ro'yxati:\n");
   printf("| %25s | %10s | %6s | %7s |\n", "NOM", "NARX", "QOLDIQ", "SOTILDI");
   for (int i = 0; i < len; i++){
       printf("| %25s | %10.2lf | %6d | %7d |\n", dorilar[i].name, dorilar[i].price, dorilar[i].quantity, dorilar[i].sold);
   }
   printf("\n");
}


// Eng ko'p sotilgan dorini ko'rsatadigan funksiya
void most_sold(Dori *dorilar, int len){
   Dori most = dorilar[0];
   printf("Eng ko'p sotilgan dori:\n");
   printf("| %25s | %10s | %6s | %7s |\n", "NOM", "NARX", "QOLDIQ", "SOTILDI");
   for (int i = 1; i < len; i++){
       if(most.sold < dorilar[i].sold) most = dorilar[i];
   }
   printf("| %25s | %10.2lf | %6d | %7d |\n\n", most.name, most.price, most.quantity, most.sold);
}


// Eng qimmat dorini ko'rsatadigan funksiya
void most_price(Dori *dorilar, int len){
   Dori most = dorilar[0];
   printf("Eng qimmat dori:\n");
   printf("| %25s | %10s | %6s | %7s |\n", "NOM", "NARX", "QOLDIQ", "SOTILDI");
   for (int i = 1; i < len; i++){
       if(most.price < dorilar[i].price) most = dorilar[i];
   }
   printf("| %25s | %10.2lf | %6d | %7d |\n\n", most.name, most.price, most.quantity, most.sold);
}


// Eng arzon dorini ko'rsatadigan funksiya
void least_price(Dori *dorilar, int len){
   Dori least = dorilar[0];
   printf("Eng arzon dori:\n");
   printf("| %25s | %10s | %6s | %7s |\n", "NOM", "NARX", "QOLDIQ", "SOTILDI");
   for (int i = 1; i < len; i++){
       if(least.price > dorilar[i].price) least = dorilar[i];
   }
   printf("| %25s | %10.2lf | %6d | %7d |\n\n", least.name, least.price, least.quantity, least.sold);
}


// Dorilarni narx bo'yicha arzondan qimmatga filterlaydigan funksiya
void least_to_most(Dori *dorilarlar, int len){
   Dori dorilar[len];
   printf("Eng arzon doridan eng qimmat dorigacha ro'yxat:\n");
   printf("| %25s | %10s | %6s | %7s |\n", "NOM", "NARX", "QOLDIQ", "SOTILDI");
   for (int i = 0; i < len; i++){
       dorilar[i] = dorilarlar[i];
   }
   for (int i = 0; i < len; i++){
       Dori least = dorilar[i];
       int index = i;
       for (int j = i; j < len; j++){
           if (least.price > dorilar[j].price) {
               least = dorilar[j];
               index = j;
           }
       }
       Dori temp = dorilar[i];
       dorilar[i] = least;
       dorilar[index] = temp;
   }
   for (int i = 0; i < len; i++){
       printf("| %25s | %10.2lf | %6d | %7d |\n", dorilar[i].name, dorilar[i].price, dorilar[i].quantity, dorilar[i].sold);
   }
   printf("\n");
}
