'''
Created on 23/01/2018

@author: Peter
'''
import re
import sys
from math import atan2, sin, cos, pi
ficheiroApoios = open("Apoios.txt", 'r')
ficheiroOut = open("MicroScript.txt", "w+")
listaApoios = []
listaLinhas = []
corLinha = 0
larguraLinha = 20

for linha in ficheiroApoios:
    try:
        pto = re.findall("[-+]?\d*\.\d+|\d+", linha)
        listaApoios.append([float(pto[0]), float(pto[1]), float(pto[2])])
    except:
        e = sys.exc_info()[0]
        print("<p>Error: %s</p>" % e)


def writeToFile(ficheiroOut, ptoTmpAnt, ptoTmpPost, rumo):
    ficheiroOut.write("%s\n" % ("co=" + str(corLinha)))
    ficheiroOut.write("%s\n" % "place line")
    x1 = larguraLinha / 2 * sin(rumo + pi / 2) + ptoTmpPost[0]
    y1 = larguraLinha / 2 * cos(rumo + pi / 2) + ptoTmpPost[1]
    z = ptoTmpPost[2]
    x2 = larguraLinha / 2 * sin(rumo - pi / 2) + ptoTmpPost[0]
    y2 = larguraLinha / 2 * cos(rumo - pi / 2) + ptoTmpPost[1]
    ficheiroOut.write("%s\n" %
                      ("xy=" + str(round(x1, 2)) + "," + str(round(y1, 2)) + "," + str(round(z, 2))))
    ficheiroOut.write("%s\n" %
                      ("xy=" + str(round(x2, 2)) + "," + str(round(y2, 2)) + "," + str(round(z, 2))))
    ficheiroOut.write("%s\n" % "reset")


for i in range(1, len(listaApoios) - 1):
    if i == 1:
        ptoTmpPost = listaApoios[i - 1]
        ptoTmpAnt = listaApoios[i]
        rumo = atan2((ptoTmpPost[0] - ptoTmpAnt[0]),
                     (ptoTmpPost[1] - ptoTmpAnt[1]))
        writeToFile(ficheiroOut, ptoTmpAnt, ptoTmpPost, rumo)
    ptoTmpAnt = listaApoios[i - 1]
    ptoTmpPost = listaApoios[i]
    rumo = atan2((ptoTmpPost[0] - ptoTmpAnt[0]),
                 (ptoTmpPost[1] - ptoTmpAnt[1]))
    writeToFile(ficheiroOut, ptoTmpAnt, ptoTmpPost, rumo)

ficheiroApoios.close()
ficheiroOut.close()
