#WordCount.py
#Name: Sienna Bonner
#Date: 2/25/26
#Assignment: Lab 6

def main():
  filename = input("Enter filename: ")

  try:
    textFile = open(filename, 'r')
  except FileNotFoundError:
    print("Error: file not found.")
    return

  lineCount = 0
  wordCount = 0
  letterCount = 0 

  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1
    letterCount = letterCount + len(line)

  print("Lines:", lineCount)
  print("Words:", wordCount)
  print("Characters:", letterCount)
  

if __name__ == '__main__':
  main()
