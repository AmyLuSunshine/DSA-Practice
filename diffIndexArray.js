/* 

return the first mismatch index in two arrays, 
return -1 if they are identical

Example:
[1,2,3], [1,2,4] -> 2
[1,2,3], [1,2,3] -> -1
[1,2,3], [1,2]   ->-1

// psudo code
get min length
for loop iterate each element of two array
if - return i when arr1 and arr2 at index [i] mismatch
return -1 if same

math 
math math
ctrl + d - short cut to edit same name at the same time
*/

function diffIndexArray(arr1, arr2) {
  let length = Math.min(arr1.length, arr2.length); // O(1)-(no spread) ； O(N)-(when spread ... array)

  /* if (arr1.length < arr2.length) {
    // if else arr.length compare is O(1)
    length = arr1.length;
  } else {
    length = arr2.length;
  } */
  for (let i = 0; i < length; i++) {
    if (arr1[i] !== arr2[i]) {
      return i;
    }
  }
  return -1;
}

console.log(diffIndexArray([1, 2, 3], [1, 2, 4]));
console.log(diffIndexArray([1, 2, 3], [1, 2, 3]));
console.log(diffIndexArray([1, 2, 3], [1, 2]));
