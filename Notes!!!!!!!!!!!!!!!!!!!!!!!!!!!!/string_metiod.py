#jc 2nd string metiod notes

sentance = "The quick fox jumps over the lazy dog"

word = input("word:")
start = sentance.find(word)
lenght = len(word)
#print(sentance[start:start+lenght])
print(sentance.replace(word, "yellow"))
