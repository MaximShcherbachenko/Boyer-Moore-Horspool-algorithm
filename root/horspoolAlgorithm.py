userText = input("Enter the text:\n")   # user input Text
userPattern = input("Enter the pattern:\n")  # user input pattern

valueTable = {}  # dictionary for values for table
counter = len(userPattern) - 1
counter_1 = 0


# creating the table of rolls
for i in range(0, len(userPattern) - 1):
    valueTable[userPattern[i]] = counter
    counter -= 1

# print table of rolls
print("Rolls table:\n", valueTable, "\n")


# Realization of algorithm
textPointer = 0
while textPointer < (len(userText) - len(userPattern) + 1):
    if len(userText) - len(userPattern) != 0:
        flag = 0  # quantity match

        # gui
        print(userText)
        print(" " * textPointer + userPattern + "\n")

        # realization
        for patternPointer in range(len(userPattern)):
            if userText[textPointer + patternPointer] == userPattern[patternPointer]:
                flag += 1
            elif str(userText[textPointer + len(userPattern) - 1]) in valueTable.keys():
                textPointer += valueTable[userText[textPointer + len(userPattern) - 1]]
                break
            else:
                textPointer += len(userPattern)
                break
        # prerequisite check
        if flag == len(userPattern):
            counter_1 = textPointer
            break
    else:
        print("No matches:(\n")
        break

print("\n\n")

# print the result
if counter_1 != 0:
    print("Start position of the pattern =", counter_1)
else:
    print("No matches:(\n")
