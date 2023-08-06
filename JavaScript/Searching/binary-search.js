function binary_search(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (arr[mid] === target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

// Testing
let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
target = 5;

if (binary_search(arr, target) === -1) {
    console.log('Not found');
} else {
    console.log('Found ' + target + ' at index ' + binary_search(arr, target));
}
