function right_rotate_k(nums, k = 1) {
  for (let j = 0; j < k; j++) {
    right_rotate(nums);
  }

  return nums;
}

function right_rotate(nums) {
  const n = nums.length;
  const last = nums[n - 1];

  for (let i = n - 2; i >= 0; i--) {
    nums[i + 1] = nums[i];
  }

  nums[0] = last;
}

console.log(right_rotate_k([1, 2], 3));
