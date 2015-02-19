"""
Examples of using 'melancholia.py' module with 1D NumPy arrays..

Run it:
$ python example_1Darray.py.

The script will produce a file '1Darrays.txt'.


Copyright (C) <2015>  Jacek Pierzchlewski
                      jap [at] es dot aau dot dk
                      pierzchlewski dot jacek [at] gmail.com

*Authors*:
    Jacek Pierzchlewski, Aalborg University, Denmark. <jap@es.aau.dk>
                                                      jap [at] es.aau.dk
                                                      pierzchlewski dot jacek [at] gmail.com

*Version*:
    1.0-alpha  |  9-FEB-2015 : * Alpha version is ready. |br|
    1.0        | 13-FEB-2015 : * Version 1.0 is ready. |br|
    1.0-r1     | 18-FEB-2015 : * Comments cosmetics. |br|

*License*:
    BSD 2-Clause
"""

import numpy as np
import melancholia

if __name__ == '__main__':


    # %% 1 dimensional array printed to a file

    # Array printing: The simplest usage of printing to a file
    vA = np.random.rand(100)
    melancholia.dumpA(vA, strFile='1Darrays.txt')

    # %% 1 dimensional arrays printed to a variable (and then to a file)

    hReport = open('1Darrays.txt', 'a')      # Open the file

    # Array printing: The simplest usage of printing to a variable
    strInfo = "The simplest example of 1D array printing: \n\n"
    vA = np.random.rand(100)
    strPrintedVect = strInfo + melancholia.printA(vA)
    hReport.write(strPrintedVect)

    # Array printing: integer elements
    strInfo = "1D array printing with integer format: \n\n"
    vA = np.random.randint(-1000, 1000, 100)
    strPrintedVect =  strInfo + melancholia.printA(vA, strFormat='%d')
    hReport.write(strPrintedVect)

    # Array printing: horizontal array printing
    strInfo = "1D array horizontal printing: \n\n"
    vA = np.random.rand(100)
    strPrintedVect =  strInfo + melancholia.printA(vA, bVert1D=0)
    hReport.write(strPrintedVect)

    # Array printing: horizontal array printing with integer elements
    strInfo = "1D array horizontal printing with integer format: \n\n"
    vA = np.random.randint(-100, 100, 20)
    strPrintedVect =  strInfo + melancholia.printA(vA, bVert1D=0, strFormat='%d')
    hReport.write(strPrintedVect)

    # Array printing: horizontal array printing with integer elements and a header
    strInfo = "1D array horizontal printing with integer format and a header: \n\n"
    vA = np.random.randint(-100, 100, 20)
    strPrintedVect =  strInfo + melancholia.printA(vA, bVert1D=0, strFormat='%d',
                                                   strArrayName='vA', bPrintHeader=1)
    hReport.write(strPrintedVect)

    # ----------------------------------------------------------------------------------
    # 1 dimensional array printing with wrapped lines

    # --------------------
    # Lines wrapped because of the max allowed number of characters in a line:

    # Array printing: horizontal array printing with shorter lines
    strInfo = "1D array horizontal printing with shorter lines: \n\n"
    vA = np.random.rand(100)
    strPrintedVect =  strInfo + melancholia.printA(vA, bVert1D=0, iMaxCols=120)
    hReport.write(strPrintedVect)

    # Array printing: horizontal array printing with shorter lines and fancy delimiter
    strInfo = "1D array horizontal printing with shorter lines and custom delimiter: \n\n"
    vA = np.random.randint(-100, 100, 1000)
    strPrintedVect =  strInfo + melancholia.printA(vA, bVert1D=0, iMaxCols=120, strDelimiter='-|||-')
    hReport.write(strPrintedVect)

    # Array printing: horizontal array printing with shorter lines fancy delimiter and a header
    strInfo = "1D array horizontal printing with shorter lines, custom delimiter and a header: \n\n"
    vA = np.random.rand(100)
    strPrintedVect =  strInfo + melancholia.printA(vA, bVert1D=0, iMaxCols=120, strDelimiter='-|||-',
                                                   strArrayName='vA', bPrintHeader=1)
    hReport.write(strPrintedVect)

    # Array printing: horizontal array printing with shorter lines and no spaces between the lines
    strInfo = "1D array horizontal printing with shorter lines and no spaces between the lines: \n\n"
    vA = np.random.rand(100)
    strPrintedVect =  strInfo + melancholia.printA(vA, bVert1D=0, iMaxCols=120, iLineSpaces=0)
    hReport.write(strPrintedVect)

    # --------------------
    # Lines wrapped because of the max allowed number of entries in a line:
    strInfo = "1D array horizontal printing with shorter lines (7 elements in a line): \n\n"
    vA = np.random.rand(100)
    strPrintedVect =  strInfo + melancholia.printA(vA, bVert1D=0, iMaxEntr=7)
    hReport.write(strPrintedVect)
