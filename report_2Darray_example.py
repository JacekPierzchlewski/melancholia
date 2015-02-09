"""
Example of using 'melancholia.py' module.
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
    1.0-alpha  | 9-FEB-2015 : * Alpha version is ready. |br|

*License*:
    BSD 2-Clause
"""

import numpy as np
import melancholia

if __name__ == '__main__':

    hReport = open('2Darrays.txt', 'w')      # Open the file

    # %% 2 dimensional array printing

    # The simplest usage
    strInfo = "The simplest example of 2D array printing: \n\n"
    mA = np.random.rand(10, 10)
    strPrintedMat = strInfo + melancholia.printA(mA)
    hReport.write(strPrintedMat)

    # Custom delimiter
    strInfo = "2D array printing with a custom delimiter: \n\n"
    mA = np.random.rand(10, 10)
    strPrintedMat = strInfo + melancholia.printA(mA, strDelimiter='...')
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
                                                 strArrayName = 'mA', bPrintHeader=1)
    hReport.write(strPrintedMat)

    # ----------------------------------------------------------------------------------
    # 2 dimensional array printing with wrapped lines

    # The maximum number of characters in a single line
    strInfo = "Wrap line printing after 59 characters: \n\n" 
    mA = np.random.rand(10, 10)
    strPrintedMat = melancholia.printA(mA,  iMaxCols = 59)
    hReport.write(strPrintedMat)

    # The maximum number of characters in a single line, custom delimiter
    strInfo = "Wrap line printing after 120 characters, custom delimiter: \n\n" 
    mA = np.random.rand(10, 20)
    strPrintedMat = melancholia.printA(mA,  iMaxCols = 109, strDelimiter=' <---> ')
    hReport.write(strPrintedMat)
