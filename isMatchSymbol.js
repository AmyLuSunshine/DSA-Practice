/* 

Problem: Determine whether all parentheses, brackets, and braces are properly matched.

Examples
()[]{}→true
([])→true
(]→false

Stack:
first in last out

thinking process:
we have a string of symbol input, [({[})], 
loop over each
 push opens to stack [ ( { if statement
else:
    
        if strArr[i] is } and  stack[len-1] is {
        stack will pop // it's a match: 
        if else strArr[i] is ] and  stack[len-1] is [
        stack will pop 
        if else strArr[i] is ) and  stack[len-1] is (
        stack will pop 
        else
            return false
if (stack.length() !== 0 )        
    return false;
return true;

*/

function isMatchSymbol(strArr) {
  let stack = [];

  for (let i = 0; i < strArr.length; i++) {
    if (
        strArr[i] === "[" || 
        strArr[i] === "{" || 
        strArr[i] === "("
    ) {
      stack.push(strArr[i]);
    } else if (stack.length !== 0) {
      if (
        (strArr[i] === "}" && stack[stack.length - 1] === "{") ||
        (strArr[i] === "]" && stack[stack.length - 1] === "[") ||
        (strArr[i] === ")" && stack[stack.length - 1] === "(")
      ) {
        stack.pop();
      } else {
        // Closing bracket doesn't match the most recent opening bracket ([)]
        return false;
      }
    } else {
        // Closing bracket when the stack is empty
      return false;
    }
  }

  if (stack.length !== 0) {
    return false;
  }
  return true;
}

console.log(isMatchSymbol("()[]{}")); // true
console.log(isMatchSymbol("([])"));   // true
console.log(isMatchSymbol("(]"));     // false
console.log(isMatchSymbol("([)]"));   // false
console.log(isMatchSymbol("([}])"));  // false