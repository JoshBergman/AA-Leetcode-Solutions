// Things I learned in this problem:
// 1. Math.trunc
// 2. What reverse polish notation is

// This problem was a cool opportunity to use high-order functions
// The solution is pretty self-explanatory, although I did have to watch a video
// on a solution to figure out what reverse polish notation was, I also used chatGPT to
// find the Math.trunc method for truncating towards zero.

/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
  const stack = [];
  for (let i = 0; i < tokens.length; i++) {
    const currToken = evalChar(tokens[i]); //number or function to eval operator

    if (typeof currToken === "number") {
      stack.push(currToken);
    } else {
      const val2 = stack.pop();
      const val1 = stack.pop();
      stack.push(currToken(val1, val2));
    }
  }

  return stack[0];

  function evalChar(char) {
    // returns high-order function for operators and returns the number for non-operators
    switch (char) {
      case "+":
        return (x, y) => x + y;
      case "-":
        return (x, y) => x - y;
      case "*":
        return (x, y) => x * y;
      case "/":
        return (x, y) => Math.trunc(x / y);
      default:
        return parseInt(char);
    }
  }
};
