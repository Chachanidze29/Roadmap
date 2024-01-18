// This can be implemented using set data structure with 1 line
// but I was too dumb to think of it
// we can insert all items in set and compare length of nums and set
// if they differ that means there was duplicate and we return true

function contains_duplicate(nums) {
  const map = {};
  for (let i = 0; i < nums.length; i++) {
    if (!map[nums[i]]) {
      map[nums[i]] = 1;
    } else {
      map[nums[i]] += 1;
    }
  }

  for (const prop in map) {
    if (map[prop] > 1) {
      return true;
    }
  }

  return false;
}

contains_duplicate([1, 1, 2, 3, 4, 5]);
