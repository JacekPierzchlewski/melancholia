"""
This module prints NumPy arrays in a human readable way. |br|


*List of functions*:

        Functions which should be accessed by user:

            A - dumpA:  Function prints 1D of 2D numpy array to a text file

            B - printA:  Function prints 1D or 2D numpy array to a
                         string variable

        Internal functions:

            general usage:

                - _printHeader:      function prints a header before a NumPy
                                     array is printed

                - _decodeString:     function decodes the string with
                                     printing format

                - _decodeStringErr:  function prints error message, if
                                     the given format is incorrect


            1D array printing:

                - _1DarrayVert:      function prints 1D numpy array
                                     vertically

                - _1DarrayHori:      function prints 1D numpy array
                                     horizontally

                - _1DgetTechnical:   function computes technical parametrers
                                     of 1D array printing

                - _1DcreateEqSpaces:  function creates printing equalization
                                      spaces for 1D array printing

                - _1DgetLineParam:    function computes the line printing
                                      parameters for 1D array printing

                - _1DprintIndices:    function prints in one line indices of
                                      selected entries from a 1D array

                - _1DprintEntries:    function prints in one line selected
                                      entries from a 1D array

            2D array printing:

                - _2Darray:           function prints 2D numpy array

                - _2DgetTechnical:    function computes technical parameters
                                      of 2D-array printing

                - _2DcreateEqSpaces:  function creates printing equalization
                                      spaces for 2D array printing

                - _2DgetLineParam:    function computes the line printing
                                      parameters for 2D printing

                - _2DprintColumns:    function prints indices of columns
                                      for 2D array

                - _2DprintInxRow:     function prints one index of a row of
                                      a 2D array

                - _2DprintRow:        function prints selected entries from
                                      the current row for a 2D array

Copyright (C) <2014-2016>  Jacek Pierzchlewski
                           pierzchlewski dot jacek [at] gmail.com

*Authors*:
    Jacek Pierzchlewski, Aalborg University, Denmark.
            pierzchlewski dot jacek [at] gmail.com

*Version*:
    1.0-alpha  | 9-FEB-2015 :  * Alpha version is ready. |br|
    1.0-beta   | 10-FEB-2015 : * Beta version is ready. |br|
    1.0        | 11-FEB-2015 : * 1.0 version is ready. |br|
    1.0r1      | 05-SEP-2016 : * pep8 improvements in code |br|

*License*:
    BSD 2-Clause

*Platforms*:
    Linux
    OS X
"""
from __future__ import division
import numpy as np


# %%##########################################################################
def dumpA(arrA, strFile, strMode='w', strArrayName='', strFormat='%f',
          iRowBrake=20, strDelimiter='   ', iMaxCols=4096, iMaxEntr=np.inf,
          bVert1D=1, bPrintHeader=0, iLineSpaces=1, iRowSpaces=1):
    """
    Function prints 1D or 2D numpy array to a text file

    This is the function which prints a NumPy array to a text file.
    Take a look at files: 'report_1Darray_example'
    and 'report_2Darray_example'
    for examples of usage.

    Input:

    - 1 **arrA** (*NumPy array*)     Array to be printed

    - 2 **strFile** (*string*)       Name of the file to save the array

    - 3 **strMode** (*string*)       File opening mode
                                     [optional, default = 'w']

    - 4 **strArrayName** (*string*)  Name of the array [optional, default = '']

    - 5 **strFormat** (*string*)     Format of printing entires of the array
                                     [optional, default = '%f']
                                     Acceptable formats are %d, %f, %.1f, %.2f,
                                     %.3f, %.4f, ...

    - 6 **iRowBrake** (*int*)        The number of rows before the column
                                     indices are printed again
                                     [optional, default = 20]

    - 7 **strDelimiter** (*string*)  Delimiter printed between the entries
                                     of the array
                                     [optional, default = '  ' (double space)]

    - 8 **iMaxCols** (*int*)         The maximum number of text columns used
                                     to print a single row
                                     [optional, default = 4096]

    - 9 **iMaxEntr** (*int*)         The maximum number of entries printed in
                                     a single line
                                     [optional, default = np.inf <-- only
                                      iMaxCols decides about line wrapping]

    - 10 **bVert1D** (*int*)         Print a 1-dimensional numpy array
                                     vertically or horizontally?
                                     1 - vertically, 0 - horizontally
                                     [optional, default = 1]

    - 11 **bPrintHeader** (*int*)    Add header with array name, dimension
                                     and size?
                                     1 - yes add, 0 - do not add
                                     [optional, default = 0]

    - 12 **iLineSpaces** (*int*)     The number of spaces between printed
                                     lines
                                     [optional, default = 1]

    - 13 **iRowSpaces** (*int*)      The number of spaces between printed rows
                                     (only for 2D arrays)
                                     [optional, default = 1]

    Output:  none

    """

    hFile = open(strFile, strMode)
    strArray = printA(arrA, strArrayName, strFormat, iRowBrake, strDelimiter,
                      iMaxCols, iMaxEntr, bVert1D, bPrintHeader, iLineSpaces,
                      iRowSpaces)
    hFile.write(strArray)
    hFile.close()


