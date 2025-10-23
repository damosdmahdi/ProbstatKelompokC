#include "./matplotlibcpp.h"
#include <iostream>
#include <vector>
#include <string>

// Namespace alias untuk mempermudah pemanggilan
namespace plt = matplotlibcpp;

int main() {

    std::vector<double> curah_hujan = {
        268.2,  // Januari
        496.1,  // Pebruari
        246.7,  // Maret
        76.9,   // April
        117.7,  // Mei
        90.6,   // Juni
        11.7,   // Juli
        0.0,    // Agustus (data "-" diganti jadi 0.0)
        2.7,    // September
        8888.0, // Oktober (data "8.888,0")
        204.1,  // Nopember
        7.0     // Desember
    };


    std::vector<std::string> bulan = {
        "Jan", "Peb", "Mar", "Apr", "Mei", "Jun", 
        "Jul", "Ags", "Sep", "Okt", "Nop", "Des"
    };

    std::vector<double> x_ticks;
    for(size_t i = 0; i < bulan.size(); ++i) {
        x_ticks.push_back(i);
    }

    plt::figure_size(1200, 700); 

    plt::bar(x_ticks, curah_hujan);

    plt::plot(x_ticks, curah_hujan, "r-o");
    plt::title("Curah Hujan di Stasiun Tanjung Priok (2023)");
    plt::ylabel("Curah Hujan (Mm)");

    plt::xlabel("Bulan");


    plt::xticks(x_ticks, bulan);

    plt::ylim(0, 9500); 


    std::vector<double> y_ticks;
    for (int i = 0; i <= 9000; i += 1000) {
        y_ticks.push_back(static_cast<double>(i));
    }

    plt::yticks(y_ticks);


    plt::grid(true);
    
    plt::tight_layout();
    plt::save("curah_hujan_plot.png");
    plt::show();

    return 0;
}