function find_inversion_count(nums) {
  const n = nums.length;
  let c = 0;
  for (let i = 0; i < n - 2; i++) {
    for (let j = i + 1; j < n - 1; j++) {
      for (let k = j + 1; k < n; k++) {
        if (nums[i] > nums[j] && nums[j] > nums[k]) {
          c++;
        }
      }
    }
  }

  return c;
}

console.log(find_inversion_count([9, 4, 3, 5, 1]));
