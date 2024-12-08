let pages = [];
let allPages = new Set();
let positions = {};
let dependencies = {};
let updateIndex = 0;
let step = 0;
let maxSteps = 0;
let validUpdates = [];
let middlePages = [];
let sortingDone = false;

document
  .getElementById("fileInput")
  .addEventListener("change", handleFile, false);

function handleFile(event) {
  const file = event.target.files[0];
  const reader = new FileReader();
  reader.onload = function (event) {
    const text = event.target.result;
    processInput(text);
  };
  reader.readAsText(file);
}

function processInput(text) {
  const lines = text.trim().split("\n");
  const separatorIndex = lines.indexOf("");
  const rules = lines.slice(0, separatorIndex);
  const updates = lines
    .slice(separatorIndex + 1)
    .map((line) => line.split(",").map(Number));

  dependencies = buildDependencies(rules);
  validUpdates = updates.filter((update) => isCorrectOrder(update));

  // Add all pages from updates to the set
  updates.forEach((update) => update.forEach((page) => allPages.add(page)));

  if (validUpdates.length > 0) {
    updateIndex = 0;
    step = 0;
    sortingDone = false;
    setupCanvas(validUpdates[updateIndex]);
  } else {
    document.getElementById("result").innerText = "No valid updates found.";
  }
}

function buildDependencies(rules) {
  const deps = {};
  rules.forEach((rule) => {
    const [before, after] = rule.split("|").map(Number);
    if (!deps[after]) deps[after] = new Set();
    deps[after].add(before);
  });
  return deps;
}

function isCorrectOrder(update) {
  const positions = {};
  update.forEach((page, index) => (positions[page] = index));

  for (const [after, befores] of Object.entries(dependencies)) {
    if (positions.hasOwnProperty(after)) {
      for (const before of befores) {
        if (
          positions.hasOwnProperty(before) &&
          positions[before] > positions[after]
        ) {
          return false;
        }
      }
    }
  }
  return true;
}

function setupCanvas(update) {
  pages = [...allPages]; // Display all pages including those not in the current update
  maxSteps = update.length;
  positions = {};
  update.forEach((page, index) => {
    positions[page] = index;
  });
  updateCanvas();
}

function updateCanvas() {
  createCanvas(1500, 800).parent("canvasContainer");
  background(255);
  fill(0);
  textSize(24);
  textAlign(CENTER, CENTER);
  const gridSize = Math.ceil(Math.sqrt(pages.length));
  const cellSize = width / gridSize;

  pages.forEach((page, index) => {
    const x = (index % gridSize) * cellSize + cellSize / 2;
    const y = Math.floor(index / gridSize) * cellSize + cellSize / 2;
    if (positions.hasOwnProperty(page)) {
      fill(positions[page] === index ? "green" : "red");
    } else {
      fill("black"); // Pages not in the current update
    }
    text(page, x, y);
  });
}

function draw() {
  if (!sortingDone && validUpdates.length > 0) {
    const update = validUpdates[updateIndex];
    if (step < maxSteps - 1) {
      if (positions[update[step]] > positions[update[step + 1]]) {
        [positions[update[step]], positions[update[step + 1]]] = [
          positions[update[step + 1]],
          positions[update[step]],
        ];
        [update[step], update[step + 1]] = [update[step + 1], update[step]];
      }
      step++;
      updateCanvas();
    } else {
      step = 0;
      const middlePage = update[Math.floor(update.length / 2)];
      middlePages.push(middlePage);
      updateIndex++;
      if (updateIndex >= validUpdates.length) {
        sortingDone = true;
        const sumOfMiddlePages = middlePages.reduce((acc, val) => acc + val, 0);
        document.getElementById(
          "result"
        ).innerText = `Sorting completed. Sum of middle pages: ${sumOfMiddlePages}`;
      } else {
        setupCanvas(validUpdates[updateIndex]);
      }
    }
  }
}
