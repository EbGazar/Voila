from rply import LexerGenerator, ParserGenerator
from lexer import Lexer
import nltk
from nltk import Tree
import pandas as pd
    
text_input = ""

with open('input.txt') as file:
    for txt in file:
        text_input += txt

lexer = Lexer().get_lexer() #Lexer
tokens = lexer.lex(text_input)

#Symbol Table

dic = {}
i = 0

table = {}
idt = ['int', 'str', 'float' , 'list']
lis = []
lis2 = []
z = 1
try:
    for token in tokens:
        print(token)
        i += 1
        dic[str(i) + " - " + token.gettokentype() ] = token.getstr()

        if token.gettokentype() == "IDENTIFIER" or token.gettokentype() == "STRING" or token.gettokentype() == "NUMBER":

            lis.append(token.getstr())
        
        if token.getstr() == "\n\n" or token.getstr() == "\n     \n" or token.getstr() == "\n    \n" : 
            z += 2

        if token.getstr() == "\n    " or token.getstr() == "\n" or token.getstr() == "\n     ":
            z+= 1
            
        if token.gettokentype() == "IDENTIFIER" or token.gettokentype() == "NEWLINE":
            if token.getstr() == "int" or token.getstr() == 'str' or token.getstr() == 'float':
                continue

            lis2.append(token.getstr())
            lis2.append(z)

except Exception as e:
    print('There was an error: You have entered unrecognized token name!')
    print("Error: " ,e)
    quit()

m = 0
address = {"int" : 2, "str":  4, "lis" : 10, "float" : 4}
k = 0
lis3 = []
lis4 = []

for j in range(len(lis)):
    if m == len(lis):
        break
    if lis[m] == "int" or lis[m] == 'str' or lis[m] == 'float':
        for q in range(len(lis2)):
            if lis[m+1] == lis2[q]:
                lis3.append(lis2[q+1])
                #print(lis[m+1], lis2[q+1])
        lis4.append([lis[m+1],k, lis[m], 1, lis3[0], lis3[1:]])
        k += address[lis[m]]
        m = m + 3
        lis3 = []
    else:
        #print(lis[m])
        m += 1
print()
print("VARIABLE NAME", "    ","OBJECT CODE ADDRESS", "         ","DATA TYPE", "          ","NO OF DIMENSIONS", "      ","LINE OF DECLARATION", "         ","REFRENCE LINE")
print()

for o in lis4:
    for p in o:
        l = 25 - len(str(p))
        print(p," "*l, end = "")

    print()

print()

sym_table = []

for h in lis4:
    sym_table.append({"Name": h[0],"Address": h[1], "Type": h[2],"Dimensions" : h[3] ,"Line Declared": h[4],"Reference Line": h[5]})

for h in sym_table:
    print(h)

#Parse Table from Creating Parse Table docx file

parse_table = {
    'program': {
        'identifier': 'statement_list',
        'print': 'statement_list',
        'if': 'statement_list',
        'while': 'statement_list',
        '$': '$'
    },
    'statement_list': {
        'identifier': 'statement ; statement_list',
        'print': 'statement ; statement_list',
        'if': 'statement ; statement_list',
        'while': 'statement ; statement_list',
        ';': 'statement_list',
        '{': 'statement_list { statement_list } statement_list'
    },
    'statement': {
        'identifier': 'assignment',
        'print': 'print expression ;',
        'if': 'if expression { statement_list }',
        'while': 'while expression { statement_list }'
    },
    'assignment': {
        'identifier': 'identifier = expression ;'
    },
    'print': {
        'print': 'print expression ;'
    },
    'if_statement': {
        'if': 'if expression { statement_list }'
    },
    'while_loop': {
        'while': 'while expression { statement_list }'
    },
    'expression': {
        'identifier': 'term',
        '(': 'term',
        'number': 'term',
    },
    'term': {
        'identifier': 'identifier',
        'string': 'string',
        '(': '( expression )',
        'number': 'number'
    },
    'number': {
        'digit': 'digit'
    },
    'identifier': {
        'identifier': 'identifier ( expression ) op term',
        '(': '( expression ) op term'
    },
    'op': {
        '+': '+ term',
        '-': '- term',
        '*': '* term',
        '/': '/ term'
    },
    'string': {
        'identifier': 'identifier',
        'string': 'string'
    },
    'digit': {'digit' :'digit' }
}

df = pd.DataFrame.from_dict(parse_table, orient='index')
df.index.name = 'Non-terminal'
df.columns.name = 'Terminal'
df.fillna('', inplace=True)
df = df.rename(columns=lambda x: 'digit' if x.isdigit() else x)
print()
print("PARSE TABLE:")
print()
print(df)

#Parse Tree created using rules.

item_1 = ['int', 'str', 'float' , 'list']
prog = "(program "

assign_st = ["IDENTIFIER","IDENTIFIER","EQUALS",["NUMBER" , "STRING", ["NUMBER" , ["PLUS", "MINUS", "TIMES", "DIVIDE"], "NUMBER"]],"SEMI_COLON"]
print_st = ["IDENTIFIER", "LPAREN", ["IDENTIFIER", "NUMBER", "STRING"],"RPAREN","SEMI_COLON"]
if_st = ["IDENTIFIER", "LPAREN", "IDENTIFIER", ["GREATER_THAN", "LESS_THAN", "EQUALS", ">=" , "<="], "NUMBER"," RPAREN","{","IDENTIFIER","LPAREN","IDENTIFIER","RPAREN","SEMI_COLON", "}"]
else_st = ["IDENTIFIER","{","IDENTIFIER","LPAREN","IDENTIFIER","RPAREN","SEMI_COLON", "}"]
while_st = ["IDENTIFIER", "LPAREN", "IDENTIFIER", ["GREATER_THAN", "LESS_THAN", "EQUALS", ">=" , "<="], "NUMBER"," RPAREN","{","IDENTIFIER","LPAREN","IDENTIFIER","RPAREN","SEMI_COLON", "}"]

