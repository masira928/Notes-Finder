#===========================PROJECT - NOTES FINDER================================
#-LEVEL:1.SEARCH FOR THE FIRST OCCURENCE OF USER ENTERED WORD IN THE TEXT FILE
# and tell in which line its found:-
print("LEVEL-1")

import re,os

user=input("Search for the word in the verses:")

with open("Ar-Rahman.txt") as first:
   lines = first.readlines()
   found=False
   for i,line in enumerate(lines):
       verse=re.search("[0-9]{1,2}",line)
       useR=re.search(rf"{user}",line,re.IGNORECASE)
       if re.search(user,line,re.IGNORECASE):
           print("We found the word/verse you looked for:")
           print({useR.group():[{"Verse":verse.group()},{"File Name":first.name}]})
           found=True
           break
   if not found:
       print("Not Found")


#-LEVEL:2.SEARCH FOR ALL THE OCCURENCES OF USER ENTERED WORD IN MULTIPLE LINES
#OF THE TEXT FILE AND RETURN A LIST OF THOSE LINE NUMBERS:-
print("LEVEL-2")

user=input("Search for the word in the verses:")
with open("Ar-Rahman.txt") as first:
   lines = first.readlines()
   found=False
   print("We found the word/verse you searched:")
   for i,line in enumerate(lines):
       verse=re.search("[0-9]{1,2}",line)
       useR=re.search(rf"{user}",line,re.IGNORECASE)
       User=re.search(rf".*{user}.*",line,re.IGNORECASE)
       if re.search(user,line,re.IGNORECASE):
           print({useR.group():[{"Verse No.":verse.group()},{"File Name":first.name},{"Verse":User.group()}]})
           found=True
   if not found:
       print("Not Found")
            

#-LEVEL:3.SEARCH FOR THE FIRST OCCURENCE OF USER ENTERED WORD IN MULTIPLE FILES
#AND TELL THE NAME OF THE FILES:-
print("LEVEL-3")

user=input("Search for the word in the verses:")
directory=os.getcwd()
filenames=['Ar-Rahman.txt','Ad-Duha.txt','Al-Inshirah.txt']
for filename in filenames:
   filepath = os.path.join(directory, filename)
   with open(filepath, 'r') as file:
       content = file.readlines()
       for line in content:
           verse=re.search("[0-9]{1,2}",line)
           useR=re.search(rf"{user}",line,re.IGNORECASE)
           if re.search(user,str(line),re.IGNORECASE):
               print({useR.group():[{"Verse":verse.group()},{"File Name":filename}]})
               break
           else:
               None
                
   for i,line in enumerate(lines2):
       verse=re.search("[0-9]{1,2}",line)
       useR=re.search(rf"{user}",line,re.IGNORECASE)
       if re.search(user,str(line),re.IGNORECASE):
           print({useR.group():[{"Verse":verse.group()},{"File Name":second.name}]})
           found=True
           break
   for i,line in enumerate(lines3):
       verse=re.search("[0-9]{1,2}",line)
       useR=re.search(rf"{user}",line,re.IGNORECASE)
       if re.search(user,str(line),re.IGNORECASE):
           print({useR.group():[{"Verse":verse.group()},{"File Name":third.name}]})
           found=True
           break
   if not found:
       print("Not Found")


#-LEVEL:4.SEARCH FOR ALL THE OCCURENCES OF USER ENTERED WORD IN MULTIPLE FILES AND TELL THE NAME 
#OF THE FILES AND ALSO TELL IN WHICH LINES THAT WORD IS FOUND IF THE WORD IS
#REPEATED:-
print("LEVEL-4")

user=input("Search for the word in the verses:")
with open("Ar-Rahman.txt") as first:
    lines = first.readlines()
with open("Al-Inshirah.txt") as second:
    lines2 = second.readlines()
with open("Ad-Duha.txt")as third:
    lines3 = third.readlines()
    print("We found the word/verse you searched for:")
    found=False
    for line in lines:
        verse=re.search("[0-9]{1,2}",line)
        useR=re.search(rf"{user}",line,re.IGNORECASE)
        User=re.search(rf".*{user}.*",line,re.IGNORECASE)
        if re.findall(user,str(line),re.IGNORECASE):
            print({useR.group():[{"Verse":verse.group()},{"File Name":first.name},{"Verse":User.group()}]})
            found=True
    for line in lines2:
        verse=re.search("[0-9]{1,2}",line)
        useR=re.search(rf"{user}",line,re.IGNORECASE)
        User=re.search(rf".*{user}.*",line,re.IGNORECASE)
        if re.findall(user,str(line),re.IGNORECASE):
            print({useR.group():[{"Verse":verse.group()},{"File Name":second.name},{"Verse":User.group()}]})
            found=True
    for line in lines3:
        verse=re.search("[0-9]{1,2}",line)
        useR=re.search(rf"{user}",line,re.IGNORECASE)
        User=re.search(rf".*{user}.*",line,re.IGNORECASE)
        if re.findall(user,str(line),re.IGNORECASE):
            print({useR.group():[{"Verse":verse.group()},{"File Name":third.name},{"Verse":User.group()}]})
            found=True
    if not found:
        print("Not Found")
