''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT
import sys
def main():

    addChar = 0
    for line in sys.stdin:
        str = line
    #str = 'aaacbbb'
    try :
        if str and len(str)%2 != 0 and str.endswith(str[0]) == False:
            addChar = addChar + 1;
            str = str + str[0]
        i = 0
        j = len(str) -1
        while i < j:
            if str[i] == str[j]:
                i = i+1
                j= j-1
            elif str[i] != str[j]:
                str = str[:i] + str[j] + str[i:]
                addChar = addChar + 1;
                i = i + 1
        if str and len(str) % 2 == 0 and str.endswith(str[0]) == False:
            addChar = addChar + 1;
            str = str + str[0]
        i = 0
        j = len(str) - 1
        while i < j:
            if str[i] == str[j]:
                i = i + 1
                j = j - 1
            elif str[i] != str[j]:
                str =  str[:j] + str[i] + str[j:]
                addChar = addChar + 1;
                i = i + 1
        print(addChar)
    except:
        print("Empty String"+str)
main()
