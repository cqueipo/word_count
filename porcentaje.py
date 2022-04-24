"""
Se lee un archivo por lineas. Para cada una se extrae de forma aleatoria un número. 
Si este es menor que el ratio, en otro fichero se escribe esa linea. 
"""

import random
import sys
def main(infilename, outfilename, ratio):
    with open(infilename) as infile:
        with open(outfilename, 'w') as outfile:
            for line in infile:
                if random.random()<=ratio:
                    outfile.write(line)


if __name__=="__main__":
    if len(sys.argv)<4:
        print(f"Usage: {sys.arv[0]} <infilename> <outfilename> <ratio")
        exit(1)
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    ratio = float(sys.argv[3])
    main(infilename, outfilename, ratio)