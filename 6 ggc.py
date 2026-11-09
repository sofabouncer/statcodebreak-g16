import math
import random


with open("moby dick.txt", encoding="utf-8") as f:
    data = f.read().upper()

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]


bob = {}
for letter in alphabet:
    bob[letter] = data.count(letter)

btrc = {}
for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        bigram = alphabet[i] + alphabet[j]
        count = data.count(bigram)
        if count > 0:
            btrc[bigram] = count

encoded_text = list("TULOMREMAEKBLRSWCTMWBIHB BTN KKUT NBTULOMRB DWBKSYMBYSWMRDBTULOMRKBJUNNBRMQMNBKE EUKEUT NBUDPSRY EUSDB ISCEBEOMBLN UDEMAEB DWBEOEBUDPSRY EUSDBT DBSPEMDBIMBCKMWBESBIRM XBEOMBTULOMRBPEMRBEOMBWUKTSQMRHBSPBPRMVCMDTHB D NHKUKBIHBEOMB R IBY EOMY EUTU DBDWBLSNHY EOB NBXUDWUB NKSBXDSJDB KB NXUDWCKBUDBEOMBDUDEOBTMDECRHBDMRNHB NNBKCTOBTULOMRKBTSCNWBIMBIRSXMDBIHB DBUDPSRYMWB EE TXMRBKCTOBTNKKUT NBTULOMRKBKEUNNBMDGSHBLSLCN RUEHBESW HBEOSCFOBYSKENHB KBLCZZNMKBNBXUDWUBJRSEMB BISSXBSDBTRHLESFR LOHBMDEUENMWBRUK N OBPUBUKEUXORGB NBYC YY BY DCKTRULEBPSRBEOMBWMTULOMRUDFBTRHLESFR LOUTBYMKKFMKBJOUTOBWMKTRUIMWBEOMBPURKEBXDSJDBCKMBSPBPRMVCMDTHB D NHKUKB DWBTRHLED NHKUKBEMTODUVCMKB DBUYLSRE DEBTSDERUICEUSDBSPBUIDB WN DBJ KBSDBKYLNMBKUZMBPSRBCKMBSPBPRMVCMDTHB D NHKUK")


def calculate_score(text_list, btrc, bob):
    s_score = 0
    for i in range(len(text_list)-1):
        pi = text_list[i]
        pj = text_list[i+1]
        plf = pi + pj
        
        bg_count = btrc.get(plf, 0) 
        ug_counts = bob.get(pi, 1)  
        
        p_score = (bg_count + 1) / ug_counts
        s_score += math.log(p_score)
    return s_score

def apply_cipher(text, cipher_dict):
    return [cipher_dict.get(c, c) for c in text]


def get_frequencies(text_data, alpha):
    counts = {char: text_data.count(char) for char in alpha}
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)

in_order_book = get_frequencies(data, alphabet)
in_order_encrypted = get_frequencies(encoded_text, alphabet)


current_cipher = {}
for i in range(len(alphabet)):
    current_cipher[in_order_encrypted[i][0]] = in_order_book[i][0]


current_m = apply_cipher(encoded_text, current_cipher)
current_score = calculate_score(current_m, btrc, bob)

T = 1.0 
num_steps = 100000
for step in range(num_steps):
 
    char1, char2 = random.sample(alphabet, 2)
    
    new_cipher = current_cipher.copy()
    new_cipher[char1], new_cipher[char2] = new_cipher[char2], new_cipher[char1]
    

    new_m = apply_cipher(encoded_text, new_cipher)
    new_score = calculate_score(new_m, btrc, bob)
    

    if new_score > current_score:

        current_cipher = new_cipher
        current_score = new_score
        current_m = new_m
    else:
    
        probability = math.exp((new_score - current_score) / T)
        if random.random() < probability:
            current_cipher = new_cipher
            current_score = new_score
            current_m = new_m
    if step % 10000 == 0:
        preview = "".join(current_m)
        print(f"Step {step:6d} | Score: {current_score:.2f} | Guess: {preview}...")

print("\nFinal Decrypted Text:")
print("".join(current_m))