# %%##########################################################################
def printA(arrA, strArrayName='', strFormat='%f', iRowBrake=20,
           strDelimiter='   ', iMaxCols=4096, iMaxEntr=np.inf, bVert1D=1,
           bPrintHeader=0, iLineSpaces=1, iRowSpaces=1):
    """
    Function prints 1D or 2D numpy array to a string variable


    This is the function which prints a NumPy array to a string variable.
    Take a look on files: 'report_1Darray_example'
    and 'report_2Darray_example'
    for examples of usage.


    Input:

    - 1 **arrA** (*NumPy array*)     Array to be printed

    - 2 **strArrayName** (*string*)  Name of the array
                                     [optional, default = '']

    - 3 **strFormat** (*string*)     Format of printing entires of the
                                     array
                                     [optional, default = '%f']
                                     Acceptable formats are %d, %f, %.1f, %.2f,
                                     %.3f, %.4f, ...

    - 4 **iRowBrake** (*int*)        The number of rows before the column
                                     indices are printed again
                                     [optional, default = 20]

    - 5 **strDelimiter** (*string*)  Delimiter printed between the entries
                                     of the array
                                     [optional, default = '  ' (double space)]

    - 6 **iMaxCols** (*int*)         The maximum number of text columns used
                                     to print a single row
                                     [optional, default = 4096]

    - 7 **iMaxEntr** (*int*)         The maximum number of entries printed in
                                     a single line
                                     [optional, default = np.inf <-- only
                                      iMaxCols decides about line wrapping]

    - 8 **bVert1D** (*int*)          Print a 1-dimensional numpy array
                                     vertically or horizontally?
                                     1 - vertically, 0 - horizontally
                                     [optional, default = 1]

    - 9 **bPrintHeader** (*int*)     Add header with array name, dimension
                                     and size?
                                     1 - yes add, 0 - do not add
                                     [optional, default = 0]

    - 10 **iLineSpaces** (*int*)     The number of spaces between printed
                                     lines
                                     [optional, default = 1]

    - 11 **iRowSpaces** (*int*)      The number of spaces between printed rows
                                     (only for 2D arrays)
                                     [optional, default = 1]
    Output:

    - 1 **strArray** (*string*)    String with entries of the numpy array
    """

    # Check if the input array has 1 or 2 dimensions
    if (arrA.ndim == 1):

        # For 1 dimensinal array, the array may be printed horizontally
        # or vertically
        if bVert1D == 1:
            strArray = _1DarrayVert(arrA, strArrayName, strFormat, iRowBrake,
                                    bPrintHeader)
        else:
            strArray = _1DarrayHori(arrA, strArrayName, strFormat, iRowBrake,
                                    strDelimiter, iMaxCols, iMaxEntr,
                                    bPrintHeader, iLineSpaces)

    elif (arrA.ndim == 2):
        strArray = _2Darray(arrA, strArrayName, strFormat, iRowBrake,
                            strDelimiter, iMaxCols, iMaxEntr, bPrintHeader,
                            iLineSpaces, iRowSpaces)

    # If the array has neither 1 nor 2 dimensions, it is an error
    else:
        strErr = 'NumPy array which is to be printed to a file must '
        strErr += 'be of 1- or 2-dimensions!'
        raise ValueError(strErr)

    return strArray


# %%##########################################################################
def _printHeader(arrA, strArrayName, bPrintHeader):
    """
    Function prints a header before a NumPy array is printed


    Input:

    - 1. **arrA** (*NumPy array*)    Array to be printed

    - 2 **strArrayName** (*string*)  Name of the array

    - 3 **bPrintHeader** (*int*)     Flag  which switched on header printing
                                     1 - switch on, 0 - switch off

    Output:

    - 1 **strArray** (*string*)    String with the header, of an empty string
                                   if the header is switched off

    """

    # If header printing is switched off, return an empty string
    if bPrintHeader == 0:
        return ''

    # Print name of the array, if requested
    if (strArrayName == ''):
        strArray = ''
    else:
        strArray = ' \'%s\'  ' % (strArrayName)

    # Print dimension, size and type of the array
    strType = arrA.dtype.name  # Get the name of the array
    if arrA.ndim == 2:
        (nRows, nCols) = arrA.shape  # Get shape of the array
        strArray += '2D-array (shape - %d rows x %d cols, type - %s):\n' \
            % (nRows, nCols, strType)
    else:
        iSize = arrA.size          # Get the size of the array
        strArray += '1D-array (size - %d, type - %s):\n'\
            % (iSize, strType)

    return strArray


# %%##########################################################################
def _decodeString(strFormat):
    """
    Function decodes the string with printing format


    Input:

    - 1 **strFormat** (*string*)     Format of printing entires of the array
                                     Acceptable formats are %d, %f, %.1f,
                                     %.2f, %.3f, %.4f, ...

    Output:

    - 1 **bIntegerOnly** (*number*)      If 1 - only integers are printed
                                         (no mantissa)

    - 2 **iNDigitsAfterDot** (*int*)     The number of digits printed after
                                         dot

    """

    if len(strFormat) == 0:    # String cannot be empty
        _decodeStringErr(strFormat)

    # Check if the first character is '%', otherwise - error
    if not (strFormat[0] == '%'):
        _decodeStringErr(strFormat)

    # -----------------------------------------------------------------------
    # Check if the second character is 'd', 'f' or '.':

    # -----------------------------------------------------------------------
    # It is 'd':
    if (strFormat[1] == 'd'):
        # It must be the last element in the format string
        if len(strFormat) > 2:
            _decodeStringErr(strFormat)
        bIntegerOnly = 1
        iNDigitsAfterDot = 0

    # -----------------------------------------------------------------------
    # It is 'f':
    elif (strFormat[1] == 'f'):  # It is 'f'
        # It must be the last element in the format string
        if len(strFormat) > 2:
            _decodeStringErr(strFormat)
        bIntegerOnly = 0
        iNDigitsAfterDot = 6

    # -----------------------------------------------------------------------
    # It is '.' (dot):
    elif (strFormat[1] == '.'):  # It is dot

        if len(strFormat) == 2:    # Dot can not be the last digit
            _decodeStringErr(strFormat)

        # There must be a number after the dot
        if not ('0' <= strFormat[2] <= '9'):
            _decodeStringErr(strFormat)

        # Now read all the numbers after dot
        iNDigitsAfterDot = 0   # Number after dot
        for inxChr in np.arange(2, len(strFormat) - 1):  # Loop over all
            cChr = strFormat[inxChr]
            if not ('0' <= cChr <= '9'):
                _decodeStringErr(strFormat)

            # Translate from character to the number
            iChrNum = ord(cChr) - 48

            # Update the number after dot
            iNDigitsAfterDot = iNDigitsAfterDot * 10 + iChrNum
            bIntegerOnly = 0

        # The last letter after the number must be 'f'
        if not ((strFormat[len(strFormat) - 1]) == 'f'):
            _decodeStringErr(strFormat)

    # -----------------------------------------------------------------------
    # The second character is neither 'd', 'f' nor '.', which is incorrect
    else:
        _decodeStringErr(strFormat)

    return (bIntegerOnly, iNDigitsAfterDot)


# Print error message, if the given format is incorrect
def _decodeStringErr(strFormat):
    """
    Input:

    - 1 **strFormat** (*string*)     Format of printing entires of the array

    Output: none

    """
    strErr = ('Wrong string with printing format!')
    strErr += ('String > %s < is an incorrect string!') % (strFormat)
    strErr += (' Correct strings are: %d, %f, %.1f, %.2f, %.3f, %.4f, ...')
    raise ValueError(strErr)