program1 = []
program2 = []

tokens = lexer.lex(text_input)

w = 0
pr = 0
eq = 0

for token in tokens:
    if token.gettokentype() == "SEMI_COLON":
        w += 1

stmt = 1
tokens = lexer.lex(text_input)

inp1 = []
inp2 = []

for token in tokens:

    if token.getstr() == "\n" or token.gettokentype() == "NEWLINE" or token.getstr() == " " or token.gettokentype() == "NEWLINE" or token.getstr() == "}":
        continue

    inp2.append(token.getstr())
    inp1.append(token.gettokentype())

    if token.gettokentype() == "SEMI_COLON":

        program1.append(inp1)
        program2.append(inp2)

        inp1 = []
        inp2 = []

        if stmt == w:
            break
        stmt += 1

add= ""
for u in range(w):
    if program2[u][0] in item_1 or program2[u][1] in item_1:  #Parse Tree for Assignment Statement
        add += "(stm"
        add += "(assign_stm "
        bro = 0
        eq += 1
        for k in range(len(program1[u])):
            if k == 3:
                if program1[u][3] in assign_st[3][2]:
                    if len(program1[u]) > 6:
                        qqq = k
                        for c in range(2):
                        
                            add += " " + "(" + program1[u][qqq] + " ( " + program2[u][qqq] + " ) " +")"
                            bro += 1
                    
                            if qqq == 3 and program1[u][qqq + 1] in assign_st[3][2][1]:
                                add += " " + "(" + program1[u][qqq + 1] + " ( " + program2[u][qqq + 1] + " ) " +")"
                                bro += 1
                            qqq += 2

                        add += " " + "(" + "SEMI_COLON" +  "(" +   ";" + " ) " +")"
                        bro += 1
                        
                    else:
                        add += " " + "(" + program1[u][3] + " ( " + program2[u][3] + " ) " +")"
                        bro += 1
                        continue
                    break

            if assign_st[k] == program1[u][k]:
                add += " " + "(" + program1[u][k] +  "(" +   program2[u][k] + " ) " +")"
                bro += 1
    #add += "(stms (stm"
    if program2[u][0] == "print": #Parse Tree for Print Statement
        add += "(print_stm "
        bro = 0
        pr += 1

        for k in range(len(program1[u])):
            if k == 2:
                if program1[u][2] in print_st[2]:
                    add += " " + "(" + program1[u][2] + " ( " + program2[u][2] + " ) " +")"
                    bro += 1
            if print_st[k] == program1[u][k]:
                if program2[u][k] == ")" or program2[u][k] == "(" or program2[u][k] == ";":
                    add += " " + program1[u][k]
                    continue                    

                add += " " + "(" + program1[u][k] +  "(" +   program2[u][k] + " ) " +")"
                bro += 1


    if program2[u][0] == "if": #Parse Tree for If Statement
        add += "(if_stm "
        bro = 0
        pr += 1
        for k in range(len(program1[u])):
            if k == 3:
                if program1[u][3] in if_st[3]:
                    add += " " + "(" + "Operator" + " ( " + program2[u][3] + " ) " +")"
                    bro += 1
            if if_st[k] == program1[u][k]:
                if program2[u][k] == ")" or program2[u][k] == "(" or program2[u][k] == ";":
                    add += " " + program1[u][k]
                    continue                    

                add += " " + "(" + program1[u][k] +  "(" +   program2[u][k] + " ) " +")"
                bro += 1


    if program2[u][0] == "while": #Parse Tree for While Statement
        add += "(while_stm "
        bro = 0
        pr += 1
        for k in range(len(program1[u])):
            if k == 3:
                if program1[u][3] in while_st[3]:
                    add += " " + "(" + "Operator" + " ( " + program2[u][3] + " ) " +")"
                    bro += 1
            if while_st[k] == program1[u][k]:
                if program2[u][k] == ")" or program2[u][k] == "(" or program2[u][k] == ";":
                    add += " " + program1[u][k]
                    continue                    

                add += " " + "(" + program1[u][k] +  "(" +   program2[u][k] + " ) " +")"
                bro += 1

    if program2[u][0] == "else": #Parse Tree for Else Statement
        add += "(else_stm "
        bro = 0
        pr += 1
        for k in range(len(program1[u])):
            if else_st[k] == program1[u][k]:
                if program2[u][k] == ")" or program2[u][k] == "(" or program2[u][k] == ";":
                    add += " " + program1[u][k]
                    continue                    

                add += " " + "(" + program1[u][k] +  "(" +   program2[u][k] + " ) " +")"
                bro += 1

    #add += "))"

prog += add
prog += ")"

for p in range(eq):
     prog += "))"

for p in range(pr):
     prog += ")"

parse_tree = prog
tree = Tree.fromstring(parse_tree)
tree.draw()

with open('output.txt', 'w') as f:
    f.writelines(str(dic))