import textwrap

# 曼切斯特码解码
def mqst_decode(input):
    if len(input) % 2 != 0:
        print("非法曼切斯特码，长度不是偶数")
        return None
    output = ""
    for i in textwrap.wrap(input, 2):
        if i[0] == "1" and i[1] == "0":
            output += "1"
        elif i[0] == "0" and i[1] == "1":
            output += "0"
        else:
            print("非曼切斯特码，解码错误")
            return None
    return output

# 差分曼切斯特码解码
def diffmqst_decode(input):
    if len(input) % 2 != 0:
        print("非法差分曼切斯特码，长度不是偶数")
        return None
    output = ""
    last_two_bits = "01"
    for two_bits in textwrap.wrap(input,2):
        if two_bits != "01" and two_bits != "10":
            print("非法差分曼切斯特码")
            break
        if two_bits == last_two_bits:
            output += "0"
        else:
            output += "1"
        last_two_bits = two_bits
    return output
