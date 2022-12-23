import string
def convert(inp):
    ans = []
    if inp[0]=='S':
        split_list = inp.split(';')
        words = split_list[2]
        word = []
        word.extend(words)
        alpha = []
        for _ in word:
            if _.isupper():
                    alpha.append(" ")
                    alpha.append(_.lower())
            else:
                alpha.append(_)
        if split_list[1]=='M':
            print(alpha)
            alpha.pop()
            alpha.pop()
            alpha.pop()
            ans = "".join(alpha)
            print(ans)
        elif split_list[1]=='V'or split_list[1]=='C':
            ans.pop()
            ans = "".join(alpha)

    if inp[0]=='C': 
        sp_ls = inp.split(";")
        split_list = sp_ls[-1].split(" ")

        ans = []
        for words in split_list:
            word = []
            word.extend(words)
            word[0] = word[0].upper()
            word = ''.join(word)
            ans.append(word)
               
        if sp_ls[1]=='M':
            ans.append("()")
            ans = ''.join(ans)
        else:
            ans = ''.join(ans)
    ans = ans.strip()
    return ans

    
inp = input()
print(convert(inp))
