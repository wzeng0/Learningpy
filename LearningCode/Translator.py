# coder
# all letters shifted to the right
alphabet = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"
codebet = "z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y"
input = input("Please enter phrase: ")

# Codes the inputted phrase into the coded language
def coder(phrase):
    code = ""
    for letter in phrase:
        if letter in alphabet:
            index = alphabet.find(letter)
            code = code + codebet[index]
    return code

# test codes
# print(coder("hi"))
# print(coder("i"))

# print(alphabet.find("h")) finds index of string
# print(codebet[21]) finds character at the index given

print(coder(input))

def decode(phrase):
    decoded = ""
    for letter in phrase:
        if letter in codebet:
            index = codebet.find(letter)
            decoded = decoded + alphabet[index]
    return decoded

print(decode(coder(input)))