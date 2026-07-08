/* 
given an array of numbers, return average(arithmetic mean) of all the elements in the array.

const arr = [2, 4, 6]; // 4
const arr1 = [5, 5, 5, 5]; //5
const arr2 = [1, 2, 3, 4]; //2.5

loop through all elements adds up together
result divide by array length
*/

function averageArray(arr) {
  const length = arr.length;
  let sum = 0;

  for (let i = 0; i < length; i++) {
    sum += arr[i];
  }

  const average = sum / length;

  return average;
}

console.log(averageArray([2, 4, 6]));
console.log(averageArray([5, 5, 5, 5]));
console.log(averageArray([1, 2, 3, 4]));

//array.prototype.reduce() method ???
