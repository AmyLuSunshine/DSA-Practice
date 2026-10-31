// OH 4
/* car -> rac : false
racecar -> racecar : true
racecar
new arr[], go backwards of for loop,
arr === newArr

cleaner approach is to compare the original string with its reversed version,
or compare characters from both ends */
//----------------------------------------------

// method 1: compare two array, using method split("") and reverse(), join("")
/* const string = "racecar";

function isPalindrome(string) {
  const charsStringArray = string.split(""); //['r', 'a', 'c','e', 'c', 'a', 'r']
  const reversedStringArray = [...string].reverse();

  // return method 1:
  return charsStringArray.join("") === reversedStringArray.join("");

return method 2:
  if (charsStringArray.join("") === reversedStringArray.join("")) {
    return true;
  } else {
    return false;
  } */

/* return method 3... not recommended
Ternary operator, if you have to use ternary ... === comparison already gives a boolean
return is a statement, and ternary branches need expressions */
/*   return charsStringArray.join("") === reversedStringArray.join("")
    ? true
    : false; */

// ----------------------------------------------------
// method 2.1: compare two array, then compare two string

/* function isPalindrome(string) {
  let stringArray = [];
  let backStringArray = [];

  let length = string.length;
  for (let i = length - 1; i >= 0; i--) {
    const item = string[i];
    backStringArray.push(item); // backStringArray[length - 1 - i] = item;//backStringarray[0] = string[6]
    stringArray[i] = string[i]; // forward string, [6] = string[6];
  }
  //backString = backString.toString();// X toString() keeps the commas between array items.

  return backStringArray.join("") === stringArray.join(""); //convert arrays to string then compare

  //return backStringArray === stringArray;
  // no, With arrays, === compares whether both variables point to the exact same array object in memory,
  // not whether they contain the same items.
  // So:
  // two different arrays with the same values are not equal with ===
  // ,the same array variable compared to itself is true
}
console.log(isPalindrome("racecar")); */

// ----------------------------------------------------
// method 2.2: compare two string, string[] index

/* function isPalindrome(string) {
  let backString = "";

  const length = string.length;
  for (let i = length - 1; i >= 0; i--) {
    backString += string[i];
  }
  // if (backString === string)
  //   return true;
  // else
  //   return false;

  // simply return the result of true or false
  return backString === string;
}
console.log(isPalindrome("racecar")); */

// ----------------------------------------------------
// method 3: compare both end, left and right match or not

let word1 = "racecar";
let word2 = "yangmei";
// [r,a,c,e,c,a,r]
function problem(word) {
  const arr = word.split("");
  console.log(arr);
  console.log("--------");
  for (let i = 0; i < arr.length / 2; i++) {
    if (arr[i] !== arr[arr.length - 1 - i]) {
      console.log(arr[i], arr[arr.length - 1 - i]);
      return false;
    }
  }
  return true;
}

console.log(problem(word1));
console.log(problem(word2));
console.log(problem("level")); //true
console.log(problem("hello")); //false

// string.length, is not byte count.
console.log("racecar".length); // 7
console.log("a".length); // 1
console.log("😀".length); // 2

/* function isPalindrome(array) {
  let left = 0;
  let right = array.length - 1;

  while (left !== right) {
    if (array[left] !== array[right]) {
      return false;
    }
    left++;
    right--;
  }
  return true;
} */
