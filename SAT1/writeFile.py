#write converted CNF to File
def writeCNF(lits,terms, cnfArray):
    f = open("satTest.cnf","w+")
    f.write("p cnf " + str(lits) + " " + str(terms)+"\n")

    for i in range(0,len(cnfArray)):
        for j in range(0, len(cnfArray[i])):
            f.write(cnfArray[i][j]+" ")
        f.write("0\n")


