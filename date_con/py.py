def reverseWords(inp):       
    inputWords = inp.split("-") 
    inputWords=inputWords[-1::-1]  
    output = '-'.join(inputWords) 
    return output
def convert(date_string):
    x=date_string.split(' ')
    if(len(x)>1):
        if(x[1]=='Jan.'):
            x[1]="01"
        elif(x[1]=='Feb.'):
            x[1]="02"
        elif(x[1]=='Mar.'):
            x[1]="03"
        elif(x[1]=='Apr.'):
            x[1]="04"
        elif(x[1]=='May'):
            x[1]="05"
        elif(x[1]=='Jun.'):
            x[1]="06"
        elif(x[1]=='Jul.'):
            x[1]="07"
        elif(x[1]=='Aug.'):
            x[1]="08"
        elif(x[1]=='Sep.'):
            x[1]="09"
        elif(x[1]=='Oct.'):
            x[1]="10"
        elif(x[1]=='Nov.'):
            x[1]="11"
        elif(x[1]=='Dec.'):
            x[1]="12"
        if(int(x[0])<=9):
            x[0]="0"+x[0]
    else:
        return date_string
    ret='-'.join(x)
    return(reverseWords(ret))