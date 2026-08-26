# MergeSort-Complexity-Analysis

Eksperymentalne szacowanie złożoności obliczeniowej – Merge Sort

Autor: Tobiasz Otłowski


1. Opis algorytmu

Sortowanie przez scalanie (ang. Merge Sort) to algorytm sortowania działający w oparciu o zasadę dziel i zwyciężaj. Dzieli on tablicę na dwie podtablice, sortuje je rekurencyjnie, a następnie scala w jedną posortowaną tablicę. Algorytm ten jest stabilny i gwarantuje dobrą złożoność czasową niezależnie od charakterystyki danych wejściowych.


2. Teoretyczna złożoność obliczeniowa
- Przypadek optymistyczny: O(n log n)
- Przypadek pesymistyczny: O(n log n)
- Przypadek średni: O(n log n)

Algorytm wymaga dodatkowej pamięci pomocniczej rzędu O(n), co oznacza, że nie sortuje danych w miejscu.


3. Wyniki eksperymentalne
W celu eksperymentalnego zbadania złożoności czasowej algorytmu, przeprowadzono testy dla danych wejściowych o rozmiarach od 1000 do 10000 elementów. Dla każdego rozmiaru generowano losową tablicę liczb całkowitych, a następnie mierzono czas wykonania sortowania.
 
Powyższy wykres przedstawia zależność czasu działania algorytmu Merge Sort od rozmiaru danych wejściowych. Widzimy, że czas rośnie w sposób logarytmiczno-liniowy, co jest zgodne z teoretyczną złożonością O(n log n).


4. Wnioski
Merge Sort jest wydajnym i stabilnym algorytmem sortowania, którego zachowanie jest przewidywalne niezależnie od danych wejściowych. Eksperymentalne wyniki potwierdzają teoretyczną złożoność obliczeniową.
