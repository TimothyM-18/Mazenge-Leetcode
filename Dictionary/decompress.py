# How do you merge and re-compress a string where each character is followed by its frequency, 
# ensuring each character appears once, in alphabetical order, with summed frequencies?


def betterCompression(s):

    freq = {}
    i = 0
    print(i)
    while i < len(s): # Big O(N)
        num = 0
        char = s[i]
        print(char)
        i+=1

        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i+=1
        
        if char in freq:
            freq[char] = freq[char] + num
        else:
            freq[char] = num
    result = ''
    for key in sorted(freq.keys()): # Time complexity  k log k worst case N log N
        result += key + str(freq[key])
    print(freq)
    return result
        


print(betterCompression("a3c3b3"))


