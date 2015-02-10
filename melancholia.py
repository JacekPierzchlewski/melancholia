"""
This module prints Numpy arrays in a human readable way. |br|


*List of functions*:
    

Copyright (C) <2014-2015>  Jacek Pierzchlewski
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

*Platforms*:
    Linux
    OS X
"""
from __future__ import division
import numpy as np


# %%#############################################################################
# Function prints 1D or 2D numpy array to a string variable
#################################################################################
def printA(arrA, strArrayName='', strFormat='%f', iRowBrake=20, strDelimiter='   ', iMaxCols=4096, bVert1D=1, bPrintHeader=0):
    """
    This is the function which prints a Numpy array to a string variable.
    Take a look on files: 'report_1Darray_example' and 'report_2Darray_example' for
    examples of usage.         
         
    Inputs:
    
    - 1. **arrA** (*Numpy array*)    Array to be printed
            
    - 2 **strArrayName** (*string*)  Name of the array [optional, default = '']
    
    - 3 **strFormat** (*string*)     Format of printing entires of the array [optional, default = '%f']
                                     Acceptable formats are %d, %f, %.1f, %.2f, %.3f, %.4f, ...

    - 4 **iRowBrake** (*int*)        The number of rows before the column indices are printed again 
                                     [optional, default = 20]         
    
    - 5 **strDelimiter** (*string*)  Delimiter printed between the entries of the array  
                                     [optional, default = '  ' (double space)]
                                     
    - 6 **iMaxCols** (*int*)         The maximum number of text columns used ot print a single row 
                                     [optional, default = 4096]

    - 7 **bVert1D** (*int*)          Print a 1-dimensional numpy array vertically or horizontally?
                                     1 - vertically, 0 - horizontally [optional, default = 1]

    - 8 **bPrintHeader** (*int*)     Add header with array name, dimension and size?
                                     1 - yes add, 0 - do not add [optional, default = 0]
    Output:
    
    - 1. **strMessage** (*string*)   String with entries of the numpy array
    """

    # Check if the input array has 1 or 2 dimensions 
    if (arrA.ndim == 1):
        
        # For 1 dimensinal array, the array may be printed horizontally or vertically
        if bVert1D == 1:
            strMessage = _1DarrayVert(arrA, strArrayName, strFormat, iRowBrake, bPrintHeader)
        else:
            strMessage = _1DarrayHori(arrA, strArrayName, strFormat, iRowBrake, strDelimiter, iMaxCols, bPrintHeader)

    elif (arrA.ndim == 2):
        strMessage = _2Darray(arrA, strArrayName, strFormat, iRowBrake, strDelimiter, iMaxCols, bPrintHeader)
    # If the array has neither 1 nor 2 dimensions, it is an error    
    else:
        raise ValueError('Numpy array which is to be printed to a file must be of 1- or 2-dimensions!')
    
    return strMessage


# %%#############################################################################
# Function prints a header before a Numpy array is printed 
#################################################################################
def _printHeader(arrA, strArrayName, bPrintHeader):
    """
    Inputs:
    
    - 1. **arrA** (*Numpy array*)    Array to be printed
            
    - 2 **strArrayName** (*string*)  Name of the array
    
    - 3 **bPrintHeader** (*int*)     Flag  which switched on header printing
                                     1 - switch on, 0 - switch off 
    Output:
 
    - 1. **strMessage** (*string*)   String with the header, of an empty string if the header is switched off 
    
    """
    
    # If header printing is switched off, return an empty string
    if bPrintHeader == 0:
        return ''

    # Print name of the array, if requested
    if (strArrayName == ''):
        strMessage = ''
    else:
        strMessage = ' \'%s\'  ' % (strArrayName)

    # Print dimension, size and type of the array
    strType = arrA.dtype.name  # Get the name of the array
    if arrA.ndim == 2:
        (nRows, nCols) = arrA.shape  # Get shape of the matrix
        strMessage = strMessage + '2D-array (shape - %d rows x %d cols, type - %s):\n' % (nRows, nCols, strType)
    else:
        iSize = arrA.size          # Get the size of the array
        strMessage = strMessage + '1D-array (size - %d, type - %s):\n' % (iSize, strType)

    return strMessage


