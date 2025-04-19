/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumPairRemoval = function(nums) {
    if (nums.length <= 1) return 0;
    
    let j = 0;
    
    function isSorted(arr) {
        for (let i = 1; i < arr.length; i++) {
            if (arr[i - 1] > arr[i]) return true;
        }
        return false;
    }
    
    while (isSorted(nums)) {
        let minSum = Infinity;
        let index = 0;
        for (let k = 0; k < nums.length - 1; k++) {
            let sum = nums[k] + nums[k + 1];
            if (sum < minSum) {
                minSum = sum;
                index = k;
            }
        }
        nums.splice(index, 2, minSum);
        j++;
    }
    
    return j;
};