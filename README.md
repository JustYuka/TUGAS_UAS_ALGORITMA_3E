1.	Binary Search Tree (BST) & Traversal
•  Konsep: BST adalah struktur data pohon di mana setiap node memiliki maksimal dua anak. Anak kiri selalu lebih kecil dari induk, dan anak kanan selalu lebih besar.
•  Implementasi: Kita menggunakan class Node untuk merepresentasikan simpul. Fungsi insert_node menggunakan rekursi untuk mencari posisi yang tepat bagi angka baru.
•  Traversal (Penelusuran):
•	PreOrder: Cetak dulu, baru ke kiri, lalu ke kanan.
•	InOrder: Ke kiri dulu, cetak, baru ke kanan (Ini akan menghasilkan angka yang terurut otomatis dari kecil ke besar).
•	PostOrder: Ke kiri dulu, ke kanan, baru cetak terakhir.

2.Algoritma Dijkstra
•  Konsep: Algoritma ini mencari jarak terpendek dari satu titik (node) ke semua titik lain dalam sebuah graph berbobot positif.
•  Implementasi:
•	Menggunakan Dictionary untuk menyimpan Graph (daftar ketetanggaan).
•	Menggunakan Priority Queue (heapq). Ini sangat penting! Heap memastikan kita selalu memproses node dengan jarak terpendek terlebih dahulu, membuat algoritma ini efisien (Greedy Approach).
•	Program akan terus mengupdate jarak jika ditemukan jalur baru yang lebih "murah" (bobot lebih kecil) dibanding jalur yang sudah diketahui sebelumnya.

NOTED : Menjalankan
1.	Pastikan Python sudah terinstall.
2.	Simpan kode di atas dengan nama tugas_kelompok.py.
3.	Jalankan lewat terminal/CMD: python tugas_kelompok.py.
