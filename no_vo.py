# Write a short Python function that counts the number of vowels in a given
# character string.
vowel=[]
con=[]
a = 'good morning every one '
for i in a:
    if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel.append(i)
    elif i==' ':
        pass
    else:
        con.append(i)
        
print(len(vowel))
print(len(con))