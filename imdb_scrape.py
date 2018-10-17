import requests
from lxml import html
from datetime import date
import smtplib
import config
from date_con import py

def details(show): 
    
    url = 'https://imdb.com/find?q={}'
    #forming the search result url
    r = requests.get(url.format(show.replace(' ', '+')))
    data = html.fromstring(r.content)
    #to extract the search results
    rel = data.xpath('//td[@class="result_text"]/a/@href')
    #no result found 
    if(len(rel)==0):
        print("No such series exists")
        return("No such series exists")
    print(len(rel[0]))
    #to form the url of first search result
    show_details=requests.get('https://www.imdb.com{}'.format(rel[0]))
    
    data2=html.fromstring(show_details.content)
    #url for list of season
    rel2=data2.xpath('//div[@class="seasons-and-year-nav"]/div[3]/a[1]/@href')
    if(len(rel2)==0):
        print("This is not a series")
        return("This is not a series")
    #url for last season
    final=('https://www.imdb.com{}'.format(rel2[0]))
    if(len(final)==0):
        print("This is not a series")
        return("This is not a series")
    print(final)
    dat=requests.get(final)
    data3=html.fromstring(dat.content)
    #finding the list of date of last show detail
    rel3=data3.xpath('//div[@class="airdate"]/text()')
    if(len(rel3)==0):
        print("No such series exist")
        return("No such series exist")
    rem=[]
    #removing the unnecessary empty strings
    for i in rel3:
        if i.strip()=="":
            rem.append(i);
    for i in rem:
        rel3.remove(i)
    cnt=0
    #removing unnecessary spaces in the dates
    for i in rel3:
        rel3[cnt]=rel3[cnt].strip()
        cnt=cnt+1
    cnt=0
    #converting the dates in string format to desired format yyyy-mm-dd
    for i in rel3:
        rel3[cnt]=py.convert(i)
        cnt=cnt+1
    print(rel3)
    date1=rel3[0]
    #if only year is mentioned in date
    if(len(date1)==4):
        print("Next season of " +show+" will be aired in: "+date1)
        return("Next season of "+show+" will be aired in: "+date1)
    else:
        #finding presen day
        present=str(date.today())
        print(present)
        pre=present.split("-")
        date1=rel3[-1]
        a=date1.split('-')
        #comparing year with present year
        if(int(a[0])<int(pre[0])):
            print("All seasons of "+show+" are finished and no other details are available")
            return("All seasons of "+show+" are finished and no other details are available")
        elif(int(a[0])>int(pre[0])):
            print("Next episode of "+show+ " will be aired on: "+'-'.join(a))
            return("Next episode of "+show+ " will be aired on: "+'-'.join(a))
        #if year is same comparing months
        elif(int(a[0])==int(pre[0])):
            if(int(a[1])>int(pre[1])):
                print("Next episode of "+show+" will be aired on: "+'-'.join(a))
                return("Next episode of "+show+" will be aired on: "+'-'.join(a))
            elif(int(a[1])<int(pre[1])):
                print("All seasons of "+show+" are finished and no other details are available")
                return("All seasons of "+show+" are finished and no other details are available")
            #if month is same comparing day
            elif(int(a[1])==int(pre[1])):
                if(int(a[2])<int(pre[2])):
                    print("All seasons of "+show+" are finished and no other details are available")
                    return("All seasons of "+show+" are finished and no other details are available")
                else:
                    print("Next episode of "+show+" will be aired on: "+'-'.join(a))
                    return("Next episode of "+show+ " will be aired on: "+'-'.join(a))
#function for sending email
def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        #message insubject line
        message = 'Subject: {}\n\n{}'.format(subject, msg) 
        server.sendmail(config.EMAIL_ADDRESS,config.receiver_addr, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print('unable to send email check login credentials')
        
list_of_shows=config.l
#print(list_of_shows)
c=0
message=""
#forming the list of all the show details
for i in list_of_shows:
    message=message+i+": "+details(i)+'\n \n'
send_email("Your show details ",message)