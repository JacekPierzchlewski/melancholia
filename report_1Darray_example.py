"""
Example of using 'melancholia.py' module.
Run it:
$ python report_1Darray_example.py.

The script will produce a file '1Darrays.txt'.


Copyright (C) <2015>  Jacek Pierzchlewski
                      jap [at] es dot aau dot dk
                      pierzchlewski dot jacek [at] gmail.com

*Authors*:
    Jacek Pierzchlewski, Aalborg University, Denmark. <jap@es.aau.dk>
                                                      jap [at] es.aau.dk
                                                      pierzchlewski dot jacek [at] gmail.com

*Version*:
    1.0-alpha  | 9-FEB-2015 : * Alpha version is ready. |br|

*License*:
    BSD 2-Clause
"""

import numpy as np
import melancholia

if __name__ == '__main__':

    hReport = open('1Darrays.txt', 'w')      # Open the file

    # %% 1 dimensional vector printing

    # Vector printing: The simplest usage
    vA = np.random.rand(100)
    strPrintedVect = melancholia.printA(vA)
    hReport.write(strPrintedVect)

    # Vector printing: integer elements
    vA = np.random.randint(-100, 100, 100)
    strPrintedVect = melancholia.printA(vA, strFormat = '%d')
    hReport.write(strPrintedVect)

    # Vector printing: horizontal vector printing
    vA = np.random.rand(100)
    strPrintedVect = melancholia.printA(vA, bVert1D=0)
    hReport.write(strPrintedVect)

    # Vector printing: horizontal vector printing with integer elements
    vA = np.random.randint(-100, 100, 1000)
    strPrintedVect = melancholia.printA(vA, bVert1D=0, strFormat = '%d')
    hReport.write(strPrintedVect)

    # Vector printing: horizontal vector printing with shorter lines
    vA = np.random.rand(100)
    strPrintedVect = melancholia.printA(vA, bVert1D=0, iMaxCols = 120)
    hReport.write(strPrintedVect)

    # Vector printing: horizontal vector printing with shorter lines and fancy delimiter
    vA = np.random.randint(-100, 100, 1000)
    strPrintedVect = melancholia.printA(vA, bVert1D=0, iMaxCols = 120, strDelimiter=' -|||- ')
    hReport.write(strPrintedVect)

    # Vector printing: horizontal vector printing with shorter lines fancy delimiter and header
    vA = np.random.rand(100)
    strPrintedVect = melancholia.printA(vA, bVert1D=0, iMaxCols = 120, strDelimiter=' -|||- ',
                                        strArrayName = 'vA', bPrintHeader=1)
    hReport.write(strPrintedVect)