# %%#############################################################################
# Function decodes the string with printing format
#################################################################################
def _decodeString(strFormat):
    """
    Inputs:
                    
    - 1 **strFormat** (*string*)     Format of printing entires of the array
                                     Acceptable formats are %d, %f, %.1f, %.2f, %.3f, %.4f, ...

    Output:
 
    - 1. **bIntegerOnly** (*number*)      If 1 - only integers are printed (no mantissa) 
 
    - 2. **iNDigitsAfterDot** (*int*)     The number of digits printed after dot  
    
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
        if len(strFormat) > 2:  # It must be the last element in the format string
            _decodeStringErr(strFormat)   
        bIntegerOnly = 1
        iNDigitsAfterDot = 0

    # -----------------------------------------------------------------------
    # It is 'f':
    elif (strFormat[1] == 'f'): # It is 'f'
        if len(strFormat) > 2:  # It must be the last element in the format string
            _decodeStringErr(strFormat)    
        bIntegerOnly = 0
        iNDigitsAfterDot = 6

    # -----------------------------------------------------------------------
    # It is '.' (dot):
    elif (strFormat[1] == '.'): #

        if len(strFormat) == 2:    # Dot can not be the last digit
            _decodeStringErr(strFormat)

        if not ('0' <= strFormat[2] <= '9'):  # There must be a number after the dot
           _decodeStringErr(strFormat)
            
        # Now read all the numbers after dot
        iNDigitsAfterDot = 0   # Number after dot
        for inxChr in np.arange(2, len(strFormat)-1):  # Loop over all 
            cChr = strFormat[inxChr]
            if not ('0' <= cChr <= '9'):
                _decodeStringErr(strFormat)
            iChrNum = ord(cChr) - 48   # Translate from character to the number
            iNDigitsAfterDot = iNDigitsAfterDot*10 + iChrNum  # Update the number after dot
            bIntegerOnly = 0

        # The last letter after the number must be 'f'
        if not ((strFormat[len(strFormat)-1]) == 'f'):
            _decodeStringErr(strFormat)

    # -----------------------------------------------------------------------            
    # The second character is neither 'd', 'f' nor '.', which is incorrect        
    else:
        _decodeStringErr(strFormat)
        
    return (bIntegerOnly, iNDigitsAfterDot)

# Print error message, if the given format is incorrect 
def _decodeStringErr(strFormat):
    """
    Inputs:
                    
    - 1 **strFormat** (*string*)     Format of printing entires of the array
 
    Output: none
 
    """
    strErr = ('Wrong string with printing format! String > %s < is an incorrect string!') % (strFormat)
    strErr = strErr + (' Correct strings are: %d, %f, %.1f, %.2f, %.3f, %.4f, ...')
    raise ValueError(strErr)


# %%#############################################################################
# Function prints 1D numpy array vertically
#################################################################################
def _1DarrayVert(arrA, strArrayName, strFormat, iRowBrake, bPrintHeader):
    """
    Inputs:
    
    - 1. **arrA** (*Numpy array*)     Array to be printed
            
    - 2 **strArrayName** (*string*)   Name of the array
    
    - 3 **strFormat** (*string*)      Format of printing entires of the array [optional, default = '%f']
                                      Acceptable formats are %d, %f, %.1f, %.2f, %.3f, %.4f, ...

    - 4 **iRowBrake** (*int*)         The number of rows before the column indices are printed again
    
    - 5 **bPrintHeader** (*int*)      Add header with array name, dimension and size?
                                      1 - yes add, 0 - do not add [optional, default = 0]

    Output:

    - 1. **strMessage** (*string*)   String with entries of the numpy array printed vertically

    """

    # Get technial parameters of 1D array printing
    (nEnt, nD, nMaxChrInd, nMaxChrEnt, nMinChrEnt) = _1DgetTechnical(arrA, strFormat, '')
    # nEnt - the number of entries in the array
    # nD   - the number of characters in delimter
    # nMaxChrInd - the maximum number of characters in indices of the array
    # nMaxChrEnt - the maximum number of characters in entries of the array
    # nMinChrEnt - the minimum number of characters in entries of the array

    # Get the printing equalization spaces
    (lSpacesInd, lSpacesEnt, _, _) = _1DcreateEqSpaces(nMaxChrInd, nMaxChrEnt, nMinChrEnt)
    # lSpacesInd - a list with spaces which should be added to indices of an entry
    # lSpacesEnt - a list with spaces which should be added to entries

    # --------------------------------------------------------------------
    # Printing starts here:
    strMessage = _printHeader(arrA, strArrayName, bPrintHeader) # Add a header, if requested
                
    # Loop over all entries in the array
    nDig = 1;   # The number of digits in the current index of an entry
    iThr = 10;  # The next threshold which changes the number of digits 
    strPrintEntry = '\'%s\' %% (arrA[inxEntr])' % (strFormat)  # Create the command which prints a single entry
    for inxEntr in np.arange(nEnt):

        # If the threshold is reached, move forward the number of digits in index of an entry  
        if inxEntr == iThr:
            nDig = nDig + 1
            iThr = iThr * 10  # Move the threshold forward

        # Print index of the current entry and its value
        strMessage = strMessage + ('%d:%s  ') % (inxEntr, lSpacesInd[nDig-1])  # Print index of the current entry
        strEntry = eval(strPrintEntry)                # Print the entry
        nBlankSpace = len(strEntry) - nMaxChrEnt      # Compute the number of blank spaces which must be added after an entry
        if arrA[inxEntr] >= 0:    # If the number is 0 or positive, add a blank space before the number
            strBlankMinus = ' '
        else:
            strBlankMinus = ''
        strMessage = strMessage + strBlankMinus + strEntry + lSpacesEnt[nBlankSpace] + '\n'   # Print the entry
        
        # Add a row brake, if iRowBrake entries where printed without printing a row brake
        if ((inxEntr+1) %  iRowBrake) == 0:
            strMessage = strMessage + '\n'
    
    strMessage = strMessage + '\n'
    return strMessage


# %%#############################################################################
# Function prints 1D numpy array horizontally
#################################################################################
def _1DarrayHori(arrA, strArrayName, strFormat, iRowBrake, strDelimiter, iMaxCols, bPrintHeader):
    """
    Inputs:
    
    - 1. **arrA** (*Numpy array*)     Array to be printed
            
    - 2 **strArrayName** (*string*)   Name of the array
    
    - 3 **strFormat** (*string*)      Format of printing entires of the array 
                                      Acceptable formats are %d, %f, %.1f, %.2f, %.3f, %.4f, ...

    - 4 **iRowBrake** (*int*)         The number of rows before the column indices are printed again

    - 5 **strDelimiter** (*string*)   Delimiter printed between the entries of the array  
                                     
    - 6 **iMaxCols** (*int*)          The maximum number of text columns used ot print a single row 

    - 7 **bPrintHeader** (*int*)      Add header with array name, dimension and size?
                                      1 - yes add, 0 - do not add [optional, default = 0]

    Output:
    
    - 1. **strMessage** (*string*)   String with entries of the numpy array
    """

    # Get technial parameters of 1D array printing
    (nEnt, nD, nMaxChrInd, nMaxChrEnt, nMinChrEnt) = _1DgetTechnical(arrA, strFormat, strDelimiter)
    # nEnt - the number of entries in the array
    # nD   - the number of characters in delimter
    # nMaxChrInd - the maximum number of characters in indices of the array
    # nMaxChrEnt - the maximum number of characters in entries of the array
    # nMinChrEnt - the minimum number of characters in entries of the array

    # Get the printing equalization spaces
    (lSpacesInd, lSpacesEnt, strAddSpaceInd, strAddSpaceEnt) = _1DcreateEqSpaces(nMaxChrInd, nMaxChrEnt, nMinChrEnt)
    # lSpacesInd - a list with spaces which should be added to indices of an entry
    # lSpacesEnt - a list with spaces which should be added to entries
    # strAddSpaceInd - string with an additional space added to indices of entries
    # strAddSpaceEnt - string with an additional space added to  entries
    
    # Get the line printing parameters: the number of lines and number of entries in one line
    (nLines, nEntrypLine, nEntrypLastLine) = _1DgetLineParam(iMaxCols, nEnt, nD, nMaxChrEnt,  strAddSpaceEnt)
    # nLines - the number of lines used to print all the entries from the array
    # nEntrypLine - the number of entries in one line
    # nEntrypLastLine - the number of entries in the last line

    # --------------------------------------------------------------------
    # Printing starts here
    strMessage = _printHeader(arrA, strArrayName, bPrintHeader)    # Add a header, if requested

    # Loop over all lines to be printed
    iStartEntry = 0   # Starting index of the current entry
    for inxLine in np.arange(nLines):
        # If it is the last line, the number of entries is different
        if inxLine == (nLines - 1):
            nEntrypLine = nEntrypLastLine

        strMessage = strMessage + 4 * ' '   # Print the margin
        strMessage = strMessage + _1DprintIndices(arrA, iStartEntry,           # Print indices of entries
                                                  nEntrypLine, lSpacesInd,     # ^
                                                  strAddSpaceInd, nD) + '\n'   # ^

        strMessage = strMessage + 4 * ' '   # Print the margin
        strMessage = strMessage + _1DprintEntries(arrA, iStartEntry,              # Print entries
                                                  nEntrypLine,                    # ^
                                                  strAddSpaceEnt, lSpacesEnt,     # ^
                                                  strDelimiter, strFormat,        # ^
                                                  nMaxChrEnt) + '\n\n'            # ^

        iStartEntry = iStartEntry + nEntrypLine  # Move forward the start entry

    # Add new line at the end of the output string
    strMessage = strMessage + '\n\n'
    return strMessage


# %%#############################################################################
# Function computes technical parametrers of 1D array printing
#################################################################################
def _1DgetTechnical(arrA, strFormat, strDelimiter):
    """

    Inputs:
    
    - 1. **arrA** (*Numpy array*)     Array to be printed
                
    - 2 **strFormat** (*string*)      Format of printing entires of the array 

    - 3 **strDelimiter** (*string*)   Delimiter printed between the entries of the array  


    Output:
    
    - 1. **nEnt** (*int*)         The number of entries in the array

    - 2. **nD** (*int*)           The number of characters in the delimter

    - 3. **nMaxChrInd** (*int*)   The maximum number of characters in indices of the array

    - 4. **nMaxChrEnt** (*int*)   The maximum number of characters in entries of the array

    - 5. **nMinChrEnt** (*int*)   The minimum number of characters in entries of the array
   
    """
    nEnt = arrA.size    # Get the number of entries in 1D array

    (bInt, nM) = _decodeString(strFormat)   # Decode the string with printing format

    # --------------------------------------------------------------------
    # Get the higest number of characters in...

    iMaxAbsInt = np.floor(np.max(np.abs(arrA)))        # ...integer part of entries of the array 
    nX = np.ceil(np.log10(iMaxAbsInt+1)).astype(int)   # ^
    if (nX == 0):                                      # ^
        nX = 1                                         # ^
 
    nC = np.ceil(np.log10(nEnt)).astype(int)       # ...size of the array
    if (nC == 0):
        nC = 1
           
    nD = len(strDelimiter)                             # ...delimiter

    nMaxChrInd = nC + 1               # ... indices of the array (1 because of :)
    
    nMaxChrEnt = nX + nM              # ... entries of the array 
    if bInt == 0:                     # Add 1 because of . in float numbers
        nMaxChrEnt = nMaxChrEnt + 1   # ^
    if (arrA[arrA<0].size) > 0:       # Add 1 because of '-' in negative numbers
        nMaxChrEnt = nMaxChrEnt + 1   # ^

    # ----
    # Get the lowest number of characters in...
    iMinAbsInt = np.floor(np.min(np.abs(arrA)))         # ...integer part of entries of the array 
    nXl = np.ceil(np.log10(iMinAbsInt+1)).astype(int)   # ^
    if nXl == 0:
        nXl = 1

    nMinChrEnt = nXl + nM             # ... entries of the array 
    if bInt == 0:                     # Add 1 because of . in float numbers
        nMinChrEnt = nMinChrEnt + 1   # ^
    if (arrA[arrA>=0].size) == 0:     # Add 1 because of '-' in all negative numbers
        nMinChrEnt = nMinChrEnt + 1   # ^

    # --------------------------------------------------------------------
 
    return (nEnt, nD, nMaxChrInd, nMaxChrEnt, nMinChrEnt)


# %%#############################################################################
# Function creates printing equalization spaces for 1D array printing
#################################################################################
def _1DcreateEqSpaces(nMaxChrInd, nMaxChrEnt, nMinChrEnt):
    """
    Inputs:
    
    - 1. **nMaxChrInd** (*int*)   The maximum number of characters in indices of the array

    - 2. **nMaxChrEnt** (*int*)   The maximum number of characters in entries of the array

    - 3. **nMinChrEnt** (*int*)   The minimum number of characters in entries of the array


    Output:
    
    - 1. **lSpacesInd** (*list*)  A list with spaces which should be added to indices of an entry   

    - 2. **lSpacesEnt** (*list*)  A list with spaces which should be added to entries

    - 3. **strAddSpaceInd** (*string*)  A string with an additional space added to indices of entries
    
    - 4. **strAddSpaceEnt** (*string*)  A string with an additional space added to entries
        
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
    nLongSpace = nMaxChrInd - 2                        # The longest space to be added to indices of entries
    lSpacesInd = []                                    # Start a list with blank spaces
    for iSpaceSize in np.arange(nLongSpace, -1, -1):   # Create a list with blank space
        lSpacesInd.append(iSpaceSize * ' ')

    # Create a list with spaces which should be added to entries
    # These spaces are used to equalize the number of characters in entries  
    # with the number of characters in the longest entry
    nLongSpace = nMaxChrEnt - nMinChrEnt         # The longest space to be added to entries
    lSpacesEnt = []                              # Start a list with blank spaces
    for iSpaceSize in np.arange(nLongSpace+1):   # Create a list with blank spaces
        lSpacesEnt.append(iSpaceSize * ' ')
    
    return (lSpacesInd, lSpacesEnt, strAddSpaceInd, strAddSpaceEnt)


