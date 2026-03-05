# How do you merge and re-compress a string where each character is followed by its frequency, 
# ensuring each character appears once, in alphabetical order, with summed frequencies?

def compression(s):

    freq = [0] * 26

    i = 0 

    while i < len(s):
        num = 0
        char = s[i]
        i += 1

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        
        index = ord(char) - ord('a')

        freq[index] = freq[index] + num
    
    result = ''
    for i in range(26):
        if freq[i] > 0:
            char =  chr(i + ord('a'))
            result += char + str(freq[i])
    
    return result

print(compression("a3c3b3a5"))


