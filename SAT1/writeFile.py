import string


#write converted CNF to File
def writeCNF(lits,terms, cnfArray, writemode = "w+"):

    if writemode == "w+":
        f = open("satTest.cnf", writemode)
        f.write("p cnf " + str(lits) + " " + str(terms)+"\n")
    else:
        f = open("satTest.cnf", "r+")
        line = f.readline()
        txt = f.read()
        elem = line.split()
        terms += int(elem[3])
        line = line.replace(str(elem[3]), str(terms))
        result = line + txt
        #result = result + newFormular

        f.close()

        f = open("satTest.cnf", "w+")
        f.write(result)


    for i in range(0,len(cnfArray)):
        for j in range(0, len(cnfArray[i])):
            f.write(str(cnfArray[i][j])+" ")
        f.write("0\n")


