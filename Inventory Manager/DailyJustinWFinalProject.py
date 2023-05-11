"""
Author: Justin W Daily
Date written: 03/09/23
Assignment: DailyJustinWFinalProject
Version of Python: 3.11.1

Short Desc: This program maintains files for a basic inventory database.  The database has a fixed schema.
The user uses the GUI to create files for storing inventory lists, to copy files for storing inventory lists, to output the inventory
from files that store inventory lists, add inventory items to files that store inventory lists, delete items from files that store
inventory lists, and to close the program.
"""

#Import libraries and modules that are necessary for proper program functionality

#Import module for checking file existence
from pathlib import Path

#Import tkinter module for GUI creation
#Import scrolledtext for the output window, to enable inventory output that exceeds the vertical size of the output window
#Import DISABLED and NORMAL to prevent users from directly altering the text in the output window's output textbox
#Import Image and ImageTk from PIL to integrate images into the GUI
#Use try except statement for alternate import of outside modules, if PIL modules cannot be imported
#For PIL modules to function properly, pip needs to be installed in python
    #There is no guarantee that pip will be installed, so PIL should not be imported as a requirement
#All images that require PIL will default to alternate text if PIL modules cannot be imported
try:
    from tkinter import *
    import tkinter as tk
    import tkinter.scrolledtext as scrolledtext
    from tkinter import DISABLED
    from tkinter import NORMAL
    from PIL import Image, ImageTk
except:
    from tkinter import *
    import tkinter as tk
    import tkinter.scrolledtext as scrolledtext
    from tkinter import DISABLED
    from tkinter import NORMAL



#Define functions that are attached to buttons in input window

#Check for main file name validity with checkFile function
#Use decision for correct responses to validity check
#If the validity check has failed, output an error message
#Use fileErrorMessage for error message
#If the validity check has passed, use user input from file entry field
#Add the correct file directory and file extension to the user's filename
#Create a new file with user input value by opening the file with 'w'
#Close the new file after its creation
#Enable the ability to alter text in the output textbox so that output can be placed into the output textbox
#Delete all text in the output textbox to remove clutter
#Output message that informs the user of new file creation by inserting text into output textbox
#Disable the ability to alter text in the output textbox to avoid clutter
def newFile():
    """Create a new file"""
    isValid = checkFile() #isValid is the flag variable that represents whether the user input is valid in validation testing
    if isValid == False:
        fileErrorMessage()
    else:
        fileName = fileEntry.get() #fileName contains the name of the file that is obtained from the main file entry field
        newFile = open("Inventory Files\\" + fileName + ".txt", 'w') #newFile contains a newly created file
        newFile.close()
    outputTextBox["state"] = NORMAL
    outputTextBox.delete('1.0', tk.END)
    outputTextBox.insert(tk.END, "New file created\n")
    outputTextBox["state"] = DISABLED

#Check for main file name validity with checkFile function
#Use decision for correct responses to validity checks
#If the validity check has failed, output an error message
#Use fileErrorMessage function for error message
#Check if main file name is an actual file in the text file directory with inDirectory function
#If the main file name does not exsit, output an error message
#Use notInDirectoryMessage function for error message
#Check for copy file name validity with checkCopy function
#If the validity check has failed, output an error message
#Use copyErrorMessage function for error message
#If the validity checks have passed, move on to the rest of the function
#Use getInventoryDictionary function to obtain inventory dictionary from file
#Use sortInventoryDictionary function to sort the inventory dictionary by SKU
#Save the sorted inventory dictionary to main file with saveToFile function
#Save the sorted inventory dicitonary to copy file with saveToCopy function
#Enable the ability to alter text in the output textbox so that output can be placed into the output textbox
#Delete all text in the output textbox to remove clutter
#Output message that informs the user of copy file creation by inserting text into output textbox
#Disable the ability to alter text in the output textbox to avoid clutter
def copyFile():
    """Copy file contents to a different file"""
    isValid = checkFile() #isValid is the flag variable that represents whether the user input is valid in validation testing
    if isValid == False:
        fileErrorMessage()
    else:
        inDirectory = checkDirectory() #inDirectory is the flag variable that represents whether a text file actually exists in the text file directory
        if inDirectory == False:
            notInDirectoryMessage()
        else:
            isValid = checkCopy() #isValid is the flag variable that represents whether the user input is valid in validation testing
            if isValid == False:
                copyErrorMessage()
            else:
                inventoryDictionary = getInventoryDictionary() #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
                inventoryDictionary = sortInventoryDictionary(inventoryDictionary) #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
                saveToFile(inventoryDictionary)
                saveToCopy(inventoryDictionary)
                outputTextBox["state"] = NORMAL
                outputTextBox.delete('1.0', tk.END)
                outputTextBox.insert(tk.END, "Copy file created\n")
                outputTextBox["state"] = DISABLED

