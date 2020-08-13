"""
Mission 3: Find a word in a crossword (horizontal & vertical).
Write a function named capitalize_word_in_crossword that accepts a 2-dimensional list of characters
(like a crossword puzzle) and a string (word) as input arguments. This function searches the rows
and columns of the 2d list to find a match for the word. If a match is found, this functions
capitalizes the matched characters in 2-dimensional list and returns the list. If no match is found,
this function simply returns the origianl 2-dimensional list with no modification.
"""

def find_word_horizontal(crosswords, word):
    char = 0
    res = ""
    for row in range(len(crosswords)):
        for column in range(len(crosswords[row])):
#            print(row, column, crosswords[row][column])
            if crosswords[row][column] == word[char]:
                res = res + crosswords[row][column]
#                print(res,'=', word,"?")
                if res == word:
                    return [row, column]
                else:
                    n = 1
                    for col1 in range(len(crosswords[row])):
                        col1 = column + n
#                        print(res, '=', word, "?")
                        if col1 > len(crosswords[row]) - 1:
                            res = ""
                            break
                        if crosswords[row][col1] == word[char+n]:
                            res = res + crosswords[row][col1]
#                            print(res, '=', word, "?")
                            if res == word:
                                return [row, column]
                            else:
                                n = n + 1
                        else:
                            res = ""
                            break
    return None

def find_word_vertical(crosswords, word):
    char = 0
    res = ""
    for row in range(len(crosswords)):
        for column in range(len(crosswords[row])):
#            print(row, column, crosswords[row][column])
            if crosswords[row][column] == word[char]:
                res = res + crosswords[row][column]
#                print(res,'=', word,"?")
                if res == word:
                    return [row, column]
                else:
                    n = 1
                    for row1 in range(len(crosswords)):
                        row1 = row + n
#                        print(res, '=', word, "?")
                        if row1 > len(crosswords) - 1:
                            res = ""
                            break
                        if crosswords[row1][column] == word[char+n]:
                            res = res + crosswords[row1][column]
#                            print(res, '=', word, "?")
                            if res == word:
                                return [row, column]
                            else:
                                n = n + 1
                        else:
                            res = ""
                            break
    return None

def capitalize_word_in_crosswords(crosswords, word):
    position = find_word_horizontal(crosswords,word)
#    print(position)
    if position != None:
        row = position[0]
        column = position[1]
        for char in word:
            crosswords[row][column] = chr(ord(crosswords[row][column]) - 32)
            column = column + 1
        return crosswords
    else:
        position = find_word_vertical(crosswords, word)
#        print(position)
        if position != None:
            row = position[0]
            column = position[1]
            for char in word:
                crosswords[row][column] = chr(ord(crosswords[row][column]) - 32)
                row = row + 1
            return crosswords
        else:
            return crosswords

crosswords = [['f', 'd', 'g', 'c','a','t',"e"],
              ['i', 'f', 'i', 's','d','w',"r"],
              ['d', 'i', 'l', 'i','o','n',"l"],
              ['h', 's', 'i', 'a','g','n',"i"],
              ['a', 'h', 's', 't','s','g',"e"],
              ['t', 'u', 'r', 't','l','e',"n"],
              ['f', 'o', 'x', 'd','o','f',"q"]]


for r in range(len(crosswords)):
    row = ""
    for c in range(len(crosswords[r])):
        row = row + crosswords[r][c] + "  "
    print(row)
print("\nSearch animals in the crosswords.\n(cat, dog, fish, fox, lion, turtle)\n")
word = input("find an animal in the crosswords: ")
crosswords_solve = capitalize_word_in_crosswords(crosswords, word)

for r in range(len(crosswords_solve)):
    row = ""
    for c in range(len(crosswords_solve[r])):
        row = row + crosswords_solve[r][c] + "  "
    print(row)
