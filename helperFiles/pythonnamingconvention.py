# This file takes a list of all known elements and preps them for
# use in the Amazon Echo Periodic Element Skill

# Created by Alexander Davis

originfile = open("elementnamelist.txt", "r")
newfile = open("finalformattedlist.txt", "w")
atomicnum = 1
newfile.write("module.exports = {\n")
for line in originfile:
    line.split()
    newfile.write('\t"'+line[:-1]+'": '+'"'+str(atomicnum)+'",\n')
    newfile.write('\t"'+str(atomicnum)+'": '+'"'+line[:-1]+'",\n')
    atomicnum += 1
newfile.write("};")

    # line.split()
    # newfile.write("DICTIONARY.push({\n")
    # newfile.write("\tkey: '" + str(atomicnum) + "',\n")
    # newfile.write("\tvalue: '" + line[:-1] + "'\n")
    # newfile.write("});\n")
    # atomicnum += 1