# %%##########################################################################
def _1DarrayVert(arrA, strArrayName, strFormat, iRowBrake, bPrintHeader):
    """
    Function prints 1D numpy array vertically


    Input:

    - 1 **arrA** (*NumPy array*)      Array to be printed

    - 2 **strArrayName** (*string*)   Name of the array

    - 3 **strFormat** (*string*)      Format of printing entires of
                                      the array [optional, default = '%f']
                                      Acceptable formats are %d, %f, %.1f,
                                      %.2f, %.3f, %.4f, ...

    - 4 **iRowBrake** (*int*)         The number of rows before the column
                                      indices are printed again

    - 5 **bPrintHeader** (*int*)      Add header with array name, dimension
                                      and size?
                                      1 - yes add, 0 - do not add
                                      [optional, default = 0]

    Output:

    - 1 **strArray** (*string*)   String with entries of the numpy array
                                  printed vertically

    """

    # Get technial parameters of 1D array printing
    (nEnt, nD, nMaxChrInd, nMaxChrEnt, nMinChrEnt) \
        = _1DgetTechnical(arrA, strFormat, '')
    # nEnt - the number of entries in the array
    # nD   - the number of characters in delimter
    # nMaxChrInd - the maximum number of characters in indices of the array
    # nMaxChrEnt - the maximum number of characters in entries of the array
    # nMinChrEnt - the minimum number of characters in entries of the array

    # Get the printing equalization spaces
    (lSpacesInd, _, _, _) = \
        _1DcreateEqSpaces(nMaxChrInd, nMaxChrEnt, nMinChrEnt)
    # lSpacesInd - a list with spaces which should be added
    # to indices of an entry

    # --------------------------------------------------------------------
    # Printing starts here:

    # Add a header, if requested
    strArray = \
        _printHeader(arrA, strArrayName, bPrintHeader)

    # Loop over all entries in the array
    nDig = 1   # The number of digits in the current index of an entry
    iThr = 10  # The next threshold which changes the number of digits

    # Create the command which prints a single entrys
    strPrintEntry = '\'%s\' %% (arrA[inxEntr])' % (strFormat)
    for inxEntr in np.arange(nEnt):

        # If the threshold is reached, move forward the number
        # of digits in index of an entry
        if inxEntr == iThr:
            nDig = nDig + 1
            iThr = iThr * 10  # Move the threshold forward

        # Print index of the current entry and its value:
        strArray = strArray + ('%d:%s  ') % (inxEntr, lSpacesInd[nDig - 1])
        strEntry = eval(strPrintEntry)                # Print the entry

        # If the number is nan, 0 or positive, add a blank space before
        # the number
        if (arrA[inxEntr] >= 0) or np.isnan(arrA[inxEntr]):
            strBlankMinus = ' '
        else:
            strBlankMinus = ''

        # Print the entry
        strArray = strArray + strBlankMinus + strEntry + '\n'

        # Add a row brake, if iRowBrake entries where printed without
        # printing a row brake
        if ((inxEntr + 1) % iRowBrake) == 0:
            strArray = strArray + '\n'

    strArray = strArray + '\n'
    return strArray


# %%##########################################################################
def _1DarrayHori(arrA, strArrayName, strFormat, iRowBrake, strDelimiter,
                 iMaxCols, iMaxEntr, bPrintHeader, iLineSpaces):
    """
    Function prints 1D numpy array horizontally


    Input:

    - 1 **arrA** (*NumPy array*)      Array to be printed

    - 2 **strArrayName** (*string*)   Name of the array

    - 3 **strFormat** (*string*)      Format of printing entires of the array
                                      Acceptable formats are %d, %f, %.1f,
                                      %.2f, %.3f, %.4f, ...

    - 4 **iRowBrake** (*int*)         The number of rows before the column
                                      indices are printed again

    - 5 **strDelimiter** (*string*)   Delimiter printed between the entries
                                      of the array

    - 6 **iMaxCols** (*int*)          The maximum number of text columns used
                                      to print a single row

    - 7 **iMaxEntr** (*int*)          The maximum number of entries printed in
                                      a single line

    - 8 **bPrintHeader** (*int*)      Add header with array name, dimension
                                      and size?
                                      1 - yes add, 0 - do not add
                                      [optional, default = 0]

    - 9 **iLineSpaces** (*int*)       The number of spaces between printed
                                      lines
                                      [optional, default = 1]

    Output:

    - 1 **strArray** (*string*)   String with entries of the numpy array
    """

    # Get technial parameters of 1D array printing
    (nEnt, nD, nMaxChrInd, nMaxChrEnt, nMinChrEnt) \
        = _1DgetTechnical(arrA, strFormat, strDelimiter)
    # nEnt - the number of entries in the array
    # nD   - the number of characters in delimter
    # nMaxChrInd - the maximum number of characters in indices of the array
    # nMaxChrEnt - the maximum number of characters in entries of the array
    # nMinChrEnt - the minimum number of characters in entries of the array

    # Get the printing equalization spaces
    (lSpacesInd, lSpacesEnt, strAddSpaceInd, strAddSpaceEnt) \
        = _1DcreateEqSpaces(nMaxChrInd, nMaxChrEnt, nMinChrEnt)
    # lSpacesInd - a list with spaces which should be added to indices of
    #              an entry
    #
    # lSpacesEnt - a list with spaces which should be added to entries
    #
    # strAddSpaceInd - string with an additional space added to indices
    #                  of entries
    #
    # strAddSpaceEnt - string with an additional space added to  entries

    # Get the line printing parameters: the number of lines and number of
    # entries in one line
    (nLines, nEntrypLine, nEntrypLastLine) \
        = _1DgetLineParam(iMaxCols, iMaxEntr, nEnt, nD, nMaxChrEnt,
                          strAddSpaceEnt)
    # nLines - the number of lines used to print all the entries from
    # the array

    # nEntrypLine - the number of entries in one line
    # nEntrypLastLine - the number of entries in the last line

    # --------------------------------------------------------------------
    # Printing starts here

    # Add a header, if requested
    strArray = _printHeader(arrA, strArrayName, bPrintHeader)

    # Loop over all lines to be printed
    iStartEntry = 0   # Starting index of the current entry
    for inxLine in np.arange(nLines):
        # If it is the last line, the number of entries is different
        if inxLine == (nLines - 1):
            nEntrypLine = nEntrypLastLine

        strArray += 4 * ' '   # Print the margin

        # Print indices of entries
        strArray += _1DprintIndices(arrA, iStartEntry, nEntrypLine,
                                    lSpacesInd, strAddSpaceInd, nD) + '\n'

        # Print the margin
        strArray += 4 * ' '
        strArray += _1DprintEntries(arrA, iStartEntry, nEntrypLine,
                                    strAddSpaceEnt, lSpacesEnt,
                                    strDelimiter, strFormat,
                                    nMaxChrEnt) + '\n'

        strArray += iLineSpaces * '\n'  # Add spaces between lines

        iStartEntry += nEntrypLine  # Move forward the start entry

    # Add new line at the end of the output string
    strArray += '\n\n'
    return strArray


