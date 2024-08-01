def wordPattern(pattern, s):
    con = dict() #conversionDictionary
    t = s.split()
    for i in range(len(pattern)):
        if pattern[i] in con.keys():
            if con.get(pattern[i]) != t[i]:
                return False
        else:
            con.update({pattern[i]: t[i]})

    #print(con)
    return True

# Example 1:
# Input: 
pattern = "abba"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
# Output: true

# Example 2:
# Input: 
pattern = "abba"
s = "dog cat cat fish"
print(wordPattern(pattern, s))
# Output: false

# Example 3:
# Input: 
pattern = "aaaa"
s = "dog cat cat dog"
print(wordPattern(pattern, s))
# Output: false
