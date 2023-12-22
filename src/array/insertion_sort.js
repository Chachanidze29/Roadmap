function insertion_sort(nums) {
  const n = nums.length;
  for (let i = 0; i < n; i++) {
    const value = nums[i];
    let j = i;
    while (j > 0 && nums[j - 1] > value) {
      nums[j] = nums[j - 1];
      j--;
    }
    nums[j] = value;
  }

  return nums;
}

console.log(insertion_sort([3, 8, 5, 4, 1, 9, -2]));