# %%#########################################################################
def _1DgetTechnical(arrA, strFormat, strDelimiter):
    """
    Function computes technical parametrers of 1D array printing

    Input:

    - 1 **arrA** (*NumPy array*)      Array to be printed

    - 2 **strFormat** (*string*)      Format of printing entires of the array

    - 3 **strDelimiter** (*string*)   Delimiter printed between
                                      the entries of the array

    Output:

    - 1 **nEnt** (*int*)         The number of entries in the array

    - 2 **nD** (*int*)           The number of characters in the delimter

    - 3 **nMaxChrInd** (*int*)   The maximum number of characters in indices
                                 of the array

    - 4 **nMaxChrEnt** (*int*)   The maximum number of characters in entries
                                 of the array

    - 5 **nMinChrEnt** (*int*)   The minimum number of characters in entries
                                 of the array

    """
    # --------------------------------------------------------------------
    # Count how many +inf, -inf and nan are in the array.
    # Change inf, -inf and nan into 0
    arrA_nan = np.isnan(arrA)                  # Positions of nan values in A
    arrA[arrA_nan] = 0                         # Change nans into 0
    nNan = (arrA_nan[arrA_nan == True]).size   # The number of nan values in A

    arrA_pinf = np.isinf(arrA) * (arrA >= 0)     # Positions of +inf vals in A
    arrA[arrA_pinf] = 0                          # Change +infs into 0
    nPInf = (arrA_pinf[arrA_pinf == True]).size  # The number of +inf vals in A

    arrA_ninf = np.isinf(arrA) * (arrA < 0)      # Positions of -inf vals in A
    arrA[arrA_ninf] = 0                          # Change -infs into 0
    nNInf = (arrA_ninf[arrA_ninf == True]).size  # The number of -inf vals in A
    # --------------------------------------------------------------------

    # --------------------------------------------------------------------
    # Get the higest number of characters in...

    # Decode the string with printing format
    (bInt, nM) = _decodeString(strFormat)

    # Get the higest number of characters in integer part of entries
    # of the array
    iMaxAbsInt = np.floor(np.max(np.abs(arrA)))
    nX = np.ceil(np.log10(iMaxAbsInt + 1)).astype(int)   #
    if (nX == 0):                                        #
        nX = 1                                           #

    # Get the higest number of characters in entries of the array
    nMaxChrEnt = nX + nM
    if bInt == 0:                     # Add 1 because of . in float numbers
        nMaxChrEnt = nMaxChrEnt + 1   # ^
    if (arrA[arrA < 0].size) > 0:     # Add 1 because of '-' in negat. numbers
        nMaxChrEnt = nMaxChrEnt + 1   # ^

    # If there is nan in the array, the minumum value of
    # the max number of characters in entries is 3
    if (nNan > 0) and (nMaxChrEnt < 3):
        nMaxChrEnt = 3

    # If there is inf in the array, the minumum value of the max number
    # of characters in entries is 3
    if (nPInf > 0) and (nMaxChrEnt < 3):
        nMaxChrEnt = 3

    # If there is -inf in the array, the minumum value of the max number
    # of characters in entries is 4
    if (nNInf > 0) and (nMaxChrEnt < 4):
        nMaxChrEnt = 4

    # -------
    nEnt = arrA.size    # Get the number of entries in 1D array

    nC = np.ceil(np.log10(nEnt)).astype(int)       # ...size of the array
    if (nC == 0):
        nC = 1
    nMaxChrInd = nC + 1          # ... indices of the array (1 because of :)

    nD = len(strDelimiter)       # ...delimiter

    # --------------------------------------------------------------------
    # Get the lowest number of characters in...

    # ...integer part of entries of the array
    iMinAbsInt = np.floor(np.min(np.abs(arrA)))
    nXl = np.ceil(np.log10(iMinAbsInt + 1)).astype(int)
    if nXl == 0:
        nXl = 1

    nMinChrEnt = nXl + nM            # ... entries of the array
    if bInt == 0:                    # Add 1 due to . in float numbers
        nMinChrEnt = nMinChrEnt + 1  # ^
    if (arrA[arrA >= 0].size) == 0:  # Add 1 due to '-' in all neg. numbers
        nMinChrEnt = nMinChrEnt + 1  # ^

    # If there is nan in the array, the maximum value of
    # the min number of characters in entries is 3
    if (nNan > 0) and (nMinChrEnt > 3):
        nMinChrEnt = 3

    # If there is inf in the array, the maximum value of
    # the min number of characters in entries is 3
    if (nPInf > 0) and (nMinChrEnt > 3):
        nMinChrEnt = 3

    # If there is -inf in the array, the maximum value of
    # the min number of characters in entries is 4
    if (nNInf > 0) and (nMinChrEnt > 4):
        nMinChrEnt = 4

    # --------------------------------------------------------------------
    # Restore correct positions of +inf, -inf and nan in the array
    if nNan > 0:
        arrA[arrA_nan] = np.nan
    if nPInf > 0:
        arrA[arrA_pinf] = np.inf
    if nNInf > 0:
        arrA[arrA_ninf] = -np.inf
    # --------------------------------------------------------------------

    return (nEnt, nD, nMaxChrInd, nMaxChrEnt, nMinChrEnt)


# %%#########################################################################
def _1DcreateEqSpaces(nMaxChrInd, nMaxChrEnt, nMinChrEnt):
    """
    Function creates printing equalization spaces for 1D array printing

    Input:

    - 1 **nMaxChrInd** (*int*)   The maximum number of characters in indices
                                 of the array

    - 2 **nMaxChrEnt** (*int*)   The maximum number of characters in entries
                                 of the array

    - 3 **nMinChrEnt** (*int*)   The minimum number of characters in entries
                                 of the array

    Output:

    - 1 **lSpacesInd** (*list*)  A list with spaces which should be added
                                 to indices of an entry

    - 2 **lSpacesEnt** (*list*)  A list with spaces which should be added
                                 to entries

    - 3 **strAddSpaceInd** (*string*)  A string with an additional space
                                       added to indices of entries

    - 4 **strAddSpaceEnt** (*string*)  A string with an additional space
                                       added to entries

    """
    # Create additional spaces for indices of entries and the entries
    # These spaces are used to equalize indices of entries with the entries
    if (nMaxChrInd >= nMaxChrEnt):
        strAddSpaceEnt = (nMaxChrInd - nMaxChrEnt) * ' '
        strAddSpaceInd = ''
    else:
        strAddSpaceEnt = ''
        strAddSpaceInd = (nMaxChrEnt - nMaxChrInd) * ' '

    # --------------------------------------------------------------------
    # Create a list with spaces which should be added to indices of an entry
    # These spaces are used to equalize the number of characters in indices of
    # entries with the number of characters in the longest index of an entry

    # The longest space to be added to indices of entries
    nLongSpace = nMaxChrInd - 2

    # Start a list with blank spaces
    lSpacesInd = []

    # Create a list with blank space
    for iSpaceSize in np.arange(nLongSpace, -1, -1):
        lSpacesInd.append(iSpaceSize * ' ')

    # Create a list with spaces which should be added to entries
    # These spaces are used to equalize the number of characters in entries
    # with the number of characters in the longest entry

    # The longest space to be added to entries
    nLongSpace = nMaxChrEnt - nMinChrEnt

    # Start a list with blank spaces
    lSpacesEnt = []

    # Create a list with blank spaces
    for iSpaceSize in np.arange(nLongSpace + 1):
        lSpacesEnt.append(iSpaceSize * ' ')

    return (lSpacesInd, lSpacesEnt, strAddSpaceInd, strAddSpaceEnt)