#Check for main file name validity with checkFile function
#Use decision for correct responses to validity checks
#If the validity check has failed, output an error message
#Use fileErrorMessage function for error message
#Check if main file name is an actual file in the text file directory with inDirectory function
#If the main file name does not exsit, output an error message
#Use notInDirectoryMessage function for error message
#If the validity checks have passed, move on to the rest of the function
#Use getInventoryDictionary function to obtain inventory dictionary from file
#Use sortInventoryDictionary function to sort the inventory dictionary by SKU
#Save the sorted inventory dictionary to main file with saveToFile function
#Output sorted inventory dictionary to user with outputInventory function
def openFile():
    """Output inventory from a file"""
    isValid = checkFile() #isValid is the flag variable that represents whether the user input is valid in validation testing
    if isValid == False:
        fileErrorMessage()
    else:
        inDirectory = checkDirectory() #inDirectory is the flag variable that represents whether a text file actually exists in the text file directory
        if inDirectory == False:
            notInDirectoryMessage()
        else:
            inventoryDictionary = getInventoryDictionary() #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
            inventoryDictionary = sortInventoryDictionary(inventoryDictionary) #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
            saveToFile(inventoryDictionary)
            outputInventory(inventoryDictionary)

#Check for main file name validity with checkFile function
#Use decision for correct responses to validity check
#If the validity check has failed, output an error message
#Use fileErrorMessage function for error message
#Check for item input field validity with checkEntry function
#If the validity check has failed, output an error message
#Use entryErrorMessage function for error message
#Check if main file name is an actual file in the text file directory with inDirectory function
#If the main file name does not exsit, output an error message
#Use notInDirectoryMessage function for error message
#If the validity check have passed, move on to the rest of the function
#Use getInventoryDictionary function to obtain inventory dictionary from file
#Use sortInventoryDictionary function to sort the inventory dictionary by SKU
#Use getInventoryItem function to add new item to inventory dictionary
#Use sortInventoryDictionary function to sort the inventory dictionary by SKU
#Save the sorted inventory dictionary to main file with saveToFile function
#Output sorted inventory dictionary to user with outputInventory function
def addToFile():
    """Add an inventory item to a file"""
    isValid = checkFile() #isValid is the flag variable that represents whether the user input is valid in validation testing
    if isValid == False:
        fileErrorMessage()
    else:
        isValid = checkEntry() #isValid is the flag variable that represents whether the user input is valid in validation testing
        if isValid == False:
            entryErrorMessage()
        else:
            inDirectory = checkDirectory() #inDirectory is the flag variable that represents whether a text file actually exists in the text file directory
            if inDirectory == False:
                notInDirectoryMessage()
            else:
                inventoryDictionary = getInventoryDictionary() #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
                inventoryDictionary = sortInventoryDictionary(inventoryDictionary) #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
                inventoryDictionary = getInventoryItem(inventoryDictionary) #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
                inventoryDictionary = sortInventoryDictionary(inventoryDictionary) #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
                saveToFile(inventoryDictionary)
                outputInventory(inventoryDictionary)

#Check for main file name validity with checkFile function
#Use decision for correct responses to validity check
#If the validity check has failed, output an error message
#Use fileErrorMessage function for error message
#Check if main file name is an actual file in the text file directory with inDirectory function
#If the main file name does not exsit, output an error message
#Use notInDirectoryMessage function for error message
#Check for entry field SKU validity with checkSKU function
#If the validity check has failed, output an error message
#Use skuErrorMessage function for error message
#If the validity checks have passed, move on to the rest of the function
#Use getInventoryDictionary function to obtain inventory dictionary from file
#Use sortInventoryDictionary function to sort the inventory dictionary by SKU
#Check if user SKU is in inventory dictionary with checkIfFromFile function
#Use notInFileMessage function to output message if user SKU is not in file
#If user SKU is in the file, set inventorySKU to user SKU from SKU entry field
#Remove SKU entry from inventory dictionary
#Save the altered inventory dictionary to main file with saveToFile function
#Output altered inventory dictionary to user with outputInventory function
def deleteFromFile():
    """Remove an inventory item from a file"""
    isValid = checkFile() #isValid is the flag variable that represents whether the user input is valid in validation testing
    if isValid == False:
        fileErrorMessage()
    else:
        inDirectory = checkDirectory() #inDirectory is the flag variable that represents whether a text file actually exists in the text file directory
        if inDirectory == False:
            notInDirectoryMessage()
        else:
            isValid = checkSKU() #isValid is the flag variable that represents whether the user input is valid in validation testing
            if isValid == False:
                skuErrorMessage()
            else:
                inventoryDictionary = getInventoryDictionary() #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
                inventoryDictionary = sortInventoryDictionary(inventoryDictionary) #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
                inFile = checkIfFromFile(inventoryDictionary) #inFile is the flag variable for whether an inventory item with the user input SKU actually exists in the input file
                if inFile == False:
                    notInFileMessage()
                else:
                    inventorySKU = skuEntry.get() #inventorySKU contains the SKU value for an inventory item in the inventory dictionary
                    inventoryDictionary.pop(inventorySKU)
                    saveToFile(inventoryDictionary)
                    outputInventory(inventoryDictionary)



#Define the sub-functions that the main button functions use

#Use elif decision structure to check for validity of user input from main file entry field
#All forms of invalid input return False for validity variable
#Use loop to check for invalid characters in filename
#Return False for validity variable if any check has failed
#Return True for validity variable if all checks are passed
def checkFile():
    """Check validity of main file name"""
    if fileEntry.get() == "":
        return False
    elif type(fileEntry.get()) != str:
        return False
    else:
        for key in ('/', '\\', '?', '%', '*', ':', '|', '"', '<', '>', '.', ',', ';', '=', ' '):
            if key in fileEntry.get():
                return False
        return True

