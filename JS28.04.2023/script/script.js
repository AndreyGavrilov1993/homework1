//! #1

function except(first, second) {
    let set = [], result = [], count = first.length, count2 = second.length;
    
    for (let i = 0; i < count2; ++i) {
        let item = second[i];
        if (!set.some(e => e === item))
            set.push(item);
    }
    for (let i = 0; i < count; ++i) {
        let item = first[i];
        if (!set.some(e => e === item)) {
            set.push(item);
            result.push(item);
        }
    }
    return result;
}
 
function getDifferences(array1, array2) {
    return except(array1, array2).concat(except(array2, array1));
}
 
console.log(getDifferences([1, 2, 3, 4], [2, 3, 6, 8]));
console.log(getDifferences([1, 6, 3, 4], [1, 3, 7, 4]));
console.log(getDifferences([1, 2, 3], [4, 5, 6, 7]));
console.log(getDifferences([1, 2], [5, 2, 8, 7]));

//! #2
/*
const array1 = [3, 5, 7, 8, 2];
const array2 = [6, 8, 3, 9];
const array3 = [];

array1.concat(array2).forEach(function(item) {
    array3[item] = true;
});
let result = Object.keys(array3);
console.log(result);
*/