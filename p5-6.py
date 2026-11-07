import math
with open("moby dick.txt", encoding="utf-8") as f:
    data = f.read()
    data = data.upper()
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"," "]
def count_alphabet(data, alphabet):
    alphcount = {}
    for i in range(len(alphabet)):
        alphcount[alphabet[i]] = data.count(alphabet[i])
    return(alphcount)
lf = []
btrc = {}
bob = count_alphabet(data, alphabet)
#pi = input("enter i: ")
#pj = input("enter j: ")
def count_bigram(data, alphabet,pi,pj):
    for letter in alphabet:
        lf.append(data.count(letter))
    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
            bigram_count = data.count(alphabet[i] + alphabet[j])
            if bigram_count > 0:
                btrc[f"{alphabet[i]}{alphabet[j]}"] = bigram_count

    plf = pi+pj
    if plf in btrc:
        pboc = btrc[plf] 
        return(pboc,bob[pi])

    else: 
        return(0,bob[pi])

encoded_text = list("GPKZFER JRSER EKWIGIWKWVRZ YZRCWMWCRSEVRYWEWISCRGLIGFJWRGIFYISDD EYRCSEYLSYWRGPKZFEJRVWJ YERGZ CFJFGZPRWDGZSJ QWJRUFVWRIWSVST C KPRN KZR KJREFKSTCWRLJWRFXRJ YE X USEKR EVWEKSK FER KJRCSEYLSYWRUFEJKILUKJRSEVRFTAWUKRFI WEKWVRSGGIFSUZRS DRKFRZWCGRGIFYISDDWIJRNI KWRUCWSIRCFY USCRUFVWRXFIRJDSCCRSEVRCSIYWRJUSCWRGIFAWUKJ")
s_score = 0
for i in range(len(encoded_text)-1):
    pi = encoded_text[i]
    pj = encoded_text[i+1]
    big_counts = count_bigram(data, alphabet,pi,pj)
    bg_count = big_counts[0]
    ug_counts = big_counts[1]
    p_score = (bg_count + 1)/ ug_counts
    s_score += math.log(p_score)
print(s_score)