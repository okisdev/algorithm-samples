# Binary Search

二元搜尋（Binary Search）是一種在有序數列中尋找特定值的搜尋演算法。其搜尋過程是先將目標值與數列中間的元素比較，如果目標值較大，則在數列的右半部繼續搜尋；如果目標值較小，則在數列的左半部繼續搜尋，如此反覆直到找到目標值，或是搜尋範圍已經縮小到無法再縮小為止。

二元搜尋的時間複雜度為 O(log n)，其中 n 為數列的長度。這意味著每增加一倍的數據量，所需的搜尋時間只會增加一個常數。因此，對於非常大的數據集，二元搜尋比線性搜尋（Linear Search）更有效率。然而，二元搜尋的前提是數列必須已經排序。

## Source Code

[Python](https://github.com/okisdev/algorithm-samples/blob/main/Python/Searching/binary-search.py)

[JavaScript](https://github.com/okisdev/algorithm-samples/blob/main/JavaScript/Searching/binary-search.js)
