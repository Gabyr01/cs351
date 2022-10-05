
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
import re

# This is how you can use findall function with regular expression
# to find substrings in a long string
def findall_example():
    #r'your regex': this format tells python that this string is a special regex pattern
    print(re.findall(r'\s\d{1,5}\s', 'this 45 is a random string asr234a 98asd82 23 d*&@'))

    #What is the returned result?

#This is how you can use the match function to test if a entire string matches to your regex
def match_example():
    result1=re.match(r'\d\s\w+', '4th street')
    if (result1 != None):
        print("a match found")
    else:
        print("no match")

    result2=re.match(r'\d\s\w+', '4 street abc asdfae')
    if (result2 != None):
        print("a match found")
        print(result2)
        print('Starting Position: ', result2.start())
        print('End Position', result2.end())
    else:
        print("no match")



#This is how you can use the search function to see if a certain substring is in a long str
def search_example():
    result = re.search(r'\d+','asdfaf 101 Math; 102 Biology; 105 CS')
    print(result)
    print('Starting Position: ', result.start())
    print('End Position', result.end())

#If you will use the same regular expression multiple times, you can compile it into an object
def compile_example():
    myregexInt = re.compile('\d+')
    result = myregexInt.search('101 Math; 102 Biology; 105 CS')
    print(result)
    print('Starting Position: ', result.start())
    print('End Position', result.end())

if __name__ == '__main__':
    floatFind("I bought 5.2lb of apples and 2.4lb of pears.")
    #floatFindStart()
    #print("##### Find example ####")
    #findall_example()
    #print("##### Match example ####")
    #match_example()
    #print("##### Search example ####")
    #search_example()
    #print("##### Compile example ####")
    compile_example()
