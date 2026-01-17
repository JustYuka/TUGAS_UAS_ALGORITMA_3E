import heapq
import sys


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert_node(root, key):
    """Fungsi untuk memasukkan angka ke dalam BST"""
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert_node(root.right, key)
        else:
            root.left = insert_node(root.left, key)
    return root
def inorder_traversal(root):
    """InOrder: Kiri -> Akar -> Kanan"""
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    """PreOrder: Akar -> Kiri -> Kanan"""
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    """PostOrder: Kiri -> Kanan -> Akar"""
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=' ')

def menu_bst():
    root = None
    while True:
        print("\n--- MENU BINARY SEARCH TREE ---")
        print("1. Tambah Angka (Insert Node)")
        print("2. Lihat Traversal (Pre/In/Post Order)")
        print("3. Reset Tree")
        print("4. Kembali ke Menu Utama")
        
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            try:
                angka = int(input("Masukkan angka: "))
                root = insert_node(root, angka)
                print(f"Angka {angka} berhasil dimasukkan.")
            except ValueError:
                print("Error: Harap masukkan angka bulat.")
        
        elif pilihan == '2':
            if root is None:
                print("Tree masih kosong!")
            else:
                print("\nPreOrder  : ", end="")
                preorder_traversal(root)
                print("\nInOrder   : ", end="")
                inorder_traversal(root)
                print("\nPostOrder : ", end="")
                postorder_traversal(root)
                print()
        
        elif pilihan == '3':
            root = None
            print("Tree berhasil dikosongkan.")
            
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        self.nodes.add(from_node)
        self.nodes.add(to_node)
        self.edges.setdefault(from_node, []).append((to_node, weight))
        self.edges.setdefault(to_node, []).append((from_node, weight))

def dijkstra(graph, start_node):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start_node] = 0
    
    pq = [(0, start_node)]

    previous_nodes = {node: None for node in graph.nodes}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        if current_node in graph.edges:
            for neighbor, weight in graph.edges[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous_nodes

def menu_dijkstra():
    g = Graph()
    print("\nInisialisasi Graph Default...")
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 3)
    g.add_edge('E', 'D', 4)
    print("Graph default: A-B(4), A-C(2), B-C(5), B-D(10), C-E(3), E-D(4)")

    while True:
        print("\n--- MENU DIJKSTRA (SHORTEST PATH) ---")
        print("1. Tambah Jalur (Edge)")
        print("2. Cari Jalur Terpendek")
        print("3. Reset Graph")
        print("4. Kembali ke Menu Utama")
        
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            try:
                u = input("Node Asal (contoh: A): ").upper()
                v = input("Node Tujuan (contoh: B): ").upper()
                w = int(input("Bobot/Jarak (angka): "))
                g.add_edge(u, v, w)
                print(f"Jalur {u}-{v} dengan bobot {w} ditambahkan.")
            except ValueError:
                print("Bobot harus berupa angka.")

        elif pilihan == '2':
            start = input("Masukkan Node Awal: ").upper()
            if start not in g.nodes:
                print("Node tidak ditemukan dalam graph!")
                continue
            
            distances, _ = dijkstra(g, start)
            
            print(f"\nJarak terpendek dari {start}:")
            for node, dist in distances.items():
                print(f"Ke {node} : {dist}")

        elif pilihan == '3':
            g = Graph()
            print("Graph dikosongkan.")

        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")

def main():
    while True:
        print("\n========================================")
        print("   TUGAS KELOMPOK: ALGORITMA & DATA")
        print("========================================")
        print("1. Studi Kasus: Binary Search Tree & Traversal")
        print("2. Studi Kasus: Algoritma Dijkstra")
        print("3. Keluar")
        
        choice = input("Pilih modul (1-3): ")

        if choice == '1':
            menu_bst()
        elif choice == '2':
            menu_dijkstra()
        elif choice == '3':
            print("非常感谢，程序已经完成了 :3.")
            break
        else:
            print("Input salah, silakan coba lagi.")

if __name__ == "__main__":
    main()