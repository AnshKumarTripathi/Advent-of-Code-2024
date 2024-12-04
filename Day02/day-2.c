#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MAX_REPORTS 10000
#define MAX_LEVELS 10

bool isSafeReport(int report[], int size)
{
  bool increasing = true;
  bool decreasing = true;
  for (int i = 0; i < size - 1; i++)
  {
    int diff = report[i + 1] - report[i];
    if (!(abs(diff) >= 1 && abs(diff) <= 3))
    {
      return false;
    }
    if (diff > 0)
    {
      decreasing = false;
    }
    else if (diff < 0)
    {
      increasing = false;
    }
  }
  return increasing || decreasing;
}

int readReportsFromFile(const char *filename, int reports[MAX_REPORTS][MAX_LEVELS])
{
  FILE *file = fopen(filename, "r");
  if (file == NULL)
  {
    perror("Error opening file");
    return -1;
  }

  char line[256];
  int reportCount = 0;
  while (fgets(line, sizeof(line), file) && reportCount < MAX_REPORTS)
  {
    char *token = strtok(line, " ");
    int levelCount = 0;
    while (token != NULL && levelCount < MAX_LEVELS)
    {
      reports[reportCount][levelCount++] = atoi(token);
      token = strtok(NULL, " ");
    }
    reportCount++;
  }

  fclose(file);
  return reportCount;
}

int main()
{
  const char *filename = "D:/Advent-of-code-2024/Advent-of-Code-2024/Day02/input.txt";
  int reports[MAX_REPORTS][MAX_LEVELS];
  int reportCount = readReportsFromFile(filename, reports);

  if (reportCount == -1)
  {
    return 1;
  }

  int safeCount = 0;
  for (int i = 0; i < reportCount; i++)
  {
    if (isSafeReport(reports[i], MAX_LEVELS))
    {
      safeCount++;
    }
  }

  printf("Number of safe reports: %d\n", safeCount);
  return 0;
}