#Use elif decision structure to check for validity of user input from copy file entry field
#All forms of invalid input return False for validity variable
#Main file entry field must be filled and must be string
#Use loop to check for invalid characters in filename
#Return False for validity variable if any check has failed
#Return True for validity variable if all checks are passed
def checkCopy():
    """Check validity of copy file name"""
    if fileCopyEntry.get() == "":
        return False
    elif type(fileCopyEntry.get()) != str:
        return False
    else:
        for key in ('/', '\\', '?', '%', '*', ':', '|', '"', '<', '>', '.', ',', ';', '=', ' '):
            if key in fileCopyEntry.get():
                return False
        return True

#Obtain filename from user input in a file entry field
#Add the correct file directory and file extension to the user's filename
#Copy file entry field must be filled and must be string
#Use is_file function to check if file actually exists in the text file directory
#Return False if a file with the user's filename does not exist in the text file directory
#Return True if a file with the user's filename actually exists in the text file directory
def checkDirectory():
    """Checks for existence of main file"""
    file = Path("Inventory Files\\" + fileEntry.get() + ".txt") #file contains the name of an input text file
    if file.is_file():
        return True
    else:
        return False

#Use elif decision structure to check for validity of user input from inventory item entry fields
#Use input from inventory item entry fields for inventory item values
#All forms of invalid input return False for validity variable
#No inventory value entry field can be left empty
#The inventory values for SKU, name, and department must be string
#The inventory values for quantity and price must be digits only
#There must be no spaces in any inventory value
#The SKU value must be four characters long
#The remaining inventory values must be below 11 characters long
#Return True for validity variable if all checks are passed
def checkEntry():
    """Check validity of input field values"""
    if skuEntry.get() == "":
        return False
    elif nameEntry.get() == "":
        return False
    elif departmentEntry.get() == "":
        return False
    elif quantityEntry.get() == "":
        return False
    elif priceEntry.get() == "":
        return False
    elif type(skuEntry.get()) != str:
        return False
    elif type(nameEntry.get()) != str:
        return False
    elif type(departmentEntry.get()) != str:
        return False
    elif quantityEntry.get().isdigit() == False:
        return False
    elif priceEntry.get().isdigit() == False:
        return False
    elif " " in skuEntry.get():
        return False
    elif " " in nameEntry.get():
        return False
    elif " " in departmentEntry.get():
        return False
    elif " " in quantityEntry.get():
        return False
    elif " " in priceEntry.get():
        return False
    elif len(skuEntry.get()) != 4:
        return False
    elif len(nameEntry.get()) > 10:
        return False
    elif len(departmentEntry.get()) > 10:
        return False
    elif len(quantityEntry.get()) > 10:
        return False
    elif len(priceEntry.get()) > 10:
        return False
    else:
        return True

#Us elif decision structure to check for validity of user input from SKU entry field
#All forms of invalid input return False for validity variable
#The SKU entry field must be filled
#The SKU value must be string
#The SKU value must not contain spaces
#The SKU value must be four characters long
#Return True for validity variable if all checks are passed
def checkSKU():
    """Check validity of input field SKU"""
    if skuEntry.get() == "":
        return False
    elif type(skuEntry.get()) != str:
        return False
    elif " " in skuEntry.get():
        return False
    elif len(skuEntry.get()) != 4:
        return False
    else:
        return True

#Obtain list of inventory SKUs from inventory dictionary
#Use in to determine if value from SKU entry field is within the list of keys
#Return True for in file variable if SKU is in inventory dictionary
#Return False for in file variable if SKU is not in inventory dictionary
def checkIfFromFile(inventoryDictionary):
    """Check if SKU is in main file"""
    inventorySKUs = list(inventoryDictionary.keys()) #inventorySKUs contains a list of inventory dictionary keys, which are inventory item SKU values
    if skuEntry.get() in inventorySKUs:
        return True
    else:
        return False

#Enable the ability to alter text in the output textbox so that output can be placed into the output textbox
#Delete all text in the output textbox to remove clutter
#Output message for invalid main file name by inserting text into output textbox
#Disable the ability to alter text in the output textbox to avoid clutter
def fileErrorMessage():
    """Output error message for invalid main file name"""
    outputTextBox["state"] = NORMAL
    outputTextBox.delete('1.0', tk.END)
    outputTextBox.insert(tk.END, "Invalid main file name\n" + \
                                 "Main file name field must be filled\n" + \
                                 "Main file name must not contain spaces\n" + \
                                 "Main file name must not contain the following characters:\n" + \
                                 "/ \\ ? % * : | \" < > . , ; =\n")
    outputTextBox["state"] = DISABLED

#Enable the ability to alter text in the output textbox so that output can be placed into the output textbox
#Delete all text in the output textbox to remove clutter
#Output message for invalid copy file name by inserting text into output textbox
#Disable the ability to alter text in the output textbox to avoid clutter
def copyErrorMessage():
    """Output error message for invalid copy file name"""
    outputTextBox["state"] = NORMAL
    outputTextBox.delete('1.0', tk.END)
    outputTextBox.insert(tk.END, "Invalid copy file name\n" + \
                                 "Copy file name field must be filled\n" + \
                                 "Copy file name must not contain spaces\n" + \
                                 "Copy file name must not contain the following characters:\n" + \
                                 "/ \\ ? % * : | \" < > . , ; =\n")
    outputTextBox["state"] = DISABLED