# %%#########################################################################
def _1DgetLineParam(iMaxCols, iMaxEntr, nEnt, nD, nMaxChrEnt, strAddSpaceEnt):
    """
    Function computes the line printing parameters for 1D array printing

    Input:

    - 1 **iMaxCols** (*int*)        The maximum number of text columns used
                                    to print a single row

    - 2 **iMaxEntr** (*int*)        The maximum number of entries printed in
                                    a single line

    - 3 **nEnt** (*int*)            The number of entries in the array

    - 4 **nD** (*int*)              The number of characters in the delimter

    - 5 **nMaxChrEnt** (*int*)      The maximum number of characters in
                                    entries of the array

    - 6 **strAddSpaceEnt** (*int*)  A string with an additional space added
                                    to entries

    Output:

    - 1 **nLines** (*int*)           The number of lines used to print all
                                     the entries from the array

    - 2 **nEntrypLine** (*int*)      The number of entries in one line

    - 3 **nEntrypLastLine** (*int*)  The number of entries in the last line

    """

    # Calculate the maximum number of characters needed to print one entry

    # Entry additional space + entry + delimiter
    nChr1Entry = len(strAddSpaceEnt) + nMaxChrEnt + nD

    # Compute the number of entries in one line
    nEntrypLine = np.floor((iMaxCols - 4 - 1) / nChr1Entry).astype(int)
    if (nEntrypLine > iMaxEntr):
        nEntrypLine = iMaxEntr

    # Check if it is possible to print at least one entry?
    if (nEntrypLine == 0):
        strErr = 'The requested line is to short to print a single entry'
        raise ValueError(strErr)

    # Into how many lines do we have to break the printing?
    nLines = np.ceil(nEnt / nEntrypLine)

    # Compute the number of entries in the last line
    nEntrypLastLine = nEnt - nEntrypLine * (nLines - 1)

    return (nLines, nEntrypLine, nEntrypLastLine)


# %%#########################################################################
def _1DprintIndices(arrA, iStartEntry, nEntries, lSpacesInd,
                    strAddSpaceInd, nD):
    """
    Function prints in one line indices of selected entries from a 1D array

    Input:

    - 1 **arrA** (*NumPy array*)       Array to be printed

    - 2 **iStartEntry** (*int*)        Index of the first entry to be printed

    - 3 **nEntries** (*int*)           The number of entries to be printed

    - 4 **lSpacesInd** (*list*)        A list with spaces which should be
                                       added to indices of an entry

    - 5 **strAddSpaceEnt** (*string*)  Blank spaces before every entry to
                                       equalize length of printed entries
                                       with printed indices of column

    - 6 **nD** (*integer*)             The number of characters in delimiter

    Output:

    - 1 **strArray** (*string*)   String with indices of entries
    """

    # Get the lowest number of digits in indices of entries
    if (iStartEntry >= 2):
        nIndDigL = np.ceil(np.log10(iStartEntry)).astype(int)
    else:
        nIndDigL = 1

    strArray = ''
    nDigs = nIndDigL     # The current number of digits
    iThr = 10 ** nDigs   # Next threshold which changes the number of digits

    # Loop over all entries
    for inxEntry in np.arange(iStartEntry, iStartEntry + nEntries):
        if inxEntry == iThr:     # Threshold is reached
            nDigs = nDigs + 1    # The number of digits
            iThr = iThr * 10     # Threshold

        # Print the entry
        strArray += ('%s%s%d:%s') \
            % (strAddSpaceInd, lSpacesInd[nDigs - 1], inxEntry, nD * ' ')

    return strArray


# %%#########################################################################
def _1DprintEntries(arrA, iStartEntry, nEntries, strAddSpaceEnt, lSpaces,
                    strDelimiter, strFormat, nMaxChrEnt):
    """
    Function prints in one line selected entries from a 1D array

    Input:

    - 1 **arrA** (*NumPy array*)        Array to be printed

    - 2 **iStartEntry** (*int*)         Index of the first entry to be printed

    - 3 **nEntries** (*int*)            The number of entries to be printed

    - 4 **strAddSpaceEnt** (*string*)   Blank spaces before every entry to
                                        equalize length of printed entries
                                        with printed indices of column

    - 5 **lSpaces** (*list*)            List with blank spaces used to
                                        equalize length of printed entries

    - 6 **strDelimiter** (*string*)     Delimiter printed between the entries

    - 7 **strFormat** (*string*)        Format of printing entires of the array
                                        Acceptable formats are %d, %f, %.1f,
                                        %.2f, %.3f, %.4f, ...

    - 8 **nMaxChrEnt** (*integer*)      The maximum possible number of
                                        characters used to print one entry
                                         from the array

    Output:

    - 1. **strArray** (*string*)   String with selected entries of
                                   the numpy array
    """
    # Create a command which prints a single entry
    strPrintEntry = '\'%s\' %% (arrA[inxEntr])' % (strFormat)

    strArray = ''
    # Loop over all entries
    for inxEntr in np.arange(iStartEntry, iStartEntry + nEntries):
        strEntry = eval(strPrintEntry)    # Create the current entry

        # The number of characters in the current entryv
        nChrEntry = len(strEntry)

        # The lenght of a space which must be added
        nSpace = nMaxChrEnt - nChrEntry

        # Print the entry
        strArray += ('%s%s%s%s') \
            % (strAddSpaceEnt, lSpaces[nSpace], strEntry, strDelimiter)

    return strArray


