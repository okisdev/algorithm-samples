# Algorithm Samples

This repository contains samples of various types of algorithms implemented in Python.

## Types of Algorithms

1. **Searching Algorithms:**

    - Examples: Binary Search, Linear Search
    - Description: Searching algorithms are designed to check for an element or retrieve an element from any data structure where it is stored. Binary search is a fast search algorithm with run-time complexity of Ο(log n). This search algorithm works on the principle of divide and conquer. For this algorithm to work properly, the data collection should be in the sorted form. Linear search is the simplest search algorithm and often called sequential search. It is a method for finding an element within a list.

2. **Dynamic Programming Algorithms:**

    - Examples: Knapsack Problem, Longest Common Subsequence
    - Description: Dynamic programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions. The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences (often just two sequences).

3. **Divide and Conquer Algorithms:**

    - Examples: Merge Sort, Quick Sort
    - Description: Divide and conquer is an algorithmic paradigm. A typical Divide and Conquer algorithm solves a problem using the following three steps. 1) Divide: Break the given problem into subproblems of same type. 2) Conquer: Recursively solve these subproblems. 3) Combine: Appropriately combine the answers. Merge Sort is a kind of Divide and Conquer algorithm in computer programrming. It is one of the most popular sorting algorithms and a great way to develop confidence in building recursive algorithms. Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays.

4. **Greedy Algorithms:**

    - Examples: Kruskal's Algorithm, Prim's Algorithm
    - Description: A Greedy algorithm is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. So the problems where choosing locally optimal also leads to global solution are best fit for Greedy. Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of the least possible weight that connects any two trees in the forest. Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. It finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

5. **Backtracking Algorithms:**

    - Examples: Eight Queens Problem, Rat in a Maze
    - Description: Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree). For example, the eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. The Rat in a Maze is a simple problem to understand and interpret the working of backtracking.

6. **Machine Learning Algorithms:**

    - Examples: Linear Regression, Logistic Regression
    - Description: Machine Learning algorithms are an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine Learning focuses on the development of computer programs that can access data and use it learn for themselves. For example, Linear regression is a linear approach to modelling the relationship between a dependent variable and one or more independent variables. Logistic Regression is a Machine Learning classification algorithm that is used to predict the probability of a categorical dependent variable. In logistic regression, the dependent variable is a binary variable that contains data coded as 1 (yes, success, etc.) or 0 (no, failure, etc.). In other words, the logistic regression model predicts P(Y=1) as a function of X.

7. **Cryptography Algorithms:**

    - Examples: RSA, AES
    - Description: Cryptography involves creating written or generated codes that allow information to be kept secret. Cryptography converts data into a format that is unreadable for an unauthorized user, allowing it to be transmitted without unauthorized entities decoding it back into a readable format, thus compromising the data. RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. In such a cryptosystem, the encryption key is public and distinct from the decryption key which is kept secret (private). AES (Advanced Encryption Standard) is a symmetric encryption algorithm established by the U.S. National Institute of Standards and Technology (NIST) in 2001.

8. **Geometry Algorithms:**

    - Examples: Convex Hull, Line Intersection
    - Description: Geometry algorithms are those algorithms which perform computations and process data related to geometric shapes like points, lines, polygons etc. Convex Hull is the smallest polygon convex figure that contains all the points of S. In other words, the smallest convex polygon that can be drawn around the points is called Convex Hull. The Line Intersection problem is to find whether two lines intersect at a point or not.

9. **Graph Algorithms:**

    - Examples: Breadth First Search, Depth First Search
    - Description: Graph algorithms are a significant field of interest within computer science. Graph algorithms are algorithms that deal with graphs, which are a specific set of vertices connected by edges. Breadth First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level. Depth First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

10. **Pattern Searching Algorithms:**

    - Examples: Naive Pattern Searching, Rabin-Karp Algorithm
    - Description: Pattern searching is an important problem in computer science. When we do search for a string in notepad/word file or browser or database, pattern searching algorithms are used to show the search results. Naive Pattern Searching is the simplest method among all the pattern searching algorithms. The idea is to slide the pattern over text one by one and check for a match. If a match is found, then slides by 1 again to check for subsequent matches. The Rabin-Karp algorithm is a string-searching algorithm that uses hashing to find any one of a set of pattern strings in a text. For text of length n and p patterns of combined length m, its average and best case running time is O(n+m) in space O(p), but its worst-case time is O(nm).

11. **Sorting Algorithms:**

    - Examples: Bubble Sort, Insertion Sort
    - Description: Sorting algorithms are used to rearrange a given array or list elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of element in the respective data structure. For example, Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

12. **String Algorithms:**

    - Examples: Longest Common Substring, Longest Common Prefix
    - Description: String algorithms are algorithms that work on strings. In particular, string algorithms are often designed to work with strings that contain special symbols, such as the empty string or whitespace, which are not usually allowed to appear in string searches. The longest common substring problem is to find the longest string (or strings) that is a substring (or are substrings) of two or more strings. The longest common prefix (LCP) problem is to find the longest string (or strings) that is a prefix (or are prefixes) of two or more strings.

13. **Mathematical Algorithms:**

    - Examples: Sieve of Eratosthenes, Euclidean Algorithm
    - Description: Mathematical algorithms are those algorithms which perform computations and process data related to mathematics. The sieve of Eratosthenes is a simple, ancient algorithm for finding all prime numbers up to any given limit. It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the first prime number, 2. The Euclidean algorithm, or Euclid's algorithm, is an efficient method for computing the greatest common divisor (GCD) of two integers (numbers), the largest number that divides them both without a remainder. It is named after the ancient Greek mathematician Euclid, who first described it in his Elements (c. 300 BC).

14. **Bit Manipulation Algorithms:**

    - Examples: Bit Counting, Bit Reversal
    - Description: Bit manipulation is the act of algorithmically manipulating bits or other pieces of data shorter than a byte. C language is very efficient in manipulating bits. Bit Counting is the procedure of counting the number of set bits (1s) in a binary string. Bit Reversal is the procedure of reversing the order of bits in a binary string.

15. **Operating System Algorithms:**

    - Examples: Page Replacement Algorithms, Disk Scheduling Algorithms
    - Description: Operating system algorithms are those algorithms which perform computations and process data related to operating systems. Page Replacement Algorithms are the techniques using which an Operating System decides which memory pages to swap out, write to disk when a page of memory needs to be allocated. Disk Scheduling Algorithms are the algorithms which are used to decide which disk block to access next after a disk operation request has been issued.

16. **Miscellaneous Algorithms:**
    - Examples: Tower of Hanoi, Josephus Problem
    - Description: Miscellaneous algorithms are those algorithms which do not fall into any of the above categories. The Tower of Hanoi is a mathematical game or puzzle. It consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape. The Josephus problem is a theoretical problem related to a certain counting-out game. People are standing in a circle waiting to be executed. Counting begins at a specified point in the circle and proceeds around the circle in a specified direction. After a specified number of people are skipped, the next person is executed. The procedure is repeated with the remaining people, starting with the next person, going in the same direction and skipping the same number of people, until only one person remains, and is freed.

## LICENSE

[MIT](LICENSE)