#Enable the ability to alter text in the output textbox so that output can be placed into the output textbox
#Delete all text in the output textbox to remove clutter
#Output message for the main file name not being in the text file directory by inserting text into output textbox
#Disable the ability to alter text in the output textbox to avoid clutter
def notInDirectoryMessage():
    """Output error message for main file name not being in the text file directory"""
    outputTextBox["state"] = NORMAL
    outputTextBox.delete('1.0', tk.END)
    outputTextBox.insert(tk.END, "File not in directory for main file name\n")
    outputTextBox["state"] = DISABLED

#Enable the ability to alter text in the output textbox so that output can be placed into the output textbox
#Delete all text in the output textbox to remove clutter
#Output message for invalid entry field values by inserting text into output textbox
#Disable the ability to alter text in the output textbox to avoid clutter
def entryErrorMessage():
    """Output error message for invalid input field values"""
    outputTextBox["state"] = NORMAL
    outputTextBox.delete('1.0', tk.END)
    outputTextBox.insert(tk.END, "Invalid input\n" + \
                                 "All inventory input fields must be filled\n" + \
                                 "Inventory input must contain zero spaces\n" + \
                                 "SKU must contain four characters\n" + \
                                 "Name must be ten characters or fewer\n" + \
                                 "Department must be ten characters or fewer\n" + \
                                 "Quantity must be digits only\n" + \
                                 "Quantity must be ten digits or fewer\n" + \
                                 "Price must be digits only\n" + \
                                 "Price must be ten digits or fewer\n")
    outputTextBox["state"] = DISABLED

#Enable the ability to alter text in the output textbox so that output can be placed into the output textbox
#Delete all text in the output textbox to remove clutter
#Output message for invalid SKU entry field value by inserting text into output textbox
#Disable the ability to alter text in the output textbox to avoid clutter
def skuErrorMessage():
    """Output error message for invalid input field SKU"""
    outputTextBox["state"] = NORMAL
    outputTextBox.delete('1.0', tk.END)
    outputTextBox.insert(tk.END, "Invalid input\n"\
                                 "SKU field must be filled\n" + \
                                 "SKU must contain four characters\n")
    outputTextBox["state"] = DISABLED

#Enable the ability to alter text in the output textbox so that output can be placed into the output textbox
#Delete all text in the output textbox to remove clutter
#Output message for SKU entry field value not being in main file by inserting text into output textbox
#Disable the ability to alter text in the output textbox to avoid clutter
def notInFileMessage():
    """Output message for SKU not being in main file"""
    outputTextBox["state"] = NORMAL
    outputTextBox.delete('1.0', tk.END)
    outputTextBox.insert(tk.END, "SKU not found in inventory\n")
    outputTextBox["state"] = DISABLED

#Initialize the iventory dictionary
#Set file name for main file to main file entry field value
#Add the correct file directory and file extension to the user's filename
#Set the input file variable to the contents of the main file
#Remove new line from each line in input file
#Create a list of values for each line with split function
#Insert the values that represent the major characteristics of the inventory item into a new list
#Insert the new list into the inventory dictionary
#Use list value from the line that represents the SKU as the key value
#Return the completed inventory dictionary
def getInventoryDictionary():
    """Obtain inventory dictionary from main file"""
    inventoryDictionary = {} #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
    fileName = fileEntry.get() #fileName contains the name of the file that is obtained from the main file entry field
    inputFile = open("Inventory Files\\" + fileName + ".txt", 'r') #inputFile contains the name of the file from which the inventory dictionary is obtained
    for line in inputFile: #line contains each individual line of text from a text file
        line = line.strip()
        line = line.split()
        itemDescriptors = [line[1], line[2], line[3], line[4], line[5]] #itemDescriptors contains the list of values that are associated with an inventory dictionary key
        inventoryDictionary[line[0]] = itemDescriptors
    return inventoryDictionary

#Inialize sorted inventory dictionary
#Obtain list of keys from inventory dictionary
#Sort the list of keys
#Add items to sorted inventory dictionary according to the order in the sorted list of inventory dictionary keys
#Return the completed sorted inventory dictionary
def sortInventoryDictionary(inventoryDictionary):
    """Sort inventory dictionary by SKU"""
    sortedInventoryDictionary = {} #sortedInventoryDictionary contains the inventory dictionary that has been sorted by keys
    sortedInventorySKUs = list(inventoryDictionary.keys()) #sortedInventorySKUs contains a list of sorted inventory dictionary keys, which are inventory item SKU values
    sortedInventorySKUs.sort()
    for key in sortedInventorySKUs: #key contains an individual key in the list of inventory dictionary keys
        sortedInventoryDictionary[key] = inventoryDictionary[key]
    return sortedInventoryDictionary

#Set inventory item variables to appropriate entry field values
#Convert quantity and price to integers
#Pass inventory item variables to addToInventoryDictionary function
    #Function adds inventory item to inventory dictionary
