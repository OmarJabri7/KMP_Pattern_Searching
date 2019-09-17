#The Knuth Morris Pratt algorithm is different than the Brute Force algorithm where it reduces time complexity
#and it eliminates unecessary comparisons by creating a lps array (Longest Prefix Suffix), which it will use
#to properly assign a starting point in the text string instead of using the same starting point over and over again
def KMP(pattern,text):
    textLen = len(text)
    patternLen = len(pattern)
    i = 0 #Assigning starting point for text string
    j = 0 #Assigning starting pont for patterns string
    lpsArray = [0]*patternLen #Creating an lps array of size equal pattern string length
    prefixSuffixFunctionLPS(pattern,patternLen,lpsArray) #Calling lps function to calculate the lps array
    while (i<textLen):
        if(pattern[j] == text[i]): #Checking if characters match, if yes increment starting points on both strings
            j+=1
            i+=1
        if(j==patternLen): #Representing that the last character of pattern string has been achieved and a match has been found
            print('Bug found at index ' + str(i-j))
            j = lpsArray[j-1] #Matching stopped at index j, hence we use the lps array to assign the new starting point to
            #lps[where the matching stopped], then the value within the lps will be the starting point in the pattern string
        elif(i<textLen and pattern[j]!=text[i]): #Upong mismatch, to reduce time complexity, we eliminate unecessary comparisons
        #by skipping the comparisons already known to be different and by skipping the suffix in the compared substring in the
        #text string
            if(j!=0):
                j = lpsArray[j-1]
            else:
                i+=1
#We preprocess the pattern before searching for it in the main text
#This function helps us minimize complexity time by finding the longest suffix and prefix in the current string,
#which helps us in finding the right starting point in the main text. This will lead in skipping unecessary comparisons
#and jumping to the character after the prefix in the pattern which is the suffix in the text.

def prefixSuffixFunctionLPS(pattern,patternLen,lpsArray):
    lps = 0 #Initialize first lenght of previous longest prefix suffix to be 0
    lpsArray[0] = 0 #Initialize first index of lps array to be 0 since first element does not have a prefix or suffix that matches
    i = 1 #Hence start iteratinng at index 1
    while(i<patternLen): #lps[i] matches the longest prefix which is also a suffix of the pattern
    #for lps[i] we takee two characters to check if there is any substring that is both prefix and suffix
        if(pattern[i] == pattern[lps]):#if the two chaacters match then we found one substring who is both a prefix and a suffix
            lps +=1 #we increment the length of the lps
            lpsArray[i] = lps #assign its value
            i+=1 #and increment the counter to continue our computations.
        else:
            if(pattern[i]!=pattern[lps]):#if the two chatacters do not match then we either take the length of the previous substring
            #of lps if the lps is not 0, or if it is it will turn it into a 0
                if(lps!=0):
                    lps = lpsArray[lps-1]
                else:
                    lpsArray[i] = 0
                    i+=1
#main function that reads the files and turns them into proper string inputs for further KMP searching
f=open("bug.txt", "r")
contents = f.read()
test_data = open("landscape.txt","r")
contents_test = test_data.read()
pattern = "".join(contents.split())
text = "".join(contents_test.split())
KMP(pattern, text)
