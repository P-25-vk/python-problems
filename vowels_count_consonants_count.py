string=input("Enter a String:")
vowels_count=0
consonant_count=0

for char in string:
    if(char=="A" or char=="E" or char=="I" or char=="O" or char=="U" or char=="a"
       or char=="e" or char=="i" or char=="o" or char=="u"):
        vowels_count+=1
    else:
        consonant_count+=1
print("Vowels_count:",vowels_count)
print("Consonants_count:",consonant_count)
