ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ABCabc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

AA = []
Aa = []

for j in ABC:
    for i in ABC: 
        AA.append(j + i)

for j in ABCabc:
    for i in ABCabc:
        Aa.append(j + i)

print(AA)
print(len(AA))
print(hex(len(AA)))

print(Aa)
print(len(Aa))
print(hex(len(Aa)))

VOWEL = "UOAEI"
CONSO = "BCDFGHJKLMNPQRSTVWXYZ"
#CONSO = "BDFGHJKLMNPQRSTVWXYZ"

KU = []

for j in CONSO:
    for i in VOWEL:
        KU.append(j + i)

print(KU)
print(len(KU))
print(hex(len(KU)))

T = 0
for ku in KU:
    print(ku, end = "\n" if T % 5 == 4 else " ")
    T += 1

UK = []
CONSOLE = VOWEL + CONSO

for j in VOWEL:
    for i in CONSOLE:
        UK.append(i + j)

print(UK)
print(len(UK))
print(hex(len(UK)))

T = 0
for uk in UK:
    print(uk, end = "\n" if T % len(CONSOLE) == (len(CONSOLE) - 1) else " ")
    T += 1
print()
print()

############################################################################

VOWEL = "UOAEI"
CONSO = "BCDFGHJKLMNPQRSTVWXYZ"

LV1 = len(VOWEL)
LC1 = len(CONSO)
LV0 = LV1 - 1
LC0 = LC1 - 1

UU = []

for j in VOWEL:
    for i in VOWEL:
        UU.append(j + i)

VV = []

for j in VOWEL:
    for i in CONSO:
        VV.append(i + j)

WW = []

for j in VOWEL:
    for i in CONSO:
        WW.append(j + i)

XX = []

for j in CONSO:
    for i in CONSO:
        XX.append(j + i)

YY = \
[
    "BC", "BD", "BF", "BK", "BL",
    "BP", "BQ", "BT", "BW", "SH",
    "CB", "CD", "CG", "CH", "CK",
    "CL", "CM", "CP", "PC", "CR",
]

ZZ = \
[
    "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF",
    "FF", "FF", "FF", "FF", "FF",
]

T = 0
for uu in UU:
    print(uu, end = "\n" if T % LV1 == LV0 else " ")
    T += 1
print()

T = 0
for vv in VV:
    print(vv, end = "\n" if T % LC1 == LC0 else " ")
    T += 1
print()

T = 0
for ww in WW:
    print(ww, end = "\n" if T % LC1 == LC0 else " ")
    T += 1
print()
"""
T = 0
for xx in XX:
    print(xx, end = "\n" if T % LV1 == LV0 else " ")
    T += 1
print()
"""
print()

UVWZ = UU + VV + WW + ZZ # + XX
print(len(UVWZ))
print(hex(len(UVWZ)))

print(len(XX))
print(hex(len(XX)))

print(len(UVWZ + XX))
print(hex(len(UVWZ + XX)))

print(len(UVWZ + XX) - len(ZZ))
print(hex(len(UVWZ + XX) - len(ZZ)))
