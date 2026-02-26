#WordIndex.py
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

  words = {} #create an empty dictionary
  lineNum = 0

  for line in textFile:
    lineNum = lineNum + 1
    wordList = line.split()

    for w in wordList:
      w = w.lower()
      w = w.replace("," , "")
      w = w.replace("." , "")
      w = w.replace("!" , "")
      
      words.setdefault(w, [])  
      if lineNum not in words[w]:
        words[w].append(lineNum)

  for word in words:
    print(word, words[word])

if __name__ == '__main__':
  main()
