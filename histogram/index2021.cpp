#include "./matplotlibcpp.h"
#include <iostream>
#include <vector>
#include <string>

namespace plt = matplotlibcpp;

int main() {
    std::vector<double> frekuensi = {5.0, 3.0, 2.0, 1.0, 1.0};

    std::vector<double> x_posisi = {0, 1, 2, 3, 4};

    std::vector<std::string> x_labels = {
        "0-100", "100-200", "200-300", "300-400", "400-500"
    };

    plt::figure_size(1000, 700);

    plt::bar(x_posisi, frekuensi);

    plt::title("Histogram Curah Hujan Tanjung Priok (2021)");
    plt::ylabel("Frekuensi (Jumlah Bulan)");
    plt::xlabel("Curah Hujan (mm)");

    plt::xticks(x_posisi, x_labels);

    std::vector<double> y_ticks;
    for (int i = 0; i <= 6; ++i) {
        y_ticks.push_back(static_cast<double>(i));
    }
    plt::yticks(y_ticks);

    plt::grid(true);

    plt::tight_layout();

    plt::save("histogram_tabel_2021.png");
    plt::show();

    return 0;
}