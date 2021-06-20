def isPalindromes(texts):
    characters = ''''"!?,.:;'''
    result = []
    for i in range(len(texts)):
        texts[i] = texts[i].lower().replace(' ','')
        for x in range(len(characters)):
            texts[i] = texts[i].replace(characters[x],'')
        if texts[i] == texts[i][::-1]:
            result.append(True)
        else: result.append(False)
    return result
texts = ["Madam, I'm Adam.","rotator","Hello","nurses run"]
print(isPalindromes(texts))
