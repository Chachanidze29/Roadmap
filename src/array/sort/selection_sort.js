function selection_sort(nums) {
  for (let i = 0; i < nums.length; i++) {
    let min = i;
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] < nums[min]) {
        min = j;
      }
    }

    [nums[min], nums[i]] = [nums[i], nums[min]];
  }

  return nums;
}

console.log(selection_sort([3, 5, 8, 4, 1, 9, -2]));
