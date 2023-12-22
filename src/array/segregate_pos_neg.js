function segregate(nums) {
  let pIndex = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] < 0) {
      [nums[i], nums[pIndex]] = [pIndex, nums[i]];
      pIndex++;
    }
  }

  return nums;
}

console.log(segregate([9, -3, 5, -2, -8, -6, 1, 3]));
