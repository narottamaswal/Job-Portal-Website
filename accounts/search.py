import requests, random
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta,date
import datetime as ds
from datetime import datetime
import time
from .models import Jobs
import re
from django.db import IntegrityError


def change_date_format(dt):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)

start_time = time.time()

def indeedsearch(searchedminsalary,searchedmaxsalary,searcheddateposted,searchedsalary,searchedcompanyname,searchedskills,searchedlocation,searchedexperience,searchedtitle,searchednoofjobs,searchedjobtype):
    calendar2 = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
                 'Nov': 11, 'Dec': 12}
    user_agent_list = [
        # Chrome
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        # Firefox
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
    ]

    print("yessssssssssssss")
    jobtitlefs = searchedtitle
    experiencefs = searchedexperience
    expfw = experiencefs
    locationfs = searchedlocation
    skillsfs = searchedskills
    salaryfs = searchedsalary
    searchedminsalaryfs=searchedminsalary
    searchedmaxsalaryfs=searchedmaxsalary
    companynamefs = searchedcompanyname
    jobtypefs = searchedjobtype
    datefs = searcheddateposted

    noofjobsfs = searchednoofjobs

    eachjob = int(int(noofjobsfs)/1)
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}

# # variables for indeed search
#     jobtitleindeed = jobtitlefs
#     skillsindeed = skillsfs
#     companynameindeed = companynamefs
#     locationindeed = locationfs
#     searchedminsalayshine=searchedminsalaryfs
#     searchedminsalayshine=searchedmaxsalaryfs
#     url = "https://www.indeed.co.in/jobs?as_and=" + jobtitleindeed + "&as_phr=%22" + skillsindeed + "%22&as_any=&as_not=&as_ttl=&as_cmp=" + companynameindeed + "&jt=all&st=&as_src=&salary=&radius=25&l=" + locationindeed + "&fromage=any&limit=50&sort=date&psf=advsrch&from=advancedsearch"
#     print(url)
#     if not skillsindeed:
#         skillsindeed="not defined"
#     response = requests.get(url, headers=headers)
#     html1 = response.content.decode()
#     soup = BeautifulSoup(html1, 'lxml')
#     q = []
#     data = []
#     b = ""
#     # for printing all the job links in data frame format
#     for i in soup.select("div.jobsearch-SerpJobCard > div.title >a"):
#         b = "https://www.indeed.co.in" + str(i.get('href'))
#         data.append(str(b))
#     # for all the datposted
#     print("1s")
#
#     df = pd.DataFrame(data, columns=['links'])
#     totallinks = df['links'].count()
#     i = 0
#     url2 = []
#     while (i != totallinks):
#         url1 = df['links'].loc[i]
#         url2.append(str(url1))
#         i = i + 1
#     url3 = url2
#     print("2s")
#     if noofjobsfs:
#         url2 = url2[0:eachjob+1]
#     else:
#         try:
#             url2 = url2[0:5]
#         except:
#             url2 = url3
#
#     for i in url2:
#         try:
#             Jobs.objects.get(url=i)
#             continue
#         except:
#             print("3s")
#             print(i)
#             urldb=i
#             jobtypedb=jobtypefs
#             jobportaldb="Indeed"
#             skillsdb=skillsindeed
#             og = ""
#             headers = {'User-Agent': user_agent}
#             response1 = requests.get(i, headers=headers)
#             html1 = response1.content.decode()
#             soup1 = BeautifulSoup(html1, 'lxml')
#
#             try:
#                 i = str(soup1.select("div.jobsearch-jobDescriptionText")[0])
#                 n = 0
#                 for i1 in i:
#                     n = n + 1
#                 i = i[66:n - 6]
#                 jobdescriptiondb=str(i)
#             except:
#                 jobdescriptiondb = "not defined"
#
#             try:
#                 companyname1 = soup1.select("div.icl-u-lg-mr--sm.icl-u-xs-mr--xs")[0].text
#                 companynamedb=companyname1
#             except:
#                 continue
#             jobtitledb=""
#             try:
#                 for j in soup1.select("h3.icl-u-xs-mb--xs.icl-u-xs-mt--none.jobsearch-JobInfoHeader-title"):
#                     jobtitledb=j.text
#             except:
#                 jobtitledb="jobtitle not defined"
#
#             try:
#                 ogl = soup1.select("span#originalJobLinkContainer > a")[0]
#                 ogldb = str(ogl.get('href'))
#             except:
#                 ogldb = "Original Link Not Defined"
#
#             sal = ""
#             exp = ""
#             tim = ""
#             loc = ""
#
#             for q in soup1.select("span.jobsearch-JobMetadataHeader-iconLabel"):
#                 b = q.text
#                 sal1=''
#                 minsaldb=0
#                 maxsaldb=0
#                 minexpdb=0
#                 maxexpdb = 0
#                 sal2=''
#                 if '₹' in b:
#                     sal = b
#                     sal = sal.replace('₹', '')
#                     sal = sal.replace(',', '')
#                     if 'a year' in sal:
#                         sal=sal.replace('a year','')
#                     if 'month' in sal:
#                         #12000 - 16000
#                         sal=sal.replace('a month','')
#                         if len(sal)==12:
#                             minsaldb=0
#                             maxsaldb=int(sal[0:4])*12
#                         else:
#                             for i in range(0, len(sal)):
#                                 if sal[i] == '-':
#                                     minsaldb=int(sal[0:i])*12
#                                     maxsaldb=int(sal[i + 2:i+8])*12
#                     elif 'an hour' in sal:
#                         sal = sal.replace('an hour', '')
#                         for i in range(0, len(sal)):
#                             if sal[i] == '-':
#                                 minsaldb = int(sal[0:i])
#                                 maxsaldb = int(sal[i + 2:])
#                     elif 'a week' in sal:
#                         sal=sal.replace('a week','')
#                         #₹7,000 - ₹15,000 a week
#                         for i in range(0, len(sal)):
#                             if sal[i] == '-':
#                                 minsaldb = int(sal[0:i])
#                                 maxsaldb = int(sal[i + 2:])
#
#                     else:
#                         for i in range(0, len(sal)):
#                             if sal[i] == '-':
#                                 minsaldb=int(sal[0:i])
#                                 print("minimum salary")
#                                 print(minsaldb)
#                                 maxsaldb=int(sal[i + 2:])
#                                 print("maxiumum salary")
#                                 print(maxsaldb)
#
#                     saldb=sal
#
#                 if '+' in b:
#                     exp = b
#                     if 'years' in b:
#                         if b[2]=='+':
#                             maxexpdb=int(exp[0:1])
#                             minexpdb=maxexpdb
#                         else:
#                             maxexpdb=int(exp[0])
#                             minexpdb=maxexpdb
#                     if 'months' in b:
#                         maxexpdb = 1
#                         minexpdb=0
#                 if 'time' in b:
#                     tim = b
#                     jobtypedb=tim
#                 if not '₹' in b:
#                     if not '+' in b:
#                         if not 'time' in b:
#                             loc = b
#                             locdb=loc
#             if sal == "":
#                 minsaldb=0
#                 maxsaldb=0
#                 saldb="not defined"
#             if exp == "":
#                 minexpdb=0
#                 maxexpdb=0
#                 expdb="not defined"
#             if tim == "":
#                 jobtypedb="not defined"
#             if loc == "":
#                 locdb="not defined"
#
#             #date
#             b = []
#             for i in soup1.select("div.jobsearch-JobMetadataFooter"):
#                 b.append(i.text)
#             j = []
#             for l in b:
#                 j.append(l.split('-'))
#             datedb=(j[0][1])
#             datedb3=datedb[1:]
#             if "Just posted" in datedb3:
#                 datedb = ds.date.today()
#             print(datedb3)
#             if "Today" in datedb3:
#                 datedb = ds.date.today()
#             if "ago" in datedb3:
#                 date = datedb3
#                 if date[1] == ' ':
#                     days = int(date[0])
#                     print("days ago1")
#                     print(days)
#                     date = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
#                 else:
#                     days = int(date[0:1])
#                     print("days ago2")
#                     print(days)
#                     date = datetime.strftime(datetime.now() - timedelta(days), '%Y-%m-%d')
#                 datedb=date
#
#             try:
#                 if jobtitledb:
#                     jobtypedb1="FULL-TIME"
#                     print("beefore")
#                     Jobs.objects.create(date=datedb, jobtitle=jobtitledb, companyname=companynamedb,
#                                                          minexp=minexpdb,maxexp=maxexpdb,maxsal=maxsaldb,minsal=minsaldb,location=locdb, originaljoburl=ogldb, url=urldb,
#                                                         jobdescription=jobdescriptiondb, jobportal=jobportaldb, jobtype=jobtypedb1,
#                                                         skills=skillsdb)
#
#                     print("aaftore")
#             except:
#                 continue