#Return the altered inventory dictionary
def getInventoryItem(inventoryDictionary):
    """Obtain inventory item values from input fields"""
    inventorySKU = skuEntry.get() #inventorySKU contains the inventory item's SKU value, which is used as the key for the inventory dictionary
    inventoryName = nameEntry.get() #inventoryName contains the inventory item's name value, which is placed into a list of values for the inventory item in the inventory dictionary
    inventoryDepartment = departmentEntry.get() #inventoryDepartment contains the inventory item's department value, which is placed into a list of values for the inventory item in the inventory dictionary
    inventoryQuantity = quantityEntry.get() #inventoryQuantity contains the inventory item's quantity value, which is placed into a list of values for the inventory item in the inventory dictionary
    inventoryQuantity = int(inventoryQuantity)
    inventoryPrice = priceEntry.get() #inventoryPrice contains the inventory item's price value, which is placed into a list of values for the inventory item in the inventory dictionary
    inventoryPrice = int(inventoryPrice)
    inventoryDictionary = addToInventoryDictionary(inventoryDictionary, inventorySKU, inventoryName, inventoryDepartment, inventoryQuantity, inventoryPrice) #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
    return inventoryDictionary

#Initialize list for inventory item descriptors
#Calculate inventory value by multiplying inventory quantity by inventory price
#Convert value to integer
#Append inventory item descriptor list with all inventory values except for SKU
#Add list to inventory dictionary with inventory SKU as key
#Return the altered inventory dictionary
def addToInventoryDictionary(inventoryDictionary, inventorySKU, inventoryName, inventoryDepartment, inventoryQuantity, inventoryPrice):
    """Add an inventory item to the inventory dictionary"""
    inventoryDescriptors = [] #inventoryDescriptors contains the inventory item's descriptive values, except for the SKU; the list is added to the inventory dictionary with the SKU acting as the key
    inventoryValue = inventoryQuantity * inventoryPrice #inventoryValue contains the inventory item's total monetary value, which is placed into a list of values for the inventory item in the inventory dictionary
    inventoryValue = int(inventoryValue)
    inventoryDescriptors.append(inventoryName)
    inventoryDescriptors.append(inventoryDepartment)
    inventoryDescriptors.append(inventoryQuantity)
    inventoryDescriptors.append(inventoryPrice)
    inventoryDescriptors.append(inventoryValue)
    inventoryDictionary[inventorySKU] = inventoryDescriptors #inventoryDictionary contains the dictionary of inventory items that are taken from an input file
    return inventoryDictionary

#Set file name for main file to main file entry field value
#Add the correct file directory and file extension to the user's filename
#Set the output file variable to the contents of the main file
#Obtain list of inventory keys
#Sort the list of inventory dictionary keys
#For each key in the inventory dictionary key list, initialize a list for inventory item values
#Add the key and the value for an inventory item to the list
#Use the list of inventory item values to write the inventory item to the output file
#Format each line with a space between each inventory item value
#Add a new line at the end of each inventory item
#Close the output file
def saveToFile(inventoryDictionary):
    """Save the latest inventory dictionary to main file"""
    fileName = fileEntry.get() #fileName contains the name of the file that is obtained from the main file entry field
    outputFile = open("Inventory Files\\" + fileName + ".txt", 'w') #outputFile contains the file into which the inventory dictionary is saved
    inventorySKUs = list(inventoryDictionary.keys()) #inventorySKUs contains a list of inventory dictionary keys, which are inventory item SKU values
    inventorySKUs.sort()
    for key in inventorySKUs: #key contains an individual key in the list of inventory dictionary keys
        inventoryItem = [] #inventoryItem contains all of the values for an inventory item, and the list is used to properly format each inventory item in the output file
        inventoryItem = [key] + inventoryDictionary[key]
        outputFile.write(str(inventoryItem[0]) + " " + \
                         str(inventoryItem[1]) + " " + \
                         str(inventoryItem[2]) + " " + \
                         str(inventoryItem[3]) + " " + \
                         str(inventoryItem[4]) + " " + \
                         str(inventoryItem[5]) + "\n")
    outputFile.close()

#Set file name for copy file to copy file entry field value
#Add the correct file directory and file extension to the user's filename
#Set the output file variable to the contents of the copy file
#Obtain list of inventory keys
#Sort the list of inventory dictionary keys
#For each key in the inventory dictionary key list, initialize a list for inventory item values
#Add the key and the value for an inventory item to the list
#Use the list of inventory item values to write the inventory item to the output file
#Convert each inventory item value to string
#Format each line with a space between each inventory item value
#Add a new line at the end of each inventory item
#Close the output file
def saveToCopy(inventoryDictionary):
    """Save the latest inventory dictionary to copy file"""
    fileName = fileCopyEntry.get() #fileName contains the name of the file that is obtained from the copy file entry field
    outputFile = open("Inventory Files\\" + fileName + ".txt", 'w') #outputFile contains the file into which the inventory dictionary is saved
    inventorySKUs = list(inventoryDictionary.keys()) #inventorySKUs contains a list of inventory dictionary keys, which are inventory item SKU values
    inventorySKUs.sort()
    for key in inventorySKUs: #key contains an individual key in the list of inventory dictionary keys
        inventoryItem = [] #inventoryItem contains all of the values for an inventory item, and the list is used to properly format each inventory item in the output file
        inventoryItem = [key] + inventoryDictionary[key]
        outputFile.write(str(inventoryItem[0]) + " " + \
                         str(inventoryItem[1]) + " " + \
                         str(inventoryItem[2]) + " " + \
                         str(inventoryItem[3]) + " " + \
                         str(inventoryItem[4]) + " " + \
                         str(inventoryItem[5]) + "\n")
    outputFile.close()

