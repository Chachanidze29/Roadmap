function select_activity(nums) {
  nums.sort(function (a, b) {
    return a[1] - b[1];
  });

  const set = [nums[0]];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i][0] >= set[set.length - 1][1]) {
      set.push(nums[i]);
    }
  }

  return set;
}

console.log(
  select_activity([
    [4, 5],
    [1, 2],
    [1, 5],
    [3, 4],
  ])
);
