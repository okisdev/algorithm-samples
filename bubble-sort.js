function bubbleSort(arr) {
    let len = arr.length;

    for (let i = 0; i < len - 1; i++) {
        for (let j = 0; j < len - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
            }
        }
    }

    return arr;
}

// Testing
let arr = [5, 4, 3, 2, 1];

console.log(bubbleSort(arr)); // [1, 2, 3, 4, 5]
