import random

zufallsliste = [random.randint(1, 100) for _ in range(10)]

# sortierte_liste = sorted(zufallsliste)
# print(sortierte_liste)

def bubble_sort(arr):
    n = len(arr)
    # Der äußere Durchlauf läuft von 0 bis n-2, da nach n-1 Durchläufen das größte Element an der richtigen Stelle steht.
    for i in range(n - 1):
        # Der innere Durchlauf vergleicht benachbarte Elemente und tauscht sie, wenn sie in falscher Reihenfolge sind
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

unsortierte_liste = zufallsliste.copy()
print("Unsortierte Liste:", unsortierte_liste)
bubble_sort(unsortierte_liste)
sortierte_liste = unsortierte_liste
print("Sortierte Liste:", sortierte_liste)