# %%#############################################################################
# Function computes the line printing parameters for 1D array printing
#################################################################################
def _1DgetLineParam(iMaxCols, nEnt, nD, nMaxChrEnt,  strAddSpaceEnt):
    """
    Inputs:
    
    - 1. **iMaxCols** (*int*)        The maximum number of text columns used ot print a single row

    - 2. **nEnt** (*int*)            The number of entries in the array

    - 3. **nD** (*int*)              The number of characters in the delimter
    
    - 4. **nMaxChrEnt** (*int*)      The maximum number of characters in entries of the array
    
    - 5. **strAddSpaceEnt** (*int*)  A string with an additional space added to entries

    Output:
    
    - 1. **nLines** (*int*)           The number of lines used to print all the entries from the array

    - 2. **nEntrypLine** (*int*)      The number of entries in one line

    - 3. **nEntrypLastLine** (*int*)  The number of entries in the last line
        
    """    
    
    # Calculate the maximum number of characters needed to print one entry
    nChr1Entry = len(strAddSpaceEnt) + nMaxChrEnt + nD   # entry additional space + entry + delimiter

    # Compute the number of entries in one line
    nEntrypLine = np.floor((iMaxCols - 4 - 1) / nChr1Entry).astype(int)

    # Check if it is possible to print at least one entry?
    if (nEntrypLine == 0):
        raise ValueError('The requested line is to short to print a single entry')

    # Into how many lines do we have to break the printing?
    nLines = np.ceil(nEnt / nEntrypLine)

    # Compute the number of entries in the last line
    nEntrypLastLine = nEnt - nEntrypLine * (nLines - 1)
    
    return (nLines, nEntrypLine, nEntrypLastLine)



