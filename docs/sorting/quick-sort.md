# Quick Sort

快速排序（Quick Sort）是一種使用分治法策略的排序演算法。它的基本思想是選擇數列中的一個數作為基準（pivot），然後將所有比基準小的數放到基準的左邊，將所有比基準大的數放到基準的右邊。這一步稱為分區（partition）。然後，對左右兩邊的子數列進行遞迴操作，直到所有的子數列都排序完成。

快速排序在最壞的情況下，時間複雜度為 O(n^2)，但在大多數情況下，時間複雜度為 O(n log n)。它不需要額外的記憶體空間，因此在實際應用中，快速排序通常比其他的 O(n log n) 複雜度的排序演算法更有效率。

## Source Code

[Python](https://github.com/okisdev/Algorithm-Samples/Python/Sorting/quick-sort.py)

[JavaScript](https://github.com/okisdev/Algorithm-Samples/JavaScript/Sorting/quick-sort.js)
