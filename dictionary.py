message = input(">")

word = message.split(' ')

emoji = {

    ":)" : "Smiling emoji", 
    ":(" : "Sad emoji"

}

output = ""
for wor in word:
    output += emoji.get(wor, wor) + ' '

print(output)