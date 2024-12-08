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

  // Parse rules into a graph format
  const dependencies = new Map();
  rules.forEach((rule) => {
    const [before, after] = rule.split("|").map(Number);
    if (!dependencies.has(after)) dependencies.set(after, new Set());
    dependencies.get(after).add(before);
  });

  function isUpdateValid(update) {
    const position = new Map();
    update.forEach((page, index) => position.set(page, index));

    for (let [after, befores] of dependencies.entries()) {
      if (position.has(after)) {
        for (let before of befores) {
          if (
            position.has(before) &&
            position.get(before) > position.get(after)
          ) {
            return false;
          }
        }
      }
    }
    return true;
  }

  // Check each update and find the middle page
  const validUpdates = updates.filter(isUpdateValid);
  const middlePages = validUpdates.map(
    (update) => update[Math.floor(update.length / 2)]
  );
  const result = middlePages.reduce((acc, val) => acc + val, 0);

  document.getElementById(
    "result"
  ).innerText = `The sum of the middle pages from correctly ordered updates is: ${result}`;
}
