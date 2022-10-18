translate_dict = {}
dictionary = input("Please enter words in this format <palabra>:<traducción> and divided by commas: ")
list_of_pairs = dictionary.split(",")
#print(list_of_pairs)
#['Hola:Hello', 'Adios:Bye', 'Como:How']
for pair in list_of_pairs:
    word = pair.split(":")
    #print(word)
    #['Hola', 'Hello']
    #['Adios', 'Bye']
    #['Como', 'How']
    key = word[0]
    value = word[1]
    translate_dict[key] = value

phrase = input("Please enter a phrase to translate: ")
list_of_words = phrase.split(" ")
translated_words = ""
for word in list_of_words:
    translated_words += translate_dict.get(word,word)
    translated_words += " "
print(translated_words)

