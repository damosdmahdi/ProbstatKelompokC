#include "matplotlibcpp.h"
#include <iostream>
#include <vector>
#include <string>

namespace plt = matplotlibcpp;

int main() {

    std::vector<double> jumlah_bus = {
        87,  // Swakelola
        63,  // PT Trans Batavia
        57,  // PT Jakarta Trans Metropolitan
        39,  // PT Jakarta Mega Trans
        25,  // PT Eka Sari Lorena
        27,  // PT Primajasa Perdana Raya Utama
        80,  // PT Bianglala Metropolitan
        48,  // PT Trans Mayapada Busway
        75,  // PT Perum Damri
        1    // PT Kopaja
    };


    std::vector<std::string> nama_pt = {
        "Swakelola",
        "PT Trans Batavia",
        "PT Jkt Trans Metropolitan",
        "PT Jkt Mega Trans",
        "PT Eka Sari Lorena",
        "PT Primajasa Perdana",
        "PT Bianglala Metropolitan",
        "PT Trans Mayapada",
        "PT Perum Damri",
        "PT Kopaja"
    };


    std::vector<double> x_ticks;
    for(size_t i = 0; i < nama_pt.size(); ++i) {
        x_ticks.push_back(i);
    }

    plt::figure_size(1200, 700); 

    plt::bar(x_ticks, jumlah_bus);

    plt::title("Jumlah Bus per Operator");

    plt::ylabel("Jumlah Bus");


    plt::xticks(x_ticks, nama_pt);

    plt::ylim(0, 100); 

    plt::grid(true);
    

    plt::save("jumlah_bus_operator.png");

    plt::show();

    return 0;
}