# %%#############################################################################
# Function prints in one line indices of selected entries from a 1D array 
#################################################################################
def _1DprintIndices(arrA, iStartEntry, nEntries, lSpacesInd, strAddSpaceInd, nD):
    """
    Inputs:
    
    - 1. **arrA** (*Numpy array*)       Array to be printed
            
    - 2. **iStartEntry** (*int*)        Index of the first entry to be printed
    
    - 3. **nEntries** (*int*)           The number of entries to be printed 
                                        
    - 4. **lSpacesInd** (*list*)        A list with spaces which should be added to indices of an entry 
                                        
    - 5. **strAddSpaceEnt** (*string*)  Blank spaces before every entry to equalize length of printed entries
                                        with printed indices of column

    - 6. **nD** (*integer*)             The number of characters in delimiter
    
    Output:
    
    - 1. **strMessage** (*string*)   String with indices of entries  
    """

    # Get the lowest number of digits in indices of entries
    if (iStartEntry >= 2):
        nIndDigL = np.ceil(np.log10(iStartEntry)).astype(int)
    else:
        nIndDigL = 1

    strMessage = ''
    nDigs = nIndDigL   # The current number of digits
    iThr = 10**nDigs   # Next threshold which changes the number of digits
    for inxEntry in np.arange(iStartEntry, iStartEntry+nEntries):   # Loop over all entries
        if inxEntry == iThr:     # Threshold is reached
            nDigs = nDigs + 1    # The number of digits
            iThr = iThr * 10     # Threshold
        strMessage = strMessage + ('%s%s%d:%s') % (strAddSpaceInd, lSpacesInd[nDigs-1], inxEntry, nD * ' ')  # Print the entry

    return strMessage