#shine.com scraping code starts here

    headers = {'User-Agent': user_agent}

    jobtitleshine = jobtitlefs
    experienceshine = experiencefs
    locationshine = (locationfs)
    skillsshine = skillsfs
    salaryshine = (searchedminsalary)
    companyshine = companynamefs
    jobtypeshine = jobtypefs

    if jobtitleshine:
        jobtitleshine = jobtitleshine.replace(' ', '-')
    ##salary
    ##0 to 2lakhs &fsalary=0
    ##3 to 5      &fsalary=1
    ##6 to 8      &fsalary=2
    ##9 to 12     &fsalary=3
    ##13 to 16    &fsalary=4
    ##17 to 25    &fsalary=5
    ##> than 25   &fsalary=6

    fsalary = "1"
    salaryvalue = "0-200000 a year"
    minsaldb = 0
    maxsaldb = 200000

    if not searchedminsalary:
        fsalary = "1"

    print("308")
    print(searchedminsalary)
    if searchedminsalary:
        if int(searchedminsalary) < (200000):
            minsaldb=0
            maxsaldb=200000
            fsalary="0"
        elif int(searchedminsalary) in range(300000, 599999):
            minsaldb=300000
            maxsaldb=600000
            fsalary = "1"
        elif int(searchedminsalary) in range(600000, 899999):
            minsaldb=600000
            maxsaldb=900000
            fsalary = "2"
        elif int(searchedminsalary) in range(900000, 1299999):
            minsaldb=900000
            maxsaldb=1300000
            fsalary = "3"
        elif int(searchedminsalary) in range(1300000, 1699999):
            minsaldb = 1300000
            maxsaldb = 1700000
            fsalary = "4"
        elif int(searchedminsalary) in range(1700000, 2500000):
            minsaldb = 1700000
            maxsaldb = 2500000
            fsalary = "5"
        elif int(searchedminsalary) > 2500001:
            minsaldb = 2500000
            maxsaldb = 2500000
            fsalary = "6"

    ##experience
    ##>1 &fexp=1
    ##1-2 &fexp=2
    ##3-5 &fexp=3
    ##6-8 &fexp=4
    ##9-10 &fexp=5
    ##11-15 &fexp=6
    expval = "1 years"
    if int(experienceshine) < 1:
        minexpdb=0
        maxexpdb=1
        fexp = "1"
    elif int(experienceshine) in range(1, 2):
        minexpdb = 1
        maxexpdb = 2
        fexp = "2"
    elif int(experienceshine) in range(3, 5):
        minexpdb = 3
        maxexpdb = 5
        fexp = "3"
    elif int(experienceshine) in range(6, 8):
        minexpdb = 6
        maxexpdb = 8
        fexp = "4"
    elif int(experienceshine) in range(9, 10):
        minexpdb = 9
        maxexpdb = 10
        fexp = "5"
    elif int(experienceshine) in range(11, 15):
        minexpdb = 11
        maxexpdb = 15
        fexp = "6"
    else:
        minexpdb = 0
        maxexpdb = 1
        fexp = "1"

    ##
    ##workfromhome emp_type=4
    ##https://www.shine.com/job-search/django-jobs?emp_type=4
    ##
    ##internship
    ##https://www.shine.com/job-search/django-jobs?emp_type=3
    ##
    ##fulltime
    ##https://www.shine.com/job-search/django-jobs?shift_type=1
    ##
    ##parttime
    ##https://www.shine.com/job-search/django-jobs?shift_type=2

    if jobtypeshine == "FULL-TIME":
        jobtypeval = "FULL-TIME"
        jobtypeshine = "1"
    elif jobtypeshine == "PART-TIME":
        jobtypeval = "PART-TIME"
        jobtypeshine = "2"
    elif jobtypeshine == "INTERNSHIP":
        jobtypeval = "INTERNSHIP"
        jobtypeshine = "3"
    elif jobtypeshine == "WORK-FROM-HOME":
        jobtypeval = "WORK-FROM-HOME"
        jobtypeshine = "4"
    else:
        jobtypeval = "FULL-TIME"
        jobtypeshine = "1"

    if locationshine:
        locationshine = locationshine.capitalize()
    url = "https://www.shine.com/job-search/" + jobtitleshine + "-jobs-in-" + locationshine + "?sort=1?loc=" + locationshine + "&fsalary=" + fsalary + "&fexp=" + fexp + "&shift_type=" + jobtypeshine

    print(url)
    response = requests.get(url, headers=headers)
    html1 = response.content.decode()
    soup = BeautifulSoup(html1, 'lxml')
    q = []
    data = []
    b = ""
    totallinks = 0
    # for printing all the job links in data frame format
    for i in soup.select("a.cls_searchresult_a.searchresult_link"):
        b = "https://www.shine.com" + str(i.get('href'))
        #  print(b)
        totallinks = totallinks + 1
        data.append(str(b))
    df = pd.DataFrame(data, columns=['links'])
    i = 0
    url2 = []
    while (i != totallinks):
        url1 = df['links'].loc[i]
        url2.append(str(url1))
        #    print(url2)
        url3 = url2
        i = i + 1

    if eachjob:
        url2 = url2[0:eachjob]
    else:
        try:
            url2 = url2[0:5]
        except:
            url2 = url3
    minexpdb=0
    maxexpdb=1
    count = len(url2)
    for i in url2:
        try:
            Jobs.objects.get(url=i)
           # continue
        except Jobs.DoesNotExist:


            print(i)
            jobportaldb="Shine"
            jobtypedb=jobtypeval
            urldb=i
            ogldb="not defined"
            og = ""
            headers = {'User-Agent': user_agent}
            response1 = requests.get(i, headers=headers)
            html1 = response1.content.decode()
            soup1 = BeautifulSoup(html1, 'lxml')
            # for jobtitle
            jobtitleshine = soup1.select("span.cls_jobtitle > h1")[0].text
            jobtitledb=jobtitleshine

            #job description
            jobdescriptiondb=[]
            for i in soup1.select("div.jobdescriptioninside > span > pre"):
                jobdescriptiondb.append(i.text)
            # Company name
            try:
                companynameshine = soup1.select("span.cls_jobcompany > h2")[0].text
                companynamedb=companynameshine
            except:
                companynamedb="companyname not defined"

            # experience
            try:
                experienceshine = soup1.select("li.cls_jobexperience > i > span")[0].text
                if 'Yr' in experienceshine:
                    experienceshine = experienceshine.replace('Yr', '')
                if 'Yrs' in experienceshine:
                    experienceshine=experienceshine.replace('Yrs','')
                if 'Years' in experienceshine:
                    experienceshine = experienceshine.replace('Years', '')

                for i in range(0, len(experienceshine)):
                    if 'to' in experienceshine:
                        minexpdb=int(experienceshine[0:1])
                        maxexpdb=int(experienceshine[5:6])
                print(experienceshine)
            except:
                minexpdb=0
                maxexpdb=0

            #salary
            sal=""
            try:
                sal = soup1.select("li.cls_jobsalary > i > span")[0].text
            except:
                minsaldb=0
                maxsaldb=0
            print("hiii")
            if sal:
                #Rs 1.0 - 2.5 Lakh/Yr
                #Rs 50,000 - 3.0 Lakh/Yr
                if "Lakh/Yr" in sal:
                    sal=sal.replace("Lakh/Yr","")
                if "Rs" in sal:
                    sal=sal.replace("Rs","")
                if " " in sal:
                    sal=sal.replace(" ","")
                if '.' in sal:
                    sal=sal.replace('.','')
                if ',' in sal:
                    sal=sal.replace(',','')
                #50000-30000
                    minsaldb = int(sal[0:2]) * 10000
                    print(minsaldb)
                print(sal)
                try:
                    if '000' in sal:
                        minsaldb = int(sal[0:5]) * 12
                        print(minsaldb)
                    else:
                        minsaldb=int(sal[0:2])*10000
                        print(minsaldb)
                except:
                    minsaldb=100000

                try:
                    maxsaldb=int(sal[3:])*10000
                    print(maxsaldb)
                except:
                    maxsaldb=200000
            # location
            locationshine = soup1.select("span.normaljdsnippet > a > span")[0].text
            locdb=locationshine
            skillsdb=[]
            # skills
            skills2 = []
            for i in soup1.select("i.sk > span > a"):
                p = i.text
                p = p.replace("\xa0", "")
                p = p.replace(" ", "")
                p = p.replace("\n", "")
                skills2.append(p)
            print(skills2)
            try:
                for i in range(0, len(skills2)-1):
                    if 'Viewall' in skills2[i]:
                        skills2.pop(i)
                skillsdb=skills2
               # print(skillsdb)
            except:
                skillsdb="skills not defined"

            print(skillsdb)
            # dateposted
            try:
                dateposted2 = soup1.select("span.jobDate")[0].text
                print(dateposted2)
                dateposted2 = dateposted2.replace(" ", "")
                dateposted2 = dateposted2.replace("\n", "")
                dateposted2 = dateposted2.replace(",", "")
                print(dateposted2)
                date1 = dateposted2[3:5]
                print(date1)
                month1 = dateposted2[0:3]
                print(month1)
                year1 = dateposted2[5:]
                print(year1)
                date2 = str(year1)+ '-' +str(str(calendar2.get(month1))) + '-' + str(date1)
                print(date2)
                date = datetime.strptime(date2, '%Y-%m-%d').date()
                #date = change_date_format(str(date))
                datedb=(date)
            except:
                datedb="date not defined"
                #-------------------------------
            try:
                Jobs.objects.get(url=urldb)
            except Jobs.DoesNotExist:
                Jobs.objects.create( date=datedb, minsal=minsaldb,maxsal=maxsaldb,jobtitle=jobtitledb, companyname=companynamedb,
                                             minexp=minexpdb,maxexp=maxexpdb,location=locdb, originaljoburl=ogldb, url=urldb,
                                            jobdescription=jobdescriptiondb, jobportal=jobportaldb, jobtype=jobtypedb,
                                            skills=skillsdb)

                print("created")
