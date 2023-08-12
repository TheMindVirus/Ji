#for i in range(0x3000, 0x3FFF):
#    print(chr(i), end = "")
#print()

#for i in range(0x3000, 0x3200):
#    print(chr(i), end = "")
#print()

#for i in range(0x3000, 0x3200):
#    print(chr(i), end = "")
#print()

#for i in range(0x3020, 0x3080):
#    print(chr(i), end = "")
#print()

#for i in range(0x20, 0x80):
#    print(chr(i), end = "")
#print()

#for i in range(0x3000, 0x30FF):
#    print(chr(i), end = "")
#print()

#SO NI RO GU AA KA II DE

ji = "ソ" # 184, 189 XD

ji = \
"""
ソニログアカイデ
""".removeprefix("\n").removesuffix("\n")

print(ji)
print("{} string characters".format(len(ji)))

unicode = ji.encode("utf-8")

print(unicode)
print("{} unicode characters".format(len(unicode)))

bytecode = b""
for i in ji:
    bytecode += ord(i).to_bytes(2, "big")

print(bytecode)
print(" ".join(["{:02X}".format(i) for i in bytecode]))
print("{} bytecode characters".format(len(bytecode)))

for i in ji:
    print("{:02X} ".format(ord(i) - 0x3000), end = "")
print()

#B8 CB ED B0 A2 AB A4 C7

ij = []

for i in ji:
    ij.append(ord(i) - 0x3000) #PSP3000
    print(ij[-1], end = " ")
print()

print("{} bytes".format(len(ij)))

#189 203 237 176 162 171 164 199

jib = b""
bij = b""

for i in ij:
    jib += i.to_bytes(1, "little")
    bij += i.to_bytes(1, "big")
print(jib)
print(bij)

# ログ・ア||イ #

#print(jib.decode("utf-8"))
kana = []

for i in range(0x30A1, 0x3100):
    kana.append(chr(i))
print("".join(kana))

# AIUEO, AEIOU, UOAEI

kata = \
[
    "AA",  "AA",  "II",  "II",  "UU",  "UU",  "EE",  "EE",  "OO",  "OO",
    "KA",  "GA",  "KI",  "GI",  "KU",  "GU",  "KE",  "GE",  "KO",  "GO",
    "SA",  "ZA",  "SHI", "JI",  "SU",  "ZU",  "SE",  "ZE",  "SO",  "ZO",
    "TA",  "DA",  "CHI", "DJI", "TSU", "TSU", "DZU", "TE",  "DE",  "TO",  "DO",
    "NA",  "NI",  "NU",  "NE",  "NO",  "HA",  "BA",  "PA",  "HI",  "BI",  "PI",
    "FU",  "BU",  "PU",  "HE",  "BE",  "PE",  "HO",  "BO",  "PO",
    "MA",  "MI",  "MU",  "ME",  "MO",  "YA",  "YA",  "YU",  "YU",  "YO",  "YO",
    "RA",  "RI",  "RU",  "RE",  "RO",  "WA",  "WA",  "WI",  "WE",  "WO",  "NN",
    "VU",  "KA",  "KE",  "VA",  "VI",  "VE",  "VO",  "__",  "-_",  "<<",  ">>",
    "(\\",
]
print(kata)
print(str(len(kata)))
print(str(len(kana)))

#for i in range(0, len(kana)):
#    print(kata[kana[i]])

for i in ji:
    print(kata[kana.index(i)], end = " ")

"""
ソニログアカイデ
8 string characters
b'\xe3\x82\xbd\xe3\x83\x8b\xe3\x83\xad\xe3\x82\xb0\xe3\x82\xa2\xe3\x82\xab\xe3\x82\xa4\xe3\x83\x87'
24 unicode characters
b'0\xbd0\xcb0\xed0\xb00\xa20\xab0\xa40\xc7'
30 BD 30 CB 30 ED 30 B0 30 A2 30 AB 30 A4 30 C7
16 bytecode characters
BD CB ED B0 A2 AB A4 C7 
189 203 237 176 162 171 164 199 
8 bytes
b'\xbd\xcb\xed\xb0\xa2\xab\xa4\xc7'
b'\xbd\xcb\xed\xb0\xa2\xab\xa4\xc7'
ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿ
['AA', 'AA', 'II', 'II', 'UU', 'UU', 'EE', 'EE', 'OO', 'OO', 'KA', 'GA', 'KI', 'GI', 'KU', 'GU', 'KE', 'GE', 'KO', 'GO', 'SA', 'ZA', 'SHI', 'JI', 'SU', 'ZU', 'SE', 'ZE', 'SO', 'ZO', 'TA', 'DA', 'CHI', 'DJI', 'TSU', 'TSU', 'DZU', 'TE', 'DE', 'TO', 'DO', 'NA', 'NI', 'NU', 'NE', 'NO', 'HA', 'BA', 'PA', 'HI', 'BI', 'PI', 'FU', 'BU', 'PU', 'HE', 'BE', 'PE', 'HO', 'BO', 'PO', 'MA', 'MI', 'MU', 'ME', 'MO', 'YA', 'YA', 'YU', 'YU', 'YO', 'YO', 'RA', 'RI', 'RU', 'RE', 'RO', 'WA', 'WA', 'WI', 'WE', 'WO', 'NN', 'VU', 'KA', 'KE', 'VA', 'VI', 'VE', 'VO', '__', '-_', '<<', '>>', '(\\']
95
95
SO NI RO GU AA KA II DE 
>>>
"""

# クシン # ア||イ # [XV] #
