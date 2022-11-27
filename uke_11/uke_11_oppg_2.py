def add_markers(path):
    marked_text = ""
    with open(path, "r", encoding = "utf-8") as file:
        for line in file.read().splitlines():
            marked_text += (f">>>{line}<<<\n")
    return marked_text

print("Tester add_markers... ", end="")
assert("""\
>>>Det var en gang en konge, og den kongen hadde hørt snakk om et skip \
som gikk like fort til lands som til vanns.<<<
>>>Så ville han også ha slikt et, og til den som kunne bygge det, lovte \
han ut kongsdattera og halve kongeriket, og det lyste han ut på kirkebakken \
ved alle kirkesogn over hele landet.<<<
>>>Det var mange som prøvde, kan du skjønne, for halve riket kunne være \
godt å ha, mente de vel, og kongsdattera kunne være bra å få i tillegg. Men \
ille gikk det med de fleste.<<<
""" == add_markers("askeladden.txt"))
print("ok")