#Obtain list of inventory dictionary keys
#Sort the list of inventory dictionary keys
#Enable the ability to alter text in the output textbox so that output can be placed into the output textbox
#Delete all text in the output textbox to remove clutter
#Output table header to output textbox
#For each key value in the list of inventory dictionary keys, initialize a list for inventory item values
#Add the key and the value for an inventory item to the list
#Convert each inventory value to the correct data type
#Use the list of inventory item values to produce a formatted line for output
#Output each line to the output textbox
#Add a new line to each line of output
#Use calculateTotal function to calculate the total value of the inventory
#Output the total value of the inventory as a formatted line
#Disable the ability to alter text in the output textbox to avoid clutter
def outputInventory(inventoryDictionary):
    """Output the latest inventory dictionary to the user"""
    inventorySKUs = list(inventoryDictionary.keys()) #inventorySKUs contains a list of inventory dictionary keys, which are inventory item SKU values
    inventorySKUs.sort()
    outputTextBox["state"] = NORMAL
    outputTextBox.delete('1.0', tk.END)
    outputTextBox.insert(tk.END, "%-6s%-15s%-15s%-15s%-15s%-30s" % ("SKU", "Name", "Department", "Quantity", "Price", "Value") +"\n")
    for key in inventorySKUs: #key contains an individual key in the list of inventory dictionary keys
        inventoryItem = [] #inventoryItem contains all of the values for an inventory item, and the list is used to properly format the output to the user
        inventoryItem = [key] + inventoryDictionary[key]
        inventoryItem[0] = str(inventoryItem[0])
        inventoryItem[1] = str(inventoryItem[1])
        inventoryItem[2] = str(inventoryItem[2])
        inventoryItem[3] = float(inventoryItem[3])
        inventoryItem[4] = float(inventoryItem[4])
        inventoryItem[5] = float(inventoryItem[5])
        outputTextBox.insert(tk.END, "%-6s%-15s%-15s%-15d%-15d%-30d" % (inventoryItem[0], inventoryItem[1], \
                                                                        inventoryItem[2], inventoryItem[3], \
                                                                        inventoryItem[4], inventoryItem[5]) + "\n")
    totalInventoryValue = calculateTotal(inventoryDictionary) #totalInventoryValue contains the total monetary value of all inventory items in the inventory dictionary
    outputTextBox.insert(tk.END, "%-66s%-30d" % ("Total Inventory Value   ", totalInventoryValue) + "\n")
    outputTextBox["state"] = DISABLED

#Initialize total inventory value as zero
#Obtain list of inventory dictionary keys
#Add inventory item key and inventory item values from inventory dictionary to the list of inventory item values for a single inventory item
#For each key in the list of inventory dictioary keys, add the inventory value to the total inventory value
#Use the index for the location of the monetary value for an inventory item to use the correct inventory item value
#Return the total inventory value
def calculateTotal(inventoryDictionary):
    """Calculate the total value of inventory with cost of inventory items"""
    totalInventoryValue = 0 #totalInventoryValue contains the total monetary value of all inventory items in the inventory dictionary
    inventorySKUs = list(inventoryDictionary.keys()) #inventorySKUs contains a list of inventory dictionary keys, which are inventory item SKU values
    for key in inventorySKUs: #key contains an individual key in the list of inventory dictionary keys
        inventoryItem = [] #inventoryItem contains all of the values for an inventory item, and the list is used to properly format the output to the user
        inventoryItem = [key] + inventoryDictionary[key]
        totalInventoryValue += float(inventoryItem[5])
    return totalInventoryValue

#Use destroy function to close the input window
#The output window will automatically be closed due to Toplevel with the input window acting as the root window
def closeProgram():
    """Close both windows of the program"""
    inputWindow.destroy()

#Define the function that will be used to disable the Windows close button
#Use pass so that the functionality of the Windows close button will be passed over
#Function acts a replacement to the default function of the Windows close button
def disableEvent():
    """Disables built-in Windows functions"""
    pass



#Define the input window

#Intantiate window for input from user
#Remove the ability to resize the input window
#Give the input window an appropriate title
inputWindow = tk.Tk() #inputWindow contains the widgets for user input
inputWindow.resizable(width=False, height=False)
inputWindow.title("Inventory Manager")

#Instantiate label for main file entry field
#Instantiate main file entry field
#Use .grid to properly position the widgets
fileLabel = tk.Label(inputWindow, text="Main File Name:") #fileLabel is used to indicate the purpose of the main file entry field
fileLabel.grid(row=0, column=1)
fileEntry = tk.Entry(inputWindow, text="") #fileEntry is used for user input for the main file name
fileEntry.grid(row=0, column=2)

#Instantiate label for copy file entry field
#Instantiate copy file entry field
#Use .grid to properly position the widgets
fileCopyLabel = tk.Label(inputWindow, text="Copy File Name:") #fileCopyLabel is used to indicate the purpose of the copy file entry field
fileCopyLabel.grid(row=1, column=1)
fileCopyEntry = tk.Entry(inputWindow, text="") #fileCopyEntry is used for user input for the copy file name
fileCopyEntry.grid(row=1, column=2)

#Instantiate frame for blank line
#Use .grid to properly position the frame for the blank line
#Instantiate label for blank line
#Set width of blank line so that the entire input window will have an appropriate width
#Use .pack to place the label into the frame
paddingFrameOne = tk.Frame(inputWindow) #paddingFrameOne is used to create a blank line between the file entry fields and the inventory item entry fields
paddingFrameOne.grid(row=2, column=0, columnspan=4)
paddingLabelOne = tk.Label(master=paddingFrameOne, text="", width=40) #paddingLabelOne is used to make paddingFrame visible as an empty space
paddingLabelOne.pack()

