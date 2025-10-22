#include "matplotlibcpp.h"
#include <iostream>
#include <vector>
#include <string>

// Namespace alias untuk mempermudah pemanggilan
namespace plt = matplotlibcpp;

int main() {
    // Data: Jumlah Bus (Sumbu X)
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

    // Nama Operator (Sumbu Y)
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

    // Posisi numerik untuk sumbu Y
    std::vector<double> y_ticks;
    for(size_t i = 0; i < nama_pt.size(); ++i) {
        y_ticks.push_back(i);
    }

    // Mengatur ukuran figur
    plt::figure_size(1200, 700);

    // Membuat grafik batang horizontal
    plt::barh(y_ticks, jumlah_bus);  // ← Perhatikan: barh, bukan bar

    // Memberi judul dan label sumbu
    plt::title("Jumlah Bus per Operator");
    plt::xlabel("Jumlah Bus"); // karena jumlah bus sekarang di sumbu X
    plt::ylabel("Nama Operator");

    // Mengatur label untuk sumbu Y
    plt::yticks(y_ticks, nama_pt);

    // Batas X agar cukup lebar
    plt::xlim(0, 100);

    // Menambahkan grid
    plt::grid(true);

    // Simpan dan tampilkan
    plt::save("jumlah_bus_operator_horizontal.png");
    plt::show();

    return 0;
}
