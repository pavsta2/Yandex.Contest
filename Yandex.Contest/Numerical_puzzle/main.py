import string, math

table = list(zip(range(26), string.ascii_lowercase))
table_dict = {x: y for x, y in table}
table_dict[26] = ' '

with open('input.txt', 'r') as f:
    letters = f.readline().rstrip('\n')
    enc = f.readline()

enc_list = [int(i) for i in enc.split(' ')]
final_word = ""
for i in range(len(enc_list)):
        if i == 0:
            final_word += table_dict[int(math.log2(enc_list[i]))]
        else:
            if enc_list[i]>enc_list[i-1]:
                final_word += table_dict[int(math.log2(enc_list[i]-enc_list[i-1]))]
            else:
                final_word += table_dict[int(math.log2(enc_list[i - 1] - enc_list[i]))]

with open('output.txt', 'w') as f:
    f.write(final_word)
