print("palindrome detector")

#preparing to disregard special characters
from string import punctuation
special = []
for i in range(len(punctuation)):
  special.append(punctuation[i])

while True:
  #user inserts word (disregarding spaces/special characters)
  print()
  word = input("enter a word, number, or phrase: ").replace(" ", "")

  for i in range(len(special)):
    word = word.replace(special[i],"")

  #character lists
  allCharacters = []
  firstHalf = []
  secondHalf = []

  allCharacters = list(word)

  #if odd number of characters, disregard middle letter
  if len(word) % 2 != 0:
    allCharacters.remove(allCharacters[int((((len(allCharacters))/2)-0.5))])

  #split character into two even lists
  for i in range(int(len(allCharacters)/2)):
    firstHalf.append(allCharacters[i])

  for i in range(int(len(allCharacters)/2),len(allCharacters)):
    secondHalf.append(allCharacters[i])

  #reverse order of list 2
  secondHalf.reverse()

  #check if they match
  if firstHalf == secondHalf:
    print("palindrome detected!")
  else:
    print("not a palindrome :(")