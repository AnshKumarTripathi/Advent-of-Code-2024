const fs = require("fs");

function isSafeReport(report) {
  let increasing = true;
  let decreasing = true;
  for (let i = 0; i < report.length - 1; i++) {
    let diff = report[i + 1] - report[i];
    if (!(Math.abs(diff) >= 1 && Math.abs(diff) <= 3)) {
      return false;
    }
    if (diff > 0) {
      decreasing = false;
    } else if (diff < 0) {
      increasing = false;
    }
  }
  return increasing || decreasing;
}

function readReportsFromFile(filename) {
  const data = fs.readFileSync(filename, "utf8");
  const lines = data.split("\n").filter((line) => line.trim() !== "");
  return lines.map((line) => line.split(" ").map(Number));
}

const filename = "D:/Advent-of-code-2024/Advent-of-Code-2024/Day02/input.txt";
const reports = readReportsFromFile(filename);

let safeCount = 0;
for (let report of reports) {
  if (isSafeReport(report)) {
    safeCount++;
  }
}

console.log("Number of safe reports:", safeCount);