# %%#########################################################################
def _2Darray(arrA, strArrayName, strFormat, iRowBrake, strDelimiter, iMaxCols,
             iMaxEntr, bPrintHeader, iLineSpaces, iRowSpaces):
    """
     Function prints 2D numpy array

    Input:

    - 1 **arrA** (*NumPy array*)      Array to be printed

    - 2 **strArrayName** (*string*)   Name of the array

    - 3 **strFormat** (*string*)      Format of printing entires of the array
                                      [optional, default = '%f']
                                      Acceptable formats are %d, %f, %.1f,
                                      %.2f, %.3f, %.4f, ...

    - 4 **iRowBrake** (*int*)         The number of rows before the column
                                      indices are printed again

    - 5 **strDelimiter** (*string*)   Delimiter printed between the entries
                                      of the array

    - 6 **iMaxCols** (*int*)          The maximum number of text columns used
                                      to print a single row

    - 8 **iMaxEntr** (*int*)          The maximum number of entries printed
                                      in a single line

    - 9 **bPrintHeader** (*int*)      Add header with array name, dimension
                                      and size?
                                      1 - yes add, 0 - do not add
                                      [optional, default = 0]

    - 10 **iLineSpaces** (*int*)      The number of spaces between printed
                                      lines
                                      [optional, default = 1]

    - 11 **iRowSpaces** (*int*)       The number of spaces between printed
                                      rows (only for 2D arrays)
                                      [optional, default = 1]

    Output:

    - 1 **strArray** (*string*)   String with entries of the numpy array
                                  printed vertically

    """

    # Get technical parameters of 2D array printing
    (nRows, nCols, nD, nMaxChrEnt, nMaxChrIndR, nMaxChrIndC, nMinChrEnt) \
        = _2DgetTechnical(arrA, strFormat, strDelimiter)
    # nRows - the number of rows in the array
    # nCols - the number of columns in the array
    # nD - the number of characters in the delimter
    # nMaxChrEnt  - the max number of characters in entries of the array
    # nMaxChrIndR - the max number of characters in indices of rows of
    #               the array
    # nMaxChrIndC - the max number of characters in indices of columns of
    #               the array
    # nMinChrEnt - the min number of characters in entries of the array

    # Get the printing equalization spaces
    (lSpacesIndC, lSpacesIndR, lSpacesEnt, strAddSpaceIndC, strAddSpaceEnt) = \
        _2DcreateEqSpaces(nMaxChrEnt, nMaxChrIndR, nMaxChrIndC, nMinChrEnt)

    # --------------------------------------------------------------------
    # Check if it is possible to print at least one entry?

    # Get the  the line printing parameters: the number of lines and number of
    #  entries in one line
    (nLines, nEntrypLine, nEntrypLastLine) = \
        _2DgetLineParam(iMaxCols, iMaxEntr, nCols, nD, nMaxChrEnt,
                        nMaxChrIndR, strAddSpaceEnt)
    # nLines - the number of lines used to print all the entries from the array
    # nEntrypLine - the number of entries in one line
    # nEntrypLastLine - the number of entries in the last line

    # -------------------------------------------------------------------
    # Printing starts here

    # If rows must be broke into many lines, indices of
    # columns must be printed after every row
    if (nLines > 1):
        iRowBrake = 1

    # Add a header, if requested
    strArray = _printHeader(arrA, strArrayName, bPrintHeader)

    # Loop over all rows of the array
    for inxRow in np.arange(nRows):

        # The current number of entries printed in a line
        nEntries = nEntrypLine

        # Loop over all lines printed for the current row
        for inxLine in np.arange(0, nLines):

            # Column index of the first entry to be printed in this line
            inxStartCol = (inxLine * nEntrypLine)

            # The number of entries in the last line is different
            if (inxLine == (nLines - 1)):
                nEntries = nEntrypLastLine

            # Print indices of columns, if needed
            if ((inxRow % iRowBrake) == 0):
                strArray += _2DprintColumns(inxStartCol, nEntries,
                                            strAddSpaceIndC, lSpacesIndC,
                                            nMaxChrIndR, nD)

            # Print index of the current line
            strArray = strArray + _2DprintInxRow(inxRow, lSpacesIndR)

            # Print entries from the current line
            strArray = strArray + _2DprintRow(arrA, inxRow, inxStartCol,
                                              nEntries, nMaxChrEnt, strFormat,
                                              strAddSpaceEnt, lSpacesEnt,
                                              strDelimiter)
            strArray = strArray + '\n'

            # Add spaces between lines (only if there are multiple
            # lines and it is not the last line)
            if (nLines > 1) and (inxLine < nLines - 1):
                strArray = strArray + iLineSpaces * '\n'

        strArray += iRowSpaces * '\n'   # Add new lines at the end of the row

        # Force a new line after the last row
        if (iRowSpaces == 0) and (inxRow == nRows - 1):
            strArray = strArray + '\n'

    strArray = strArray + '\n'   # Add a new line at the end of the array
    return strArray


