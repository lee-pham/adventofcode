const fs = require('fs');
const fileName = 'input.txt';

function calculateFuel(mass) {
  return Math.floor(mass/3) - 2;
}


function advancedCalculateFuel(mass) {
  total = 0;
  delta = calculateFuel(mass);
  while (delta >= 0) {
    total += delta;
    delta = calculateFuel(delta);
  }
  return total;
}


fs.readFile(fileName, 'utf8', function(err, data) {
  if (err) throw err;
  const masses = data.split('\n').map(x => parseInt(x));
  masses.pop();
  let part1 = 0;


  for (let i = 0; i < masses.length; i++) {
    part1 += calculateFuel(masses[i])
  }
  console.log(part1);

  let part2 = 0;
  for (let i = 0; i < masses.length; i++) {
    part2 += advancedCalculateFuel(masses[i]);
  }
  console.log(part2);
});