# %%#############################################################################
# Function prints in one line selected entries from a 1D array
#################################################################################
def _1DprintEntries(arrA, iStartEntry, nEntries, strAddSpaceEnt, lSpaces, strDelimiter, strFormat, nMaxChrEnt):
    """
    Inputs:

    - 1. **arrA** (*Numpy array*)       Array to be printed

    - 2. **iStartEntry** (*int*)        Index of the first entry to be printed

    - 3. **nEntries** (*int*)           The number of entries to be printed

    - 4. **strAddSpaceEnt** (*string*)  Blank spaces before every entry to equalieze length of printed entries
                                        with printed indices of column

    - 5. **lSpaces** (*list*)           List with blank spaces used to equalize length of printed entries

    - 6. **strDelimiter** (*string*)    Delimiter printed between the entries

    - 7. **strFormat** (*string*)       Format of printing entires of the array
                                        Acceptable formats are %d, %f, %.1f, %.2f, %.3f, %.4f, ...

    - 8. **nMaxChrEnt** (*integer*)     The maximum possible number of characters used to print one entry from the array

    Output:

    - 1. **strMessage** (*string*)   String with selected entries of the numpy array
    """
    # Create a command which prints a single entry
    strPrintEntry = '\'%s\' %% (arrA[inxEntr])' % (strFormat)

    strMessage = ''
    # Loop over all entries
    for inxEntr in np.arange(iStartEntry, iStartEntry+nEntries):
        strEntry = eval(strPrintEntry)    # Create the current entry
        nChrEntry = len(strEntry)         # The number of characters in the current entry
        nSpace = nMaxChrEnt - nChrEntry   # The lenght of a space which must be added
        strMessage = strMessage + ('%s%s%s%s') % (strAddSpaceEnt, lSpaces[nSpace], strEntry, strDelimiter)  # Print the entry

    return strMessage


