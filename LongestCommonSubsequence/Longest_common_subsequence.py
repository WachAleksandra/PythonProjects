import difflib
import termcolor
import sys

f1 = sys.argv[1]
f2 = sys.argv[2]
file_1 = open(f1, 'r')
file_2 = open(f2, 'r')
file_1_line = file_1.readlines()
file_2_line = file_2.readlines()

def search(file_1_line, file_2_line):
    for iterator in range(len(file_1_line)):
        line_1 = file_1_line[iterator]
        line_2 = file_2_line[iterator]
        matrix = [["" for x in range(len(line_2))] for x in range(len(line_1))]
        for i in range(len(line_1)):
            for j in range(len(line_2)):
                if line_1[i] == line_2[j]:
                    if i == 0 or j == 0:
                        matrix[i][j] = line_1[i]
                    else:
                        matrix[i][j] = matrix[i-1][j-1] + line_1[i]
                else:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)
                    
        cs = matrix[-1][-1]                
        print('Longest common subsequence:',cs.rstrip(), len(cs.rstrip()))  #usuwa białe znaki z końca
        
def diff(file_1_line, file_2_line):
    for iterator in range(len(file_1_line)):
        line_1 = file_1_line[iterator]
        line_2 = file_2_line[iterator]
        cases=[(line_1,line_2)] 
        for a,b in cases:     
            print('{} => {}'.format(a,b))  
            for i,s in enumerate(difflib.ndiff(a, b)): #porownanie, enumerate iterowanie po el. sekwencji i otrzymanie indeksu danego elementu oraz wartości elementu
                if s[0]==' ': continue
                elif s[0]=='-':
                    print(u'Removed "{}" from position {}'.format(s[-1],i))
                elif s[0]=='+':
                    print(u'Added "{}" to position {}'.format(s[-1],i))
                    
def comparison(file_1_line, file_2_line):
    print("Compare files ", " + " + 'file1.txt', " - " + 'file2.txt', sep='\n')
    print()
    for iterator in range(len(file_1_line)):
        line_1 = file_1_line[iterator]
        line_2 = file_2_line[iterator]
        if line_1 != '' or line_2 != '':
            if line_1 == line_2:
                print("Same lines", termcolor.colored("=" + line_1.rstrip(), 'green', attrs=["reverse", "blink"]), "", sep='\n')
            elif line_1 != line_2:
                print("Different line", termcolor.colored("+" + line_1.rstrip(),'red', attrs=["reverse", "blink"]),
                        termcolor.colored("-" + line_2.rstrip(),'yellow', attrs=["reverse", "blink"]), "", sep='\n')
                
        
search(file_1_line, file_2_line)
print()
diff(file_1_line, file_2_line)
print()
comparison(file_1_line, file_2_line)