#Instantiate label for SKU entry field
#Instantiate SKU entry field
#Use .grid to properly position the widgets
skuLabel = tk.Label(inputWindow, text="SKU:") #skuLabel is used to indicate the purpose of the SKU entry field
skuLabel.grid(row=3, column=1)
skuEntry = tk.Entry(inputWindow, text="") #skuEntry is used for user input for the inventory item's SKU value
skuEntry.grid(row=3, column=2)

#Instantiate label for name entry field
#Instantiate name entry field
#Use .grid to properly position the widgets
nameLabel = tk.Label(inputWindow, text="Item Name:") #nameLabel is used to indicate the purpose of the name entry field
nameLabel.grid(row=4, column=1)
nameEntry = tk.Entry(inputWindow, text="") #nameEntry is used for user input for the inventory item's name value
nameEntry.grid(row=4, column=2)

#Instantiate label for document entry field
#Instantiate document entry field
#Use .grid to properly position the widgets
departmentLabel = tk.Label(inputWindow, text="Department:") #departmentLabel is used to indicate the purpose of the department entry field
departmentLabel.grid(row=5, column=1)
departmentEntry = tk.Entry(inputWindow, text="") #departmentEntry is used for user input for the inventory item's department value
departmentEntry.grid(row=5, column=2)

#Instantiate label for quantity entry field
#Instantiate quantity entry field
#Use .grid to properly position the widgets
quantityLabel = tk.Label(inputWindow, text="Quantity:") #quantityLabel is used to indicate the purpose of the quantity entry field
quantityLabel.grid(row=6, column=1)
quantityEntry = tk.Entry(inputWindow, text="") #quantityEntry is used for user input for the inventory item's quantity value
quantityEntry.grid(row=6, column=2)

#Instantiate label for price entry field
#Instantiate price entry field
#Use .grid to properly position the widgets
priceLabel = tk.Label(inputWindow, text="Price:") #priceLabel is used to indicate the purpose of the price entry field
priceLabel.grid(row=7, column=1)
priceEntry = tk.Entry(inputWindow, text="") #priceEntry is used for user input for the inventory item's price value
priceEntry.grid(row=7, column=2)

#Instantiate frame for blank line
#Use .grid to properly position the frame for the blank line
#Instantiate label for blank line
#Use .pack to place the label into the frame
paddingFrameTwo = tk.Frame(inputWindow) #paddingFrameTwo is used to create a blank line between the inventory item entry fields and the buttons
paddingFrameTwo.grid(row=8, column=0, columnspan=4)
paddingLabelTwo = tk.Label(master=paddingFrameTwo, text="") #paddingLabelTwo is used to make paddingFrameTwo visible as an empty space
paddingLabelTwo.pack()

#Obtain a render for the "New File" icon
#Instantiate "New File" button
#Add "New File" icon to button
#Connect button to newFile command
#Use .grid to properly position the button
#Use try-except statement for if the icon image is not properly loaded
#Have alternate button that uses no image
try:
    newFileImage = Image.open("Icons\\New_File.png") #newFileImage contains the "New_File.png" file, which acts as the "New File" icon
    newFileRender = ImageTk.PhotoImage(newFileImage, master=inputWindow) #newFileRender contains the tkinter render of the "New File" icon
    newFileButton = tk.Button(inputWindow, image=newFileRender, text="New File", compound="top", command=newFile) #newFileButton is used for the creation of new files
    newFileButton.grid(row=9, column=1)
except:
    newFileButton = tk.Button(inputWindow, text="*New File Icon*\nNew File", command=newFile) #newFileButton is used for the creation of new files
    newFileButton.grid(row=9, column=1)

#Obtain a render for the "Copy File" icon
#Instantiate "Copy File" button
#Add "Copy File" icon to button
#Connect button to copyFile command
#Use .grid to properly position the button
#Use try-except statement for if the icon image is not properly loaded
#Have alternate button that uses no image
try:
    copyFileImage = Image.open("Icons\\Copy_File.png") #copyFileImage contains the "Copy_File.png" file, which acts as the "Copy File" icon
    copyFileRender = ImageTk.PhotoImage(copyFileImage, master=inputWindow) #copyFileRender contains the tkinter render of the "Copy File" icon
    copyFileButton = tk.Button(inputWindow, image=copyFileRender, text="Copy File", compound="top", command=copyFile) #copyFileButton is used for copying the contents of one file to another file
    copyFileButton.grid(row=9, column=2)
except:
    copyFileButton = tk.Button(inputWindow, text="*Copy File Icon*\nCopy File", command=copyFile) #copyFileButton is used for copying the contents of one file to another file
    copyFileButton.grid(row=9, column=2)

#Obtain a render for the "Open File" icon
#Instantiate "Open File" button
#Add "Open File" icon to button
#Connect button to openFile command
#Use .grid to properly position the button
#Use try-except statement for if the icon image is not properly loaded
#Have alternate button that uses no image
try:
    openFileImage = Image.open("Icons\\Open_File.png") #openFileImage contains the "Open_File.png" file, which acts as the "Open File" icon
    openFileRender = ImageTk.PhotoImage(openFileImage, master=inputWindow) #openFileRender contains the tkinter render of the "Open File" icon
    openFileButton = tk.Button(inputWindow, image=openFileRender, text="Open File", compound="top", command=openFile) #openFileButton is used for displaying the inventory of a file to the user
    openFileButton.grid(row=10, column=1)
