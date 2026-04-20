words = list(input("Enter a list of words (separated by spaces): ").split())
result =[]
for i in range (0,len(words)):
    for j in range (0,len(words)):
        if i!=j and words[i] in words[j]:
            result.append(words[i])
            break
print("The words that are substring of another word in the list are:",result)        