# %%#############################################################################
# Function prints 2D numpy array 
#################################################################################
def _2Darray(arrA, strArrayName, strFormat, iRowBrake, strDelimiter, iMaxCols, bPrintHeader):
    """
    Inputs:
    
    - 1. **arrA** (*Numpy array*)     Array to be printed
            
    - 2 **strArrayName** (*string*)   Name of the array
    
    - 3 **strFormat** (*string*)      Format of printing entires of the array [optional, default = '%f']
                                      Acceptable formats are %d, %f, %.1f, %.2f, %.3f, %.4f, ...

    - 4 **iRowBrake** (*int*)         The number of rows before the column indices are printed again

    - 5 **strDelimiter** (*string*)   Delimiter printed between the entries of the array

    - 6 **iMaxCols** (*int*)          The maximum number of text columns used ot print a single row

    - 7 **bPrintHeader** (*int*)      Add header with array name, dimension and size?
                                      1 - yes add, 0 - do not add [optional, default = 0]

    Output:

    - 1. **strMessage** (*string*)   String with entries of the numpy array printed vertically

    """

    # Get technical parameters of 2D array printing
    (nRows, nCols, nD, nMaxChrEnt, nMaxChrIndR, nMaxChrIndC, nMinChrEnt) = _2DgetTechnical(arrA, strFormat, strDelimiter)
    # nRows - the number of rows in the array
    # nCols - the number of columns in the array
    # nD - the number of characters in the delimter
    # nMaxChrEnt  - the maximum number of characters in entries of the array
    # nMaxChrIndR - the maximum number of characters in indices of rows of the array
    # nMaxChrIndC - the maximum number of characters in indices of columns of the array
    # nMinChrEnt - the minimum number of characters in entries of the array

    # Get the printing equalization spaces
    (lSpacesIndC, lSpacesIndR, lSpacesEnt, strAddSpaceIndC, strAddSpaceEnt) = \
        _2DcreateEqSpaces(nMaxChrEnt, nMaxChrIndR, nMaxChrIndC, nMinChrEnt)

    # --------------------------------------------------------------------    
    # Check if it is possible to print at least one entry?

    # Get the  the line printing parameters: the number of lines and number of entries in one line
    (nLines, nEntrypLine, nEntrypLastLine) = _2DgetLineParam(iMaxCols, nCols, nD, nMaxChrEnt, nMaxChrIndR, strAddSpaceEnt)
    # nLines - the number of lines used to print all the entries from the array
    # nEntrypLine - the number of entries in one line
    # nEntrypLastLine - the number of entries in the last line

    # -------------------------------------------------------------------
    # Printing starts here

    # If rows must be broke into many lines, indices of columns must be printed after every row
    if (nLines > 1):    
        iRowBrake = 1

    strMessage = _printHeader(arrA, strArrayName, bPrintHeader)   # Add a header, if requested

    # Loop over all rows of the array
    for inxRow in np.arange(nRows):

        nEntries = nEntrypLine   # The current number of entries printed in a line

        # Loop over all lines printed for the current row
        for inxLine in np.arange(0, nLines):

            # Column index of the first entry to be printed in this line
            inxStartCol = (inxLine * nEntrypLine)

            # The number of entries in the last line is different
            if (inxLine == (nLines - 1)):
                nEntries = nEntrypLastLine

            # Print indices of columns, if needed
            if ((inxRow % iRowBrake) == 0):
                strMessage = strMessage + _2DprintColumns(inxStartCol, nEntries, strAddSpaceIndC, lSpacesIndC, nMaxChrIndR, nD)
 
            # Print index of the current row
            strMessage = strMessage + _2DprintInxRow(inxRow, lSpacesIndR)

            # Print entries from the current row
            strMessage = strMessage + _2DprintRow(arrA, inxRow, inxStartCol, nEntries, nMaxChrEnt, strFormat, strAddSpaceEnt, lSpacesEnt, strDelimiter)
            strMessage = strMessage + '\n'

        # Add a separator at the end of the row
        strMessage = strMessage + '\n'
    return strMessage


# %%#############################################################################
# Function computes technical parameters of 2D-array printing
#################################################################################
def _2DgetTechnical(arrA, strFormat, strDelimiter):
    """

    Inputs:
    
    - 1. **arrA** (*Numpy array*)     Array to be printed
                
    - 2 **strFormat** (*string*)      Format of printing entires of the array 

    - 3 **strDelimiter** (*string*)   Delimiter printed between the entries of the array  


    Output:
    
    - 1. **nRows** (*int*)         The number of rows in the array

    - 2. **nCols** (*int*)         The number of columns in the array

    - 3. **nD** (*int*)            The number of characters in the delimter

    - 4. **nMaxChrEnt** (*int*)    The maximum number of characters in entries of the array

    - 5. **nMaxChrIndR** (*int*)   The maximum number of characters in indices of rows of the array

    - 6. **nMaxChrIndC** (*int*)   The maximum number of characters in indices of columns of the array

    - 7. **nMinChrEnt** (*int*)    The minimum number of characters in entries of the array
   
    """

    (nRows, nCols) = arrA.shape  # Get the dimensions of the array

    (bInt, nM) = _decodeString(strFormat)   # Decode the string with printing format

    # --------------------------------------------------------------------
    # Get the higest number of characters in...
    iMaxAbsInt = np.floor(np.max(np.abs(arrA)))        # ...integer part of elements of the array 
    nX = np.ceil(np.log10(iMaxAbsInt+1)).astype(int)   # ^
    if (nX == 0):                                      # ^
        nX = 1                                         # ^

    nMaxChrEnt = nX + nM                               # ... entries of the array
    if bInt == 0:                                      # Add 1 because of . in float numbers
        nMaxChrEnt = nMaxChrEnt + 1                    # ^
    if (arrA[arrA<0].size) > 0:                        # Add 1 because of '-' in negative numbers
        nMaxChrEnt = nMaxChrEnt + 1                    # ^

    nMaxChrIndR = np.ceil(np.log10(nRows)).astype(int)   # ...the number of rows in the array
    if (nMaxChrIndR == 0):                               # ^
        nMaxChrIndR = 1                                  # ^
    nMaxChrIndR = nMaxChrIndR + 1                        # ^  (1 because of :)

    nMaxChrIndC = np.ceil(np.log10(nCols)).astype(int)   # ...the number of columns in the array
    if (nMaxChrIndC == 0):                               # ^
        nMaxChrIndC = 1                                  # ^
    nMaxChrIndC = nMaxChrIndC + 1                        # ^  (1 because of :)

    nD = len(strDelimiter)                             # ...delimiter
    
    # ----

    # Get the lowest number of characters in...
    iMinAbsInt = np.floor(np.min(np.abs(arrA)))         # ...integer part of elements of the array
    nXl = np.ceil(np.log10(iMinAbsInt+1)).astype(int)   # ^
    if nXl == 0:
        nXl = 1

    nMinChrEnt = nXl + nM             # ... entries of the array 
    if bInt == 0:                     # Add 1 because of . in float numbers
        nMinChrEnt = nMinChrEnt + 1   # ^
    if (arrA[arrA>=0].size) == 0:     # Add 1 because of '-' in all negative numbers
        nMinChrEnt = nMinChrEnt + 1   # ^

    # --------------------------------------------------------------------
    
    return (nRows, nCols, nD, nMaxChrEnt, nMaxChrIndR, nMaxChrIndC, nMinChrEnt)