# %%#########################################################################
def _2DgetTechnical(arrA, strFormat, strDelimiter):
    """
    Function computes technical parameters of 2D-array printing


    Input:

    - 1 **arrA** (*NumPy array*)      Array to be printed

    - 2 **strFormat** (*string*)      Format of printing entires of the array

    - 3 **strDelimiter** (*string*)   Delimiter printed between the entries
                                      of the array

    Output:

    - 1 **nRows** (*int*)         The number of rows in the array

    - 2 **nCols** (*int*)         The number of columns in the array

    - 3 **nD** (*int*)            The number of characters in the delimter

    - 4 **nMaxChrEnt** (*int*)    The maximum number of characters in entries
                                  of the array

    - 5 **nMaxChrIndR** (*int*)   The maximum number of characters in indices
                                  of rows of the array

    - 6 **nMaxChrIndC** (*int*)   The maximum number of characters in indices
                                  of columns of the array

    - 7 **nMinChrEnt** (*int*)    The minimum number of characters in entries
                                  of the array

    """

    # --------------------------------------------------------------------
    # Count how many +inf, -inf and nan are in the array.
    # Change inf, -inf and nan into 0
    arrA_nan = np.isnan(arrA)                # Positions of nan values in A
    arrA[arrA_nan] = 0                       # Change nans into 0
    nNan = \
        (arrA_nan[arrA_nan == True]).size    # The number of nan values in A

    arrA_pinf = np.isinf(arrA) * (arrA >= 0)  # Positions of +inf values in A
    arrA[arrA_pinf] = 0                       # Change +infs into 0
    nPInf = \
        (arrA_pinf[arrA_pinf == True]).size   # The number of +inf values in A

    arrA_ninf = np.isinf(arrA) * (arrA < 0)   # Positions of -inf values in A
    arrA[arrA_ninf] = 0                       # Change -infs into 0
    nNInf = \
        (arrA_ninf[arrA_ninf == True]).size   # The number of -inf values in A
    # --------------------------------------------------------------------

    # --------------------------------------------------------------------
    # Get the higest number of characters in...

    # Decode the string with printing format
    (bInt, nM) = _decodeString(strFormat)

    # ... integer part of elements of the array...
    iMaxAbsInt = np.floor(np.max(np.abs(arrA)))
    nX = np.ceil(np.log10(iMaxAbsInt + 1)).astype(int)
    if (nX == 0):
        nX = 1
    nMaxChrEnt = nX + nM                # ... entries of the array
    if bInt == 0:                       # Add 1 due of . in float numbers
        nMaxChrEnt = nMaxChrEnt + 1     # ^
    if (arrA[arrA < 0].size) > 0:       # Add 1 due to '-' in negative numbers
        nMaxChrEnt = nMaxChrEnt + 1     # ^

    # If there is nan in the array, the minumum value of
    # the max number of characters in entries is 3
    if (nNan > 0) and (nMaxChrEnt < 3):
        nMaxChrEnt = 3

    # If there is inf in the array, the minumum value of
    # the max number of characters in entries is 3
    if (nPInf > 0) and (nMaxChrEnt < 3):
        nMaxChrEnt = 3

    # If there is -inf in the array, the minumum value of
    # the max number of characters in entries is 4
    if (nNInf > 0) and (nMaxChrEnt < 4):
        nMaxChrEnt = 4

    # ----
    (nRows, nCols) = arrA.shape  # Get the dimensions of the array

    # ...the number of rows in the array
    nMaxChrIndR = np.ceil(np.log10(nRows)).astype(int)
    if (nMaxChrIndR == 0):
        nMaxChrIndR = 1
    nMaxChrIndR = nMaxChrIndR + 1                        # (1 because of :)

    # ...the number of columns in the array
    nMaxChrIndC = np.ceil(np.log10(nCols)).astype(int)
    if (nMaxChrIndC == 0):
        nMaxChrIndC = 1
    nMaxChrIndC = nMaxChrIndC + 1                        # (1 because of :)

    nD = len(strDelimiter)                             # ...delimiter

    # --------------------------------------------------------------------
    # Get the lowest number of characters in...

    # ...integer part of elements of the array
    iMinAbsInt = np.floor(np.min(np.abs(arrA)))
    nXl = np.ceil(np.log10(iMinAbsInt + 1)).astype(int)
    if nXl == 0:
        nXl = 1

    # ... entries of the array
    nMinChrEnt = nXl + nM

    # Add 1 due to . in float numbers
    if bInt == 0:
        nMinChrEnt = nMinChrEnt + 1

    # Add 1 due to '-' in all negative numbers
    if (arrA[arrA >= 0].size) == 0:
        nMinChrEnt = nMinChrEnt + 1

    # If there is nan in the array, the maximum value of the
    # min number of characters in entries is 3
    if (nNan > 0) and (nMinChrEnt > 3):
        nMinChrEnt = 3

    # If there is inf in the array, the maximum value of the
    # min number of characters in entries is 3
    if (nPInf > 0) and (nMinChrEnt > 3):
        nMinChrEnt = 3

    # If there is -inf in the array, the maximum value of the
    # min number of characters in entries is 4
    if (nNInf > 0) and (nMinChrEnt > 4):
        nMinChrEnt = 4

    # --------------------------------------------------------------------
    # Restore correct positions of +inf, -inf and nan in the array
    if nNan > 0:
        arrA[arrA_nan] = np.nan
    if nPInf > 0:
        arrA[arrA_pinf] = np.inf
    if nNInf > 0:
        arrA[arrA_ninf] = -np.inf
    # --------------------------------------------------------------------

    return (nRows, nCols, nD, nMaxChrEnt, nMaxChrIndR, nMaxChrIndC, nMinChrEnt)


# %%#########################################################################
def _2DcreateEqSpaces(nMaxChrEnt, nMaxChrIndR, nMaxChrIndC, nMinChrEnt):
    """
    Function creates printing equalization spaces for 2D array printing


    Input:

    - 1 **nMaxChrEnt** (*int*)    The maximum number of characters in entries
                                  of the array

    - 2 **nMaxChrIndR** (*int*)   The maximum number of characters in indices
                                  of rows of the array

    - 3 **nMaxChrIndC** (*int*)   The maximum number of characters in indices
                                  of columns of the array

    - 4 **nMinChrEnt** (*int*)    The minimum number of characters in entries
                                  of the array

    Output:

    - 1 **lSpacesIndC** (*list*)          A list with spaces which should be
                                          added to indices of columns

    - 2 **lSpacesIndR** (*list*)          A list with spaces which should be
                                          added to indices of rows

    - 3 **lSpacesEnt** (*list*)           A list with spaces which should be
                                          added to entries

    - 4 **strAddSpaceIndC** (*string*)    A string with an additional space
                                          added to indices of entries

    - 5 **strAddSpaceEnt** (*string*)     A string with an additional space
                                          added to entries

    """
    # Create additional spaces for indices of columns and the entries
    # These spaces are used to equalize indices of columns with the entries
    if (nMaxChrIndC >= nMaxChrEnt):
        strAddSpaceEnt = (nMaxChrIndC - nMaxChrEnt) * ' '
        strAddSpaceIndC = ''
    else:
        strAddSpaceEnt = ''
        strAddSpaceIndC = (nMaxChrEnt - nMaxChrIndC) * ' '

    # Create a list with spaces which should be added to indices of columns
    # These spaces are used to equalize the number of characters in indices of
    # columns with the number of characters in the longest index of a column

    # The longest space to be added to indices of columns
    nLongSpaceC = nMaxChrIndC - 1

    # Create a list with blank space
    lSpacesIndC = []       # Start a list with blank spaces
    for iSpaceSize in np.arange(nLongSpaceC, -1, -1):
        lSpacesIndC.append(iSpaceSize * ' ')

    # Create a list with spaces which should be added to indices of rows
    # These spaces are used to equalize the number of characters in indices of
    # rows with the number of characters in the longest index of a rows

    # The longest space to be added to indices of rows
    nLongSpaceR = nMaxChrIndR - 1

    # Create a list with blank space
    lSpacesIndR = []                          # Start a list with blank spaces
    for iSpaceSize in np.arange(nLongSpaceR, -1, -1):
        lSpacesIndR.append(iSpaceSize * ' ')

    # Create a list with spaces which should be added to entries
    # These spaces are used to equalize the number of characters in entries
    # with the number of characters in the longest entry

    # The longest space to be added to entries
    nLongSpace = nMaxChrEnt - nMinChrEnt

    # Create a list with blank spaces
    lSpacesEnt = []                          # Start a list with blank spaces
    for iSpaceSize in np.arange(nLongSpace + 1):
        lSpacesEnt.append(iSpaceSize * ' ')

    return (lSpacesIndC, lSpacesIndR, lSpacesEnt,
            strAddSpaceIndC, strAddSpaceEnt)


