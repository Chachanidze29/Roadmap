function insertion_sort(nums) {
  for (let i = 1; i < nums.length; i++) {
    let j = i;
    while (j > 0 && nums[j] < nums[j - 1]) {
      [nums[j], nums[j - 1]] = [nums[j - 1], nums[j]];
      j--;
    }
  }

  return nums;
}

console.log(insertion_sort([3, 8, 5, 4, 1, 9, -2]));