#
# # #     # Times job
#     user_agent = random.choice(user_agent_list)
#     headers = {'User-Agent': user_agent}
#     sal2 = ""
#     exp2 = ""
#     jobtitletj = jobtitlefs
#     locationtj = locationfs
#     experiencetj = int(experiencefs)
#     if jobtitletj:
#         jobtitletj = jobtitletj.replace(' ', '+')
#
#     url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=" + jobtitletj + "&txtLocation=" + locationtj + "&cboWorkExp1=" + str(
#         experiencetj)
#     print(url)
#
#     response = requests.get(url, headers=headers)
#     html1 = response.content.decode()
#     soup = BeautifulSoup(html1, 'lxml')
#     q = []
#     data = []
#     b = ""
#     totallinks = 0
#     # for printing all the job links in data frame format
#     for i in soup.select("li.clearfix.job-bx.wht-shd-bx > header > h2 > a"):
#         b = str(i.get('href'))
#         #        print(b)
#         totallinks = totallinks + 1
#         data.append(str(b))
#     df = pd.DataFrame(data, columns=['links'])
#     i = 0
#     url2 = []
#     while (i != totallinks):
#         url1 = df['links'].loc[i]
#         url2.append(str(url1))
#         #    print(url2)
#         i = i + 1
#     url3 = url2
#
#     if eachjob:
#         url2 = url2[0:eachjob]
#     else:
#         try:
#             url2 = url2[0:5]
#         except:
#             url2 = url3
#
#     count = len(url2)
#     for i in url2:
#         try:
#             Jobs.objects.get(url=i)
#            # continue
#         except Jobs.DoesNotExist:
#             print(i)
#             urldb=(i)
#             jobportaldb=("Times Jobs")
#             jobtypedb=("FULL-TIME")
#
#             ogldb = "not defined"
#             headers = {'User-Agent': user_agent}
#             response1 = requests.get(i, headers=headers)
#             html1 = response1.content.decode()
#             soup1 = BeautifulSoup(html1, 'lxml')
#     # for jobtitle
#             jobtitle2 = soup1.select("h1.jd-job-title")[0]
#             bb = jobtitle2.text
#             bb = bb.replace("\n", "")
#             bb = bb.replace("\r", "")
#             b = ' '.join(bb.split())
#             jobtitledb=str(b)
#             #for jobdescription
#             jobdescriptiondb=[]
#             for i in soup1.select("div.jd-desc.job-description-main"):
#                 jobdescriptiondb.append(i)
#     #for companyname
#             companynamedb = soup1.select("div.jd-header.wht-shd-bx > h2")[0].text
#             if companynamedb:
#                 companynamedb = companynamedb.replace("\t", "")
#                 companynamedb = companynamedb.replace("\T", "")
#                 companynamedb = companynamedb.replace("\n", "")
#                 companynamedb = companynamedb.replace("\r", "")
#                 companynamedb=(" ".join(companynamedb.split()))
#
#             #for experience,salary and location
#             sal=""
#             for i in soup1.select("ul.top-jd-dtl.clearfix > li"):
#                 if "yrs" in i.text:
#                     exp = i.text
#                     exp = exp.replace(" ", "")
#                     exp2 = " ".join(exp.split())
#                     if "card_travel" in exp2:
#                         exp2 = exp2.replace("card_travel ", "")
#                         minexpdb=int(exp2[0])
#                         maxexpdb = int(exp2[3])
#                     #1to4yrs
#                 elif "₹" in i.text:
#                     if "As per Industry Standards" in i.text:
#                         minsaldb=0
#                         maxsaldb = 0
#                     elif "Best in Industry" in i.text:
#                         minsaldb=0
#                         maxsaldb = 0
#                     else:
#                         sal = i.text
#                         print(sal)
#                         sal = sal.replace("  ", "")
#                         sal2 = " ".join(sal.split())
#                         minsaldb2=searchedminsalary
#                         maxsaldb2=searchedmaxsalary
#                         if 'Lacs p.a.' in sal2:
#                             c = sal2[5:9]
#                             print(c)
#                             d = sal2[12:17]
#                             print(d)
#                             c = (c.replace('.', ''))
#                             d = (d.replace('.', ''))
#                             minsaldb2=int(c)*1000
#                             maxsaldb2 = int(d) * 1000
#                         minsaldb=minsaldb2
#                         maxsaldb = maxsaldb2
#                 else:
#                     loc = i.text
#                     if not loc:
#                         loc2 = "location not defined"
#                         locdb=(loc2)
#                     else:
#                         loc = loc.replace(" ", "")
#                         if "location_on" in loc:
#                             loc = loc.replace("location_on", "")
#                             loc = loc.replace('\n', '')
#                             loc = loc.replace('\t', '')
#                             loc = loc.replace('\r', '')
#                             locdb=str(loc)
#
#             if sal=="":
#                 minsaldb=0
#                 maxsaldb=0
#
#
#             skillsss = []
#             for i in soup1.select("div.clearfix > span.jd-skill-tag > a"):
#                 p = i.text
#                 skillsss.append(p)
#             skillsdb=(skillsss)
#             try:
#                 for i in soup1.select("div.jd-header.wht-shd-bx > ul > li > strong")[1]:
#                     dateposted3 = str(i[10:])
#                     dateposted3 = dateposted3.replace(" ", "-")
#                     dateposted3 = dateposted3.replace(",", "")
#                     date1 = dateposted3[0:2]
#                     month1 = dateposted3[3:6]
#                     year1 = dateposted3[7:11]
#
#                     date2 = str(year1)+ '-' +str(str(calendar2.get(month1))) + '-' + str(date1)
#                     date = datetime.strptime(date2, '%Y-%m-%d').date()
#                   #  date=change_date_format(str(date))
#                     datedb=(str(date))
#             except:
#                 datedb=ds.date.today()
#
#             if not skillsdb:
#                 skillsdb = "skills not defined"
#             if not sal2:
#                 saldb = "salary not defined"
#             if not exp2:
#                 expdb = "experience not defined"
#             if not companynamedb:
#                 companynamedb = "companyname not defined"
#
#             try:
#                 Jobs.objects.get(url=i)
#             except Jobs.DoesNotExist:
#                 Jobs.objects.create(minsal=minsaldb,maxsal=maxsaldb, date=datedb,minexp=minexpdb,maxexp=maxexpdb ,jobtitle=jobtitledb,
#                     companyname=companynamedb,location=locdb, originaljoburl=ogldb, url=urldb,
#                 jobdescription=jobdescriptiondb, jobportal=jobportaldb, jobtype=jobtypedb,skills=skillsdb)
#
# #
# # # # #
# # # # # ## Linked.in scrapper starts here----------------------------------------------------------------------------------------------------
# # # # #
#     user_agent = random.choice(user_agent_list)
#     headers = {'User-Agent': user_agent}
#
#     f_E = "1"
#
#     datepostedlinkedin=datefs
#     locationlinkedin = locationfs
#     jobtitlelinkedinin = jobtitlefs
#     experiencelinkedin = experiencefs
#     print(experiencelinkedin)
#     f_TP = ""
#     ##dateposted
#     ##anytime=""
#     ##past 24 hours= &f_TP=1
#     ##past month=    &f_TP=1%2C2%2C3%2C4
#     ##past week  =   &f_TP=1%2C2
#     ##
#
#     if datepostedlinkedin =='Within1day':
#         f_TP = "1"
#     elif datepostedlinkedin == 'WithinAMonth':
#         f_TP = "1%2C2"
#     elif datepostedlinkedin == 'Within1week':
#         f_TP = "1%2C2%2C3%2C4"
#     elif datepostedlinkedin == 4:
#         f_TP = ""
#
#     if experiencelinkedin:
#         if experiencelinkedin in range(0, 1):
#             minexpdb=0
#             maxexpdb=1
#             f_E = "1"
#         elif experiencelinkedin in range(1, 3):
#             minexpdb = 1
#             maxexpdb = 3
#             f_E = "2"
#         elif experiencelinkedin in range(3, 5):
#             minexpdb = 3
#             maxexpdb = 5
#             f_E = "3"
#         elif experiencelinkedin in range(5, 10):
#             minexpdb = 5
#             maxexpdb = 10
#             f_E = "4"
#         elif experiencelinkedin in range(10, 40):
#             minexpdb = 10
#             maxexpdb = 10
#             f_E = "5"
#     else:
#         f_E = "1"
#     ##
#     ##experience 1-internship         &f_E=1
#     ##            2-entry level- 1-3  &f_E=2
#     ##            3 associate 3-5     &f_E=3
#     ##            4-mi senior 5-10    &f_E=4
#     ##            5 director-10+      &f_E=5
#
#     # space means %20
#     url = "https://www.linkedin.com/jobs/search?keywords=" + jobtitlelinkedinin + "&location=" + locationlinkedin + "&trk=guest_job_search_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0&f_TP=" + f_TP + "&f_E=" + f_E
#     print(url)
#
#     response = requests.get(url, headers=headers)
#     html1 = response.content.decode()
#     soup = BeautifulSoup(html1, 'lxml')
#     data = []
#     for i in soup.select("a.result-card__full-card-link"):
#         #  print(i.get('href'))
#         data.append(str(i.get('href')))
#
#     df = pd.DataFrame(data, columns=['links'])
#     totallinks = df['links'].count() - 1
#     print(totallinks)
#     i = 0
#
#     url2 = []
#     while (i != totallinks):
#         url1 = df['links'].loc[i]
#         url2.append(str(url1))
#         #    print(url2)
#         i = i + 1
#     url3 = url2
#     count = len(url2)
#     print(count)
#
#     if eachjob:
#         url2 = url2[0:eachjob]
#     else:
#         try:
#             url2 = url2[0:5]
#         except:
#             url2 = url3
#
#     for i in url2:
#         try:
#             Jobs.objects.get(url=i)
#         #    continue
#         except Jobs.DoesNotExist:
#
#             urldb=(i)
#             jobportaldb=("Linkedin")
#             skillsdb=("not defined")
#             og = ""
#             headers = {'User-Agent': user_agent}
#             response1 = requests.get(i, headers=headers)
#             html1 = response1.content.decode()
#             soup1 = BeautifulSoup(html1, 'lxml')
#
#             try:
#                 jobtitledb = soup1.select("h1.topcard__title")[0].text
#
#             except:
#                 jobtitledb="job title not defined"
#
#             try:
#                 jobdescriptiondb=[]
#                 jobdescriptiondb.append(soup1.select("div.description__text.description__text--rich")[0].text)
#             except:
#                 jobdescription = "not defined"
#
#             try:
#                 companynamedb = soup1.select("span.topcard__flavor")[0].text
#             except:
#                 companynamedb="companyname not defined"
#             ##
#             try:
#                 applyoriginallink3 = soup1.select("a.apply-button.apply-button--link")[0]
#                 ogldb=applyoriginallink3.get('href')
#             except:
#                 ogldb="applyoriginallink Not defined"
#
#             locdb = soup1.select("span.topcard__flavor.topcard__flavor--bullet")[0].text
#
#
#             try:
#                 jobtype3 = soup1.select("span.job-criteria__text.job-criteria__text--criteria")[1].text
#                 if 'time' or 'full' or 'part' or 'intern' in jobtype3:
#                     jobtypedb=(jobtype3)
#                 else:
#                     jobtypedb="jobtype not defined"
#             except:
#                 jobtypedb="jobtype not defined"
#
#             for i in soup1.select("span.topcard__flavor--metadata.posted-time-ago__text"):
#                 # dateposted=[]
#                 if "day" in i.text:
#                     vard = i.text
#                     vard = int(vard[0])
#                     date = datetime.strftime(datetime.now() - timedelta(vard), '%Y-%m-%d')
#                     datedb=(date)
#                 if "hour" in i.text:
#                     vard = 0
#                     date = datetime.strftime(datetime.now() - timedelta(vard), '%Y-%m-%d')
#                     datedb=(date)
#                 if "week" in i.text:
#                     vard = i.text
#                     vard = int(vard[0]) * 7
#                     date = datetime.strftime(datetime.now() - timedelta(vard), '%Y-%m-%d')
#                     datedb=(date)
#                 if "month" in i.text:
#                     vard = i.text
#                     vard = int(vard[0]) * 30
#                     date = datetime.strftime(datetime.now() - timedelta(vard), '%Y-%m-%d')
#                     datedb=(date)
#             try:
#                 Jobs.objects.get(url=urldb)
#             except Jobs.DoesNotExist:
#                 Jobs.objects.create(minsal=0,maxsal=0, date=datedb,minexp=minexpdb,maxexp=maxexpdb ,jobtitle=jobtitledb,
#                     companyname=companynamedb,location=locdb, originaljoburl=ogldb, url=urldb,
#                 jobdescription=jobdescriptiondb[0], jobportal=jobportaldb, jobtype=jobtypedb,skills=skillsdb)
#
# # #     #return 5
# #
# #
# # #    #####Freshersworld----------------------------------------------------------------------------------------------------------------------
# #
#     user_agent = random.choice(user_agent_list)
#     headers = {'User-Agent': user_agent}
#
#     # freshers
#     ##experience in months 6 month,1 year=12 months
#     ##
#     jobtitlefw = jobtitlefs
#     if jobtitlefw:
#         jobtitlefw = jobtitlefw.replace(' ', '-')
#
#     locationfw= locationfs
#     if locationfw=="india":
#         locationfw=""
#     print(locationfw)
#     experiencefw = expfw
#     if not experiencefw:
#         experiencefw = 0
#     #
#     try:
#         if experiencefw:
#             experiencefw = 12 * experiencefw
#         experiencefw = str(experiencefw)
#     except:
#         experiencefw = 0
#
#     if experiencefw:
#         url = "https://www.freshersworld.com/jobs/jobsearch/" + jobtitlefw + "-jobs-in-" + locationfw + "?experience=" + str(
#             experiencefw)
#     else:
#         url = "https://www.freshersworld.com/jobs/jobsearch/" + jobtitlefw + "-jobs-in-" + locationfw + "?experience=" + str(
#             '0')
#
#     print(url)
#     ##fresher, expereince 0
#     ##6 months, experience=6
#     ##1year, experience=12
#     ##1.5years, experience=18
#     ##2years, experience=24
#     ##2.5 years, experience=30
#     ##3years, experience=36
#     ##3+ years, experience=500
#
#     response = requests.get(url, headers=headers)
#     html1 = response.content.decode()
#     soup = BeautifulSoup(html1, 'lxml')
#
#     links = []
#     # print("links")
#     for i in soup.select("div.col-md-12.col-xs-12.col-lg-12.padding-none.left_move_up > a"):
#         links.append(str(i.get('href')))
#     url3 = links
#
#     if eachjob:
#         links = links[0:eachjob]
#     else:
#         try:
#             links = links[0:5]
#         except:
#             links = url3
#     for link in links:
#         minexpdb=0
#         maxexpdb=0
#         try:
#             Jobs.objects.get(url=link)
#         #    continue
#         except Jobs.DoesNotExist:
#             print(link)
#             urldb=link
#             jobportaldb="Freshersworld"
#             jobtypedb="Full-Time"
#             ogldb="Original link not defined"
#
#             response1 = requests.get(link, headers=headers)
#             html11 = response1.content.decode()
#             soup = BeautifulSoup(html11, 'lxml')
#             try:
#                 date3 = soup.select("span.padding-left-4")[0].text
#                 # print(date)
#                 if date3:
#                     day = date3[0:1]
#                     month = date3[3:5]
#                     year = date3[7:]
#                     month = (calendar2.get(month))
#                     ymd = str(year)+'-'+str(month)+'-'+str(day)
#                     date_str = ymd
#                     date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
#                     datedb=date_object
#
#                 else:
#                     datedb=str(ds.date.today())
#             except:
#                # datedb = str(ds.date.today())
#                # vard = i.text
#                 vard = 1 * 30
#                 date = datetime.strftime(datetime.now() - timedelta(vard), '%Y-%m-%d')
#                 datedb=(date)
#
#             try:
#                 jobtitledb=soup.select("span.latest-jobs-title.font-18")[0].text
#             except:
#                 jobtitledb="jobtitle not found"
#
#             jobdescriptiondb=[]
#             try:#class="col-md-12 col-lg-12 col-xs-12 padding-none job-container"
#                 for i in soup.select("div.col-md-12.col-lg-12.col-xs-12.padding-none.job-container")[0]:
#                     jobdescriptiondb.append(i)
#             except:
#                 jobdescriptiondb="not defined"
#
#             try:
#                 companynamedb=soup.select("div.font-13 > span")[0].text
#             except:
#                 companynamedb="companyname not found"
#                 #
#             try:
#                 locdb=soup.select("span.job-location.display-block.modal-open")[0].text
#             except:
#                 locdb="location not found"
#
#             #
#             lis = []
#             for i in soup.select("div.job-details-sub-div > span.space"):
#                 lis.append(i.text)
#             print(lis)
#             exp = ""
#             sal = ""
#             minsaldb=0
#             maxsaldb=0
#             for j in lis:
#                 if 'Per Month' or '000' in j:
#                     try:
#                         sal = j
#                         sal = sal.replace(' ', '')
#                         print(sal)
#                         if '₹' in sal:
#                             sal = sal.replace('₹', '')
#                         if "PerMonth" in sal:
#                             sal = sal.replace("PerMonth", "")
#                             for i in range(0,len(sal)-1):
#                                 if sal[i]=='-':
#                                     minsaldb=int(sal[0:i])*12
#                                     print(minsaldb)
#                                     maxsaldb=int(sal[i+1:])*12
#                                     print(maxsaldb)
#                     except:
#                         minsaldb=0
#                         maxsaldb = 0
#                 if 'Years' and 'to' or '+' in j:
#                     if not 'Per Month' in j:
#                         expdb = j
#                         expdb=expdb.replace(' ','')
#                         expdb=expdb.replace('+','')
#                         if not '.' in expdb:
#                             expdb=expdb.replace('to','')
#                         expdb=expdb.replace('Years','')
#                         print(expdb)
#                         if len(expdb)<=2:
#                             minexpdb = int(expdb[0:1])
#                             print(minexpdb)
#                             try:
#                                 maxexpdb = int(expdb[1])
#                             except:
#                                 maxexpdb=minexpdb
#                             print(maxexpdb)
#                         else:
#                             if '.' in expdb:
#                                 minexpdb = (expdb[0])
#                                 print(minexpdb)
#                                 maxexpdb = (expdb[5])
#                                 print(maxexpdb)
#
#
#             #['1 Years', '14000 - 16000 Per Month']
#             #['0 to 1 Years']
#             #['0.6 to 3+ Years']
#
#             if sal == "":
#                 minsaldb = int(0)
#                 maxsaldb = int(0)
#             if expdb == "":
#                 minexpdb=int(0)
#                 maxexpdb = int(0)
#             #
#             skillsdb=""
#             try:
#                 skills2 = []
#                 for i in soup.select("span.eligibility-skills.display-block.modal-open > span > a"):
#                     skills2.append(i.text)
#                 skillsdb=(skills2)
#             except:
#                 skillsdb="skills not defined"
#
#             try:
#                 Jobs.objects.get(url=urldb)
#             except Jobs.DoesNotExist:
#                 print("created")
#                 Jobs.objects.create(minsal=minsaldb,maxsal=maxsaldb, date=datedb,minexp=minexpdb,maxexp=maxexpdb ,jobtitle=jobtitledb,
#                     companyname=companynamedb,location=locdb, originaljoburl=ogldb, url=urldb,
#                 jobdescription=jobdescriptiondb, jobportal=jobportaldb, jobtype=jobtypedb,skills=skillsdb)
#                 print("created one")


    return 5

    #        try:
    #            jobdescription.append(soup.select("div.col-md-12.col-lg-12.col-xs-12.padding-none.margin-top-7 > div:nth-child(1)")[4])
    #        except:
    #            jobdescription.append("jobdescription not found")

