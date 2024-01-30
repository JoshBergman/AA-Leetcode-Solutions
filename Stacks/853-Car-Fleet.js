// For this problem I spent a lot of time whiteboarding the solution.
// While the logic in the end isnt too complicated it requires
// a fair amount of forethought to break this problem down into an algorithm

// A unique and challenging problem that was fun to solve!

/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function (target, position, speed) {
  const pos_speed = position.map((pos, index) => [pos, speed[index]]);
  pos_speed.sort((a, b) => {
    //sort by position then speed (position == index 0, speed == index 1)
    if (a[0] !== b[0]) {
      return b[0] - a[0];
    }
    return b[1] - a[1];
  });

  const timeToTarget = (position, speed) => {
    const distanceLeft = target - position;
    return distanceLeft / speed;
  };

  const carsLength = position.length;
  let fleets = 1;
  let fleetTimeToTarget = timeToTarget(pos_speed[0][0], pos_speed[0][1]);

  for (let i = 0; i < carsLength; i++) {
    //get time to target for current car
    let time = timeToTarget(pos_speed[i][0], pos_speed[i][1]);
    if (time <= fleetTimeToTarget) {
      continue;
    } else {
      fleets += 1;
      fleetTimeToTarget = time;
    }
  }

  return fleets;
};
