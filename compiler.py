filein = ("program.txt", 'r')
fileout = ("program.asm", 'w')
freereg = 1
zz = 0

functions = map["puts", "and", "modulo"]
varlut = {}

for line in filein:
    string = line.split(' ')
        if string[0].isalpha == True:
            if len(string[0]) = 1:
                if string[1] == "=":
                    if string[2].isdigit == True:
                        if string[2] >= 64:
                            fileout.write("imme|{bin(string[2]/2)}")
                            fileout.write("mov|lreg0|sreg1")
                            fileout.write("mov|lreg1|sreg2")
                            fileout.write("add")
                            fileout.write("mov|lreg3|sout")
                        else:
                            fileout.write("imme|{bin(string[2])}")
                            fileout.write("mov|lreg0|sreg{freereg}")
                            freereg += 1
            else:
                if string[0] == "print":
                    if string[1] == '"':
                        text = str(string[2])
                        if string[3] == '"':
                            for letter in text:
                                fileout.write("Imme|{bin(letter.encode(cp850))}")
                                fileout.write("mov|lreg0|sout")
                        else:
                            print("missing end qoute on line {zz}."
                    else:
                        print("missing beginning qoute in line {zz}.")
                or if string[0].isdigit == True and string[0] not in functions:
                    if string[1] == "=":
                        if string[2].isdigit == True:
                            varlut.append(str(string[0]). string[2])
                        else:
                            if string[2] in varlut:
                                varlut.append(str(string[0]), string[2])
