function bubble_sort(nums) {
  for (let k = 0; k < nums.length; k++) {
    for (let i = 0; i < nums.length; i++) {
      if (nums[i] > nums[i + 1]) {
        [nums[i], nums[i + 1]] = [nums[i + 1], nums[i]];
      }
    }
  }

  return nums;
}

console.log(bubble_sort([3, 5, 8, 4, 1, 9, -2]));