# %%#############################################################################
# Function creates printing equalization spaces for 2D array printing
#################################################################################
def _2DcreateEqSpaces(nMaxChrEnt, nMaxChrIndR, nMaxChrIndC, nMinChrEnt):
    """

    Inputs:
    
    - 1. **nMaxChrEnt** (*int*)    The maximum number of characters in entries of the array

    - 2. **nMaxChrIndR** (*int*)   The maximum number of characters in indices of rows of the array

    - 3. **nMaxChrIndC** (*int*)   The maximum number of characters in indices of columns of the array

    - 4. **nMinChrEnt** (*int*)    The minimum number of characters in entries of the array

   
    Output:

    - 1. **lSpacesIndC** (*list*)          A list with spaces which should be added to indices of columns
 
    - 2. **lSpacesIndR** (*list*)          A list with spaces which should be added to indices of rows

    - 3. **lSpacesEnt** (*list*)           A list with spaces which should be added to entries

    - 4. **strAddSpaceIndC** (*string*)    A string with an additional space added to indices of entries
    
    - 5. **strAddSpaceEnt** (*string*)     A string with an additional space added to entries

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
    nLongSpaceC = nMaxChrIndC - 1                       # The longest space to be added to indices of columns
    lSpacesIndC = []                                    # Start a list with blank spaces
    for iSpaceSize in np.arange(nLongSpaceC, -1, -1):   # Create a list with blank space
        lSpacesIndC.append(iSpaceSize * ' ')

    # Create a list with spaces which should be added to indices of rows
    # These spaces are used to equalize the number of characters in indices of  
    # rows with the number of characters in the longest index of a rows
    nLongSpaceR = nMaxChrIndR - 1                       # The longest space to be added to indices of rows
    lSpacesIndR = []                                    # Start a list with blank spaces
    for iSpaceSize in np.arange(nLongSpaceR, -1, -1):   # Create a list with blank space
        lSpacesIndR.append(iSpaceSize * ' ')

    # Create a list with spaces which should be added to entries
    # These spaces are used to equalize the number of characters in entries  
    # with the number of characters in the longest entry
    nLongSpace = nMaxChrEnt - nMinChrEnt         # The longest space to be added to entries
    lSpacesEnt = []                              # Start a list with blank spaces
    for iSpaceSize in np.arange(nLongSpace+1):   # Create a list with blank spaces
        lSpacesEnt.append(iSpaceSize * ' ')

    return (lSpacesIndC, lSpacesIndR, lSpacesEnt, strAddSpaceIndC, strAddSpaceEnt)


# %%#############################################################################
# Function computes the line printing parameters for 2D printing
#################################################################################
def _2DgetLineParam(iMaxCols, nCols, nD, nMaxChrEnt, nMaxChrIndR, strAddSpaceEnt):
    """
    Inputs:
    
    - 1. **iMaxCols** (*int*)           The maximum number of text columns used ot print a single row

    - 2. **nCols** (*int*)              The number of columns in the array

    - 3. **nD** (*int*)                 The number of characters in the delimter
    
    - 4. **nMaxChrEnt** (*int*)         The maximum number of characters in entries of the array
    
    - 5. **nMaxChrIndR** (*int*)        The maximum number of characters in indices of row    
    
    - 5. **strAddSpaceEnt** (*string*)  A string with an additional space added to entries

    Output:
    
    - 1. **nLines** (*int*)           The number of lines used to print all the entries from the array

    - 2. **nEntrypLine** (*int*)      The number of entries in one line

    - 3. **nEntrypLastLine** (*int*)  The number of entries in the last line
        
    """    
        
    # Calculate the maximum number of characters needed to print one entry
    nChr1Entry = len(strAddSpaceEnt) + nMaxChrEnt + nD   # entry additional space + entry + delimiter

    # Compute the number of entries in one line
    nEntrypLine = np.floor((iMaxCols - 4 - 1 - nMaxChrIndR) / nChr1Entry).astype(int)
    if (nEntrypLine > nCols):
        nEntrypLine = nCols

    # Check if it is possible to print at least one entry?
    if (nEntrypLine == 0):
        raise ValueError('The requested line is to short to print a single entry')

    # Into how many lines do we have to break the printing?
    nLines = np.ceil(nCols / nEntrypLine)

    # Compute the number of entries in the last line
    nEntrypLastLine = nCols - nEntrypLine * (nLines - 1)

    return (nLines, nEntrypLine, nEntrypLastLine)



# %%#############################################################################
# Function prints indices of columns for 2D array
#################################################################################
def _2DprintColumns(iStartCol, nEntries, strAddSpaceIndC, lSpacesIndC, nMaxChrIndR, nD):
    """
    Inputs:
    
    - 1. **iStartCol** (*int*)            Index of the first columns to be printed

    - 2. **nEntries** (*int*)             The number of entries for which the indices of columns will be printed

    - 3. **strAddSpaceIndC** (*string*)   A string with an additional space added to indices of entries
    
    - 4. **lSpacesIndC** (*list*)         A list with spaces which should be added to indices of columns
    
    - 5. **nMaxChrIndR** (*int*)          A list with spaces which should be added to indices of rows
    
    - 5. **nD** (*int*)                   The number of characters in the delimter

    Output:
    
    - 1. **strMessage** (*string*)   The string with printed requested indices of columns 

    """    
    
    # Print space which is over indices of rows + 2 characters margin
    strMessage = (nMaxChrIndR * ' ') + (2 * ' ')

    # Get the lowest number of digits in indices of columns
    nIndDigL = np.ceil(np.log10(iStartCol+1)).astype(int)
    if nIndDigL == 0:
        nIndDigL = 1

    nDigs = nIndDigL   # The current number of digits
    iThr = 10**nDigs   # Next threshold which changes the number of digits
    
    # Loop over all indices of columns
    for inxCol in np.arange(iStartCol, iStartCol+nEntries):
        if inxCol == iThr:       # Threshold is reached
            nDigs = nDigs + 1    # The number of digits
            iThr = iThr * 10     # Threshold            
        strMessage = strMessage + ('%s%s%d:%s') % (strAddSpaceIndC, lSpacesIndC[nDigs], inxCol, nD * ' ')  # Print the current column
    strMessage = strMessage + '\n'
    return strMessage
    

# %%#############################################################################
# Function prints one index of a row 
#################################################################################
def _2DprintInxRow(inxRow, lSpacesIndR):
    """
    Inputs:
    
    - 1. **inxCol** (*int*)            Index of the row to be printed

    - 2. **lSpacesIndR** (*list*)      A list with spaces which should be added to indices of rows

    Output:
    
    - 1. **strMessage** (*string*)   The string with printed requested index of a row 

    """

    strRowInx = ('%d:') % inxRow                       # Print index of the row
    strSpaceBefore = lSpacesIndR[len(strRowInx) - 1]   # Pick up a correct space which is added before the index
    strMessage = strSpaceBefore + strRowInx            # Connect the above together
    strMessage = strMessage + '  '
    return strMessage

    

# %%#############################################################################
# Function prints entries from the current row for a 2D array
#################################################################################
def _2DprintRow(arrA, inxRow, iStartCol, nEntries, nMaxChrEnt, strFormat, strAddSpaceEnt, lSpacesEnt, strDelimiter):
    """
    Inputs:
    
    - 1. **arrA** (*Numpy array*)           Array to be printed

    - 2. **inxRow** (*int*)                 Index of the rows from which the entries are printed

    - 3. **iStartCol** (*int*)              Index of the first column from which the entries are printed

    - 4. **nEntries** (*int*)               The number of entries to be printed
    
    - 5. **nMaxChrEnt** (*int*)             The maximum number of characters in entries of the array
    
    - 6. **strFormat** (*string*)           Format of printing entries of the array

    - 7. **strAddSpaceEnt** (*string*)      A string with an additional space added to entries   
    
    - 8. **lSpacesEnt** (*list*)            A list with spaces which should be added to entries
    
    - 9. **strDelimiter** (*string*)        Delimiter printed between the entries of the array 


    Output:
    
    - 1. **strMessage** (*string*)   The string with printed requested entries

    """

    # Create a command which prints a single entry
    strPrintEntry = '\'%s\' %% (arrA[inxRow, inxEntr])' % (strFormat)

    strMessage = ''
    # Loop over all entries in a row
    for inxEntr in np.arange(iStartCol, iStartCol+nEntries):
        strEntry = eval(strPrintEntry)    # Create the current entry
        nChrEntry = len(strEntry)         # The number of characters in the current entry  
        nSpace = nMaxChrEnt - nChrEntry   # The lenght of a space which must be added

        strMessage = strMessage + ('%s%s%s%s') % (strAddSpaceEnt, lSpacesEnt[nSpace], strEntry, strDelimiter)  # Print the entry

    return strMessage