# %%#########################################################################
def _2DgetLineParam(iMaxCols, iMaxEntr, nCols, nD, nMaxChrEnt, nMaxChrIndR,
                    strAddSpaceEnt):
    """
    Function computes the line printing parameters for 2D printing


    Input:

    - 1 **iMaxCols** (*int*)           The maximum number of text columns used
                                       to print a single row

    - 2 **iMaxEntr** (*int*)           The maximum number of entries printed
                                       in a single line

    - 3 **nCols** (*int*)              The number of columns in the array

    - 4 **nD** (*int*)                 The number of characters in the delimter

    - 5 **nMaxChrEnt** (*int*)         The maximum number of characters
                                       in entries of the array

    - 6 **nMaxChrIndR** (*int*)        The maximum number of characters
                                       in indices of row

    - 7 **strAddSpaceEnt** (*string*)  A string with an additional space added
                                       to entries

    Output:

    - 1 **nLines** (*int*)           The number of lines used to print all
                                     the entries from the array

    - 2 **nEntrypLine** (*int*)      The number of entries in one line

    - 3 **nEntrypLastLine** (*int*)  The number of entries in the last line

    """

    # Calculate the maximum number of characters needed to print one entry

    # entry additional space + entry + delimiter
    nChr1Entry = len(strAddSpaceEnt) + nMaxChrEnt + nD

    # Compute the number of entries in one line
    nEntrypLine = np.floor((iMaxCols - 4 - 1 - nMaxChrIndR)
                           / nChr1Entry).astype(int)
    if (nEntrypLine > iMaxEntr):
        nEntrypLine = iMaxEntr
    if (nEntrypLine > nCols):
        nEntrypLine = nCols

    # Check if it is possible to print at least one entry?
    if (nEntrypLine == 0):
        strMsg = 'The requested line is to short to print a single entry'
        raise ValueError(strMsg)

    # Into how many lines do we have to break the printing?
    nLines = np.ceil(nCols / nEntrypLine)

    # Compute the number of entries in the last line
    nEntrypLastLine = nCols - nEntrypLine * (nLines - 1)

    return (nLines, nEntrypLine, nEntrypLastLine)


# %%##########################################################################
def _2DprintColumns(iStartCol, nEntries, strAddSpaceIndC, lSpacesIndC,
                    nMaxChrIndR, nD):
    """
    Function prints indices of columns for 2D array


    Input:

    - 1 **iStartCol** (*int*)            Index of the first columns to
                                         be printed

    - 2 **nEntries** (*int*)             The number of entries for which the
                                         indices of columns will be printed

    - 3 **strAddSpaceIndC** (*string*)   A string with an additional space
                                         added to indices of entries

    - 4 **lSpacesIndC** (*list*)         A list with spaces which should be
                                         added to indices of columns

    - 5 **nMaxChrIndR** (*int*)          A list with spaces which should be
                                         added to indices of rows

    - 6 **nD** (*int*)                   The number of characters in
                                         the delimter

    Output:

    - . **strArray** (*string*)   The string with printed requested indices
                                  of columns

    """

    # Print space which is over indices of rows + 2 characters margin
    strArray = (nMaxChrIndR * ' ') + (2 * ' ')

    # Get the lowest number of digits in indices of columns
    nIndDigL = np.ceil(np.log10(iStartCol + 1)).astype(int)
    if nIndDigL == 0:
        nIndDigL = 1

    nDigs = nIndDigL     # The current number of digits
    iThr = 10 ** nDigs   # Next threshold which changes the number of digits

    # Loop over all indices of columns
    for inxCol in np.arange(iStartCol, iStartCol + nEntries):
        if inxCol == iThr:       # Threshold is reached
            nDigs = nDigs + 1    # The number of digits
            iThr = iThr * 10     # Threshold

        # Print the current column
        strArray = strArray + ('%s%s%d:%s') \
            % (strAddSpaceIndC, lSpacesIndC[nDigs], inxCol, nD * ' ')
    strArray = strArray + '\n'
    return strArray


# %%#########################################################################
def _2DprintInxRow(inxRow, lSpacesIndR):
    """
    Function prints one index of a row of a 2D array


    Input:

    - 1 **inxCol** (*int*)            Index of the row to be printed

    - 2 **lSpacesIndR** (*list*)      A list with spaces which should be added
                                      to indices of rows

    Output:

    - 1 **strArray** (*string*)   The string with printed requested index of
                                  a row

    """

    # Print index of the row
    strRowInx = ('%d:') % inxRow

    # Pick up a correct space which is added before the index
    strSpaceBefore = lSpacesIndR[len(strRowInx) - 1]

    # Connect the above together
    strArray = strSpaceBefore + strRowInx
    strArray = strArray + '  '
    return strArray


# %%##########################################################################
def _2DprintRow(arrA, inxRow, iStartCol, nEntries, nMaxChrEnt, strFormat,
                strAddSpaceEnt, lSpacesEnt, strDelimiter):
    """
    Function prints selected entries from the current row for a 2D array


    Input:

    - 1 **arrA** (*NumPy array*)           Array to be printed

    - 2 **inxRow** (*int*)                 Index of the rows from which the
                                           entries are printed

    - 3 **iStartCol** (*int*)              Index of the first column from
                                           which the entries are printed

    - 4 **nEntries** (*int*)               The number of entries to be printed

    - 5 **nMaxChrEnt** (*int*)             The maximum number of characters in
                                           entries of the array

    - 6 **strFormat** (*string*)           Format of printing entries of
                                           the array

    - 7 **strAddSpaceEnt** (*string*)      A string with an additional space
                                           added to entries

    - 8 **lSpacesEnt** (*list*)            A list with spaces which should be
                                           added to entries

    - 9 **strDelimiter** (*string*)        Delimiter printed between the
                                           entries of the array

    Output:

    - 1 **strArray** (*string*)   The string with printed requested entries

    """

    # Create a command which prints a single entry
    strPrintEntry = '\'%s\' %% (arrA[inxRow, inxEntr])' % (strFormat)

    strArray = ''
    # Loop over all entries in a row
    for inxEntr in np.arange(iStartCol, iStartCol + nEntries):

        # Create the current entry
        strEntry = eval(strPrintEntry)

        # The number of characters in the current entry
        nChrEntry = len(strEntry)

        # The lenght of a space which must be added
        nSpace = nMaxChrEnt - nChrEntry

        # Print the entry
        strArray += ('%s%s%s%s') \
            % (strAddSpaceEnt, lSpacesEnt[nSpace], strEntry, strDelimiter)

    return strArray
