ABCabc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
AaBbCc = []

for j in ABCabc:
    for i in ABCabc:
        AaBbCc.append(j + i)

print()
print(AaBbCc)
print(len(AaBbCc))
print(hex(len(AaBbCc)))
print()

#######################################################################

VOWEL = "UOAEI"
CONSO = "BCDFGHJKLMNPQRSTVWXYZ"
vowel = "uoaei"
conso = "bcdfghjklmnpqrstvwxyz"

LV1 = len(VOWEL)
LC1 = len(CONSO)
LV0 = LV1 - 1
LC0 = LC1 - 1

AA = []
aa = []
Aa = []
aA = []

for j in range(0, LV1):
    for i in range(0, LV1):
        AA.append(VOWEL[j] + VOWEL[i])
        aa.append(vowel[j] + vowel[i])
        Aa.append(VOWEL[j] + vowel[i])
        aA.append(vowel[j] + VOWEL[i])

BB = []
bb = []
Bb = []
bB = []

for j in range(0, LV1):
    for i in range(0, LC1):
        BB.append(CONSO[i] + VOWEL[j])
        bb.append(conso[i] + vowel[j])
        Bb.append(CONSO[i] + vowel[j])
        bB.append(conso[i] + VOWEL[j])

CC = []
cc = []
Cc = []
cC = []

for j in range(0, LV1):
    for i in range(0, LC1):
        CC.append(VOWEL[j] + CONSO[i])
        cc.append(vowel[j] + conso[i])
        Cc.append(VOWEL[j] + conso[i])
        cC.append(vowel[j] + CONSO[i])

DD = []
dd = []
Dd = []
dD = []

for j in range(0, LC1):
    for i in range(0, LC1):
        DD.append(CONSO[j] + CONSO[i])
        dd.append(conso[j] + conso[i])
        Dd.append(CONSO[j] + conso[i])
        dD.append(conso[j] + CONSO[i])

for i in range(0, len(AA)):
    print(AA[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(aa)):
    print(aa[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(Aa)):
    print(Aa[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(aA)):
    print(aA[i], end = "\n" if i % LV1 == LV0 else " ")
print()

for i in range(0, len(BB)):
    print(BB[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(bb)):
    print(bb[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(Bb)):
    print(Bb[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(bB)):
    print(bB[i], end = "\n" if i % LV1 == LV0 else " ")
print()

for i in range(0, len(CC)):
    print(CC[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(cc)):
    print(cc[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(Cc)):
    print(Cc[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(cC)):
    print(cC[i], end = "\n" if i % LV1 == LV0 else " ")
print()

for i in range(0, len(DD)):
    print(DD[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(dd)):
    print(dd[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(Dd)):
    print(Dd[i], end = "\n" if i % LV1 == LV0 else " ")
print()
for i in range(0, len(dD)):
    print(dD[i], end = "\n" if i % LV1 == LV0 else " ")
print()

print()

ABCD = AA + aa + Aa + aA + BB + bb + Bb + bB + CC + cc + Cc + cC + DD + dd + Dd + dD
print(len(ABCD))
print(hex(len(ABCD)))
