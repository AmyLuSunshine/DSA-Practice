//OH 5 - Sherry
// Reminder: complete the requirements AJ emailed everyone regarding the Agreement and
// the TTP Checkpoint 1, as a way to maintain active status in the program
// Given two arrays, determine whether they contain the same values in the same order.

// -----------my first try-------------- too abundant psedocode
// JS
// same values []
// same order, for loop

/* arr1[]
arr2[]

Arr1.length !== Arr1.length
	return false
Length = Arr1.length
for(let i=0, i<length, i++){
	If Arr1[i] !== arr2[2];
	  False
    Return true
}

123
123 */

//—-- feedback: make sure the psudo code is psudo code, short and clear
/* 
Output boolean
Length check
For loop loop over each element to check arr1 === arr2, 
return false if any diff
Return true after loop is done
 */
//—-------------------------

function isSameArray(arr1, arr2) {
  if (arr1.length !== arr2.length) return false;

  const length = arr1.length;
  for (let i = 0; i < length; i++) {
    if (arr1[i] !== arr2[i]) return false;
  }
  return true;
}

// big O of n. because it loop through all the elements of the arrayk
