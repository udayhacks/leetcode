// Last updated: 04/04/2026, 13:11:42
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let ar = []
    for (let i = 0 ; i <arr.length;i++){
        if (fn(arr[i],i)){
         ar.push(arr[i]);
        }
    }
    return ar;
};