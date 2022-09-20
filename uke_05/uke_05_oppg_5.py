def complement(seq):
    complementSeq = ""
    dict = {"A":"T", "T":"A", "G":"C", "C":"G"}
    for chr in seq:
        complementSeq += dict[chr]
    return complementSeq[::-1]

print("Tester complement... ", end="")
assert("ACTGCTAT" == complement("ATAGCAGT"))
assert("TAGTATCTAGT" == complement("ACTAGATACTA"))
assert("ACACAGCTGCAT" == complement("ATGCAGCTGTGT"))
print("OK")