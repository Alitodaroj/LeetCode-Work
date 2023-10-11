/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let sums = 0;
    let totalSums = [];
    for(let i of nums) {
        sums += i;
        totalSums.push(sums);
    }
    return totalSums;

}