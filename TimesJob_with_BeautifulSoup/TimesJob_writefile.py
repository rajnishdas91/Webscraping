from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml') #parse method.

jobs = soup.find_all("li",class_="clearfix job-bx wht-shd-bx")

for index,job in enumerate(jobs):
    posted = job.find('span', class_='sim-posted').text
    if 'few' in posted:
        company_name = job.find('h3', class_='joblist-comp-name').text#.replace(' ','')

        skill = job.find('span', class_='srp-skills').text.replace(' ','')

        job_info = job.header.h2.a['href']

        with open (f'TimesJob_output/file{index}.txt','w') as f1:

            f1.write(f'Company Name: {company_name.strip()}\n')
            f1.write(f'Required Skill: {skill.strip()}\n')
            f1.write(f'Published on: {posted.strip()}\n')
            f1.write(f'Job Description: {job_info}\n')



