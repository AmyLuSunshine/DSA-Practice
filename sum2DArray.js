// function sumArray(arr, start, end){
//     let final = arr[end]
//     let length = end - start + 1
//     let sum = 0
//     for(let iLoop=start; iLoop < length; iLoop++) {
//         sum += arr[iLoop]
//     }
//     return sum;
// }



//6/15/2026 - Jessica

// function sum2DArray(arr) {
//     let sum = 0
//     for(let i=0; i<arr.length; i++){
//         for(let j=0; j<arr[i].length; j++){
//             sum += arr[i][j]
//         }
//     }
//     return sum
// }

// console.log(sum2DArray([[1,2],[3,4]]))
// console.log(sum2DArray([[1,1],[1,1]]))


// function recurionSum2DArray(arr, i, j){
//     let sum = 0
//     //base case
//     if(arr.length === 1 && arr[0].length === 1)
//         return sum

//     //recursive call
    
//     let i = arr.length
//     let j = arr[i].length
//     return sum + 

//     return (recurionSum2DArray(arr[i++][j++],))
// }

// function recurionSum2DArray(arr, i, j){
//     let sum = 0
//     let i = arr.length
//     let j = arr[i].length

//     //base case
//     if(i === arr.length-1 && j === arr[i].length)
//         return arr[i][j]

//     //recursive call
//     sum += arr[i][j]
   
//     return (recurionSum2DArray(arr,i++,j++))
// }

//arr[0]
function arrRecursionSum (arr){
    let sum = 0;
    //base case
    if(!Array.isArray(arr)){
        sum += arr
    }
    //recursive case
    //arr[0][0]
    else{
        for(let i=0; i<arr.length; i++){
            arrRecursionSum(arr[i])
            sum += arrRecursionSum(arr[i])
        }
    }
    return sum
}

console.log("recursion")
console.log(arrRecursionSum([[1]]))
console.log(arrRecursionSum([[1,1]]))
console.log(arrRecursionSum([[1,2],[2,3]]))
