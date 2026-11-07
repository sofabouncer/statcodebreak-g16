import math

with open("moby dick.txt", encoding="utf-8") as f:
    data = f.read().upper()

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

# 1. Count unigrams ONCE
bob = {}
for letter in alphabet:
    bob[letter] = data.count(letter)

# 2. Count bigrams ONCE
btrc = {}
for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        bigram = alphabet[i] + alphabet[j]
        count = data.count(bigram)
        if count > 0:
            btrc[bigram] = count

encoded_text = list("GPKZFER JRSER EKWIGIWKWVRZ YZRCWMWCRSEVRYWEWISCRGLIGFJWRGIFYISDD EYRCSEYLSYWRGPKZFEJRVWJ YERGZ CFJFGZPRWDGZSJ QWJRUFVWRIWSVST C KPRN KZR KJREFKSTCWRLJWRFXRJ YE X USEKR EVWEKSK FER KJRCSEYLSYWRUFEJKILUKJRSEVRFTAWUKRFI WEKWVRSGGIFSUZRS DRKFRZWCGRGIFYISDDWIJRNI KWRUCWSIRCFY USCRUFVWRXFIRJDSCCRSEVRCSIYWRJUSCWRGIFAWUKJ")

# 3. Calculate the score using the pre-built dictionaries
s_score = 0
for i in range(len(encoded_text)-1):
    pi = encoded_text[i]
    pj = encoded_text[i+1]
    plf = pi + pj
    
    # Look up the bigram count (defaults to 0 if not found in btrc)
    if plf in btrc:
        bg_count = btrc[plf]
    else:
        bg_count = 0
        
    ug_counts = bob[pi]
    
    # Apply the formula from your assignment
    p_score = (bg_count + 1) / ug_counts
    s_score += math.log(p_score)

print(s_score)