except:
    openFileButton = tk.Button(inputWindow, text="*Open File Icon*\nOpen File", command=openFile) #openFileButton is used for displaying the inventory of a file to the user
    openFileButton.grid(row=10, column=1)

#Obtain a render for the "Add To File" icon
#Instantiate "Add To File" button
#Add "Add To File" icon to button
#Connect button to addToFile command
#Use .grid to properly position the button
#Use try-except statement for if the icon image is not properly loaded
#Have alternate button that uses no image
try:
    addToFileImage = Image.open("Icons\\Add_To_File.png") #addToFileImage contains the "Add_To_File.png" file, which acts as the "Add To File" icon
    addToFileRender = ImageTk.PhotoImage(addToFileImage, master=inputWindow) #addToFileRender contains the tkinter render of the "Add To File" icon
    addToFileButton = tk.Button(inputWindow, image=addToFileRender, text="Add To File", compound="top", command=addToFile) #addToFileButton is used for adding an inventory item to a file
    addToFileButton.grid(row=10, column=2)
except:
    addToFileButton = tk.Button(inputWindow, text="*Add To File*\nAdd To File", command=addToFile) #addToFileButton is used for adding an inventory item to a file
    addToFileButton.grid(row=10, column=2)

#Obtain a render for the "Delete From Inventory" icon
#Instantiate "Delete From Inventory" button
#Add "Delete From Inventory" icon to button
#Connect button to deleteFromFile command
#Use .grid to properly position the button
#Use try-except statement for if the icon image is not properly loaded
#Have alternate button that uses no image
try:
    deleteFromInventoryImage = Image.open("Icons\\Delete_From_Inventory.png") #deleteFromInventoryImage contains the "Delete_From_Inventory.png" file, which acts as the "Delete From Inventory" icon
    deleteFromInventoryRender = ImageTk.PhotoImage(deleteFromInventoryImage, master=inputWindow) #deleteFromInventoryRender contains the tkinter render of the "Delete From Inventory" icon
    deleteFromInventoryButton = tk.Button(inputWindow, image=deleteFromInventoryRender, text="Delete From Inventory", compound="top", command=deleteFromFile) #deleteFromInventoryButton button is used for removing an inventory item from a file
    deleteFromInventoryButton.grid(row=11, column=1)
except:
    deleteFromInventoryButton = tk.Button(inputWindow, text="*Delete From Inventory Icon*\nDelete From Inventory", command=deleteFromFile) #deleteFromInventoryButton button is used for removing an inventory item from a file
    deleteFromInventoryButton.grid(row=11, column=1)

#Obtain a render for the "Close Program" icon
#Instantiate "Close Program" button
#Add "Close Program" icon to button
#Connect button to closeProgram command
#Use .grid to properly position the button
#Use try-except statement for if the icon image is not properly loaded
#Have alternate button that uses no image
try:
    closeProgramImage = Image.open("Icons\\Close_Program.png") #closeProgramImage contains the "Close Program.png" file, which acts as the "Close Program" icon
    closeProgramRender = ImageTk.PhotoImage(closeProgramImage, master=inputWindow) #closeProgramRender contains the tkinter render of the "Close Program" icon
    closeButton = tk.Button(inputWindow, image=closeProgramRender, text="Close Program", compound="top", command=closeProgram) #closeButton is used to close the program
    closeButton.grid(row=11, column=2)
except:
    closeButton = tk.Button(inputWindow, text="*Close Program Icon*\nClose Program", command=closeProgram) #closeButton is used to close the program
    closeButton.grid(row=11, column=2)



#Define the output window

#Instantiate window for output to user
#Use Toplevel to make input window the root window
#Disable the Windows close button so that only the root window can be used to close both windows simultaneously
    #Also prevents error messages that occur when the output window is closed, since many functions require the output window
#Try-except statement is used to select an alternate version of the output window in which the OS close button is not disabled
    #.protocol does not consistently function, so it should not be absolutely necessary in the program
#Remove the ability to horizontally resize the output window
#Give the output window an appropriate title
try:
    outputWindow = tk.Toplevel(inputWindow) #outputWindow act as the source of output to the user
    outputWindow.protocol("WM_DELETE_WINDOW", disableEvent)
    outputWindow.resizable(width=False, height=True)
    outputWindow.title("Inventory List")
except:
    outputWindow = tk.Toplevel(inputWindow) #outputWindow act as the source of output to the user
    outputWindow.resizable(width=False, height=True)
    outputWindow.title("Inventory List")

#Instantiate textbox for output to user
    #Use ScrolledText so that the output textbox will have a vertical scrollbar
#Give the output textbox an appropriate width for output
#Pack textbox into output window
#Make the output textbox expand to match changes in the vertical size of the output window
#Disable the user's ability alter the text in the output textbox to keep the output textbox free of clutter
outputTextBox = scrolledtext.ScrolledText(outputWindow, undo=True, width=100) #outputTextBox contains the output to the user
outputTextBox.pack(fill=tk.Y, expand=True)
outputTextBox["state"] = DISABLED



#Set inputWindow to mainloop
inputWindow.mainloop()
