emojidict = {
    "😀" : ["smiley","happy", "glad", "happiness"],
    "😍" : ["lovely","love","love eyes","happy"],
    "😇" : ["shy"],
    "😎" : ["cool"],
}


emojifound = ""
output = ""
query = input("Key in your paragraph: ").split() #splits words in the sentence into a list with each word. 

for thisword in query:
    for key in list(emojidict): #arranges the keys as a list and iterates thru them
        if (thisword in emojidict[key]): #search if the query matches any keywords in each list
            print(thisword + " found in " + key)
            emojifound += key
        else:
            print(thisword + " not found in " + key)
    output += thisword + " " + emojifound
    emojifound = "" #reinitialize
print(output)