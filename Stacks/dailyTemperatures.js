// I am going to start using javascript to do these problems as its the only lang I use now days
// For this problem I resorted to a neetcode video as I only could come up with
// two - pointers or a nested loop which arent ideal for this

// This solution uses a Monotonic decreasing stack (fancy way to say a stack with decreasing values)
// very clever solution and a great tool to add to my data structures knowledge

/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
  const result = temperatures.map(() => 0);
  const stack = []; //holds pairs ex: [temp, index][]

  for (let i = 0; i < temperatures.length; i++) {
    while (stack.length > 0 && temperatures[i] > stack[stack.length - 1][0]) {
      const [temp, index] = stack.pop();
      result[index] = i - index;
    }
    stack.push([temperatures[i], i]);
  }

  return result;
};
