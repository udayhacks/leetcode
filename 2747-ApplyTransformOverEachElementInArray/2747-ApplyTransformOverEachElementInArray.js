// Last updated: 04/04/2026, 13:11:40
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */

var map = function(arr, fn) {
    for (let i =0 ; i<arr.length;i++){
        arr[i] = fn(arr[i],i);
    }
    return arr;
};