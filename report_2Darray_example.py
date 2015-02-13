"""
Examples of using 'melancholia.py' modules with 2D Numpy arrays

Run it:
$ python report_2Darray_example.py.

The script will produce a file '2Darrays.txt'.


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

*License*:
    BSD 2-Clause
"""

import numpy as np
import melancholia

if __name__ == '__main__':


    # %% 2 dimensional array printing directly to a file

    # Array printing: The simplest usage of printing to a file
    strInfo = "This array was printed directly to a file: \n\n"
    mA = np.random.rand(10, 10)
    melancholia.dumpA(mA, strFile='2Darrays.txt')

    # %% 2 dimensional array printing

    hReport = open('2Darrays.txt', 'a')      # Open a file with matrices

    # The simplest usage
    strInfo = "The simplest example of 2D array printing: \n\n"
    mA = np.random.rand(10, 10)
    strPrintedMat = strInfo + melancholia.printA(mA)
    hReport.write(strPrintedMat)

    # The simplest usage - vertical array Nx1
    strInfo = "The simplest example of 2D array printing (vertical array): \n\n"
    mA = np.random.rand(10, 1)
    strPrintedMat = strInfo + melancholia.printA(mA)
    hReport.write(strPrintedMat)

    # Custom delimiter
    strInfo = "2D array printing with a custom delimiter: \n\n"
    mA = np.random.rand(10, 10)
    strPrintedMat = strInfo + melancholia.printA(mA, strDelimiter='...')
    hReport.write(strPrintedMat)

    # No separation between the rows
    strInfo = "No separation between the rows: \n\n"
    mA = np.random.rand(10, 20)
    strPrintedMat = strInfo + melancholia.printA(mA, iRowSpaces=0)
    hReport.write(strPrintedMat)

    # Custom format
    strInfo = "2D array printing with integer format: \n\n"
    mA = np.random.randint(-100, 100, (40, 10))
    strPrintedMat = strInfo + melancholia.printA(mA, strFormat='%d')
    hReport.write(strPrintedMat)

    # Print array entries as integer with custom delimiter
    strInfo = "2D array printing with integer format and custom delimiter: \n\n"
    mA = np.random.randint(-100, 100, (40, 20))
    strPrintedMat = strInfo + melancholia.printA(mA, strFormat='%d', strDelimiter=' <---> ')
    hReport.write(strPrintedMat)

    # Add array name and header
    strInfo = "2D array printing with integer format, custom delimiter and array header: \n\n"
    mA = np.random.rand(10, 10)
    strPrintedMat = strInfo + melancholia.printA(mA, strFormat='%.2f', strDelimiter='...',
                                                 strArrayName='mA', bPrintHeader=1)
    hReport.write(strPrintedMat)

    # ----------------------------------------------------------------------------------
    # 2 dimensional array printing with wrapped lines

    # --------------------
    # Lines wrapped because of the max allowed number of characters in a line:

    # The maximum number of characters in a single line
    strInfo = "Wrap line printing after 59 characters: \n\n"
    mA = np.random.rand(10, 10)
    strPrintedMat = strInfo + melancholia.printA(mA, iMaxCols=59)
    hReport.write(strPrintedMat)

    # The maximum number of characters in a single line, custom delimiter
    strInfo = "Wrap line printing after 120 characters, custom delimiter: \n\n"
    mA = np.random.rand(10, 20)
    strPrintedMat = strInfo + melancholia.printA(mA, iMaxCols=109, strDelimiter=' <---> ')
    hReport.write(strPrintedMat)

    # The maximum number of characters in a single line, no spearation between the lines
    strInfo = "Wrap line printing after 120 characters, no separation between the lines: \n\n"
    mA = np.random.rand(10, 20)
    strPrintedMat = strInfo + melancholia.printA(mA, iMaxCols=109, iLineSpaces=0)
    hReport.write(strPrintedMat)

    # The maximum number of characters in a single line, no spearation between the lines, no separation between the rows
    strInfo = "Wrap line printing after 120 characters, no separation between the lines, no separation between the rows: \n\n"
    mA = np.random.rand(10, 20)
    strPrintedMat = strInfo + melancholia.printA(mA, iMaxCols=109, iLineSpaces=0, iRowSpaces=0)
    hReport.write(strPrintedMat)

    # --------------------
    # Lines wrapped because of the max allowed number of entries in a line:
    strInfo = "Wrap line printing after 9 characters: \n\n"
    mA = np.random.rand(10, 20)

    # Add some nan, inf and -inf entries
    mA[0, 0] = 1000.8
    mA[3, 1] = np.nan
    mA[9, 4] = np.nan
    mA[1, 1] = np.inf
    mA[6, 8] = np.inf
    mA[5, 9] = np.inf
    mA[5, 1] = -np.inf
    mA[3, 5] = -np.inf
    mA[4, 8] = -np.inf
    strPrintedMat = strInfo + melancholia.printA(mA, iMaxEntr=9)
    hReport.write(strPrintedMat)

