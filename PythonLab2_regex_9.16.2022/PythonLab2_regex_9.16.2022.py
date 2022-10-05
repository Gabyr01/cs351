# \s == Space
# * == 0 or more instances
# ? == 0 or 1 instance
# + == 1 or more instances
# () == grouping or including
# {1,5} == 1 to 5 times of instances
# {5} == 5 instances
# [a-z] == a letter from a to z, a range
# [a-z][a-z] == two letters next to each other
# \d or [0-9] == a digit
# \w == a number or a character [a-zA-Z0-9]
# . == any thing
# ^ == except
import re #for regex
#***********task 1: Pattern matching for strings
def regex(list):

    #loop to go through every element in the list and compare regex pattern 
    for string in list:
        patternFound = 0 # default is 0(false) if pattern is true will change to 1(true)
        #find an integer
        if (re.match("^\d+$",string)):
            message = "An integer."
            result = re.match("^\d+$",string)
            print("%s matches the pattern: %s" %(string,message))
            patternFound=1
        #find A float consists of 1 or more digits before and after decimal point
        if re.match("\d+\.+\d",string):
            message = "A float consists of 1 or more digits before and after decimal point"
            result = re.match("\d+\.+\d",string)    
            print("%s matches the pattern: %s" %(string,message))
            patternFound=1
        #find A float with exactly 2 digits after the decimal point
        if re.match("^\d+\.+\d{2}$",string):
            message = "A float with exactly 2 digits after the decimal point"
            result = re.match("^\d+\.+\d{2}$",string) 
            print("%s matches the pattern: %s" %(string,message))
            patternFound=1
        #find A float end with letter f
        if re.match("\d+\.+\d+[f]",string):
            message = "A float end with letter f"
            result = re.match("\d+\.+\d+[f]",string)
            print("%s matches the pattern: %s" %(string,message))
            patternFound=1
        #find Capital letters, followed by small case letters, followed by digits
        if re.match("^[A-Z]+[a-z]+\d+$", string):
            message = "Capital letters, followed by small case letters, followed by digits"
            result = re.match("^[A-Z]+[a-z]+\d+$",string)
            print("%s matches the pattern: %s" %(string,message))
            patternFound=1
        #Exactly 3 digits, followed by at least 2 letters
        if re.match("^\d{3}[A-Za-z]{2,}$", string):
            message = "Exactly 3 digits, followed by at least 2 letters"
            result = re.match("^\d{3}[A-Za-z]{2,}$",string)
            print("%s matches the pattern: %s" %(string,message))
            patternFound=1
        if patternFound == 0:
                print("%s does not match any available pattern." %string)
#*******Task 2: Remove a part of a string
def removeInt(str):
    result = re.search(r'\d+',str)
    intNumber = str[result.start(): result.end()]
    if (result != None):
        str = str.replace(intNumber, "")
        print("Found integer %s at the beginning of this string, starting at index %s and ending index at %s. The rest of the string is: %s" 
        % (intNumber, result.start(), result.end(),str))
    
    else:
        print("no match")
#********main
if __name__ == '__main__':
    #task1
    print("********Task 1*********")
    listOfStrings = ["22.11","23","66.7f", "123abcde","Case44", "Happy","78", "66.7", "yes123","Book111"]
    regex(listOfStrings)

    #task2
    print("\n********Task 2*********")
    test1 ="22   street"
    test2= "99years"
    removeInt(test1)
    removeInt(test2)