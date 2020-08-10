import requests,pandas as pd
from bs4 import BeautifulSoup

#url
r = requests.get("https://www.indeed.com/jobs?as_and=software%20engineering%202021&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&as_src&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=feb8c8fef1d0b421")

soup = BeautifulSoup(r.text,"html.parser")
print(soup.prettify())
#csv file
file= pd.DataFrame(columns=["Location","Company","Summary","Title"])

#job titles
def job_title(soup): 
    jobs = []
    for div in soup.find_all(name="div", attrs={"class":"row"}):
      for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
          jobs.append(a["title"])
    return(jobs)


#companies name
def company(soup):
    company_names=[]
    for div in soup.find_all(name="div",attrs={"class":"row"}):
        companies = div.find_all(name="span",attrs={"class":"company"})
        for company in companies:
                company_names.append(company.text.strip())
        else:
            companies2 = div.find_all(name="span",attrs={"class":"turnstileLink"})
            for company in companies2:
                    company_names.append(company.text.strip())
    return(company_names)


#locations
def location(soup):
    locations = []
    cities = soup.findAll('span',attrs={'class':'location'})
    for city in cities:
        locations.append(city.text)
    return locations



#descriptions
def summary(soup): 
      descriptions= []
      summaries= soup.findAll('span', attrs={'class': 'div'})
      for summary in summaries:
        descriptions.append(summary.text.strip())
      return descriptions

#test csv 
#for i in range(0,len(location(soup)),2):
   # file= file.append({"Job":location(soup)[i],"Company":location(soup)[i+1]},ignore_index=True)
#file.to_csv("IndeedScraping.csv")

job_title(soup)
company(soup)
location(soup)
summary(soup)