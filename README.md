# CFG_Final_Project

Using online datasets and APIs, we have used a combination of analytical libraries and python to analyse the gender split from secondary school through to graduate outcomes, with a focus on educational influences. We have worked from the point of view of consulting for a client who wishes to address the following: 
1. What outcomes are being achieved by females at secondary and higher education levels, and how does this differ from outcomes for males? 
2. Is there an increase in the number of females studying computer science-based subjects and in females entering the technology industry? 
3. Is there a link between geographical location and the educational outcomes for females? 

You can find our report in the main folder titled report.doc and report.pdf. Each of the following folders contains a jupyter notebook, and any relevant resources for that specific analysis. 

<details>
<summary>TBC Claire</summary>
```
CODE!
```
</details>

<details>
<summary>Higher Education Data Files and Instructions </summary>
  
  The Higher Education data used in the analysis for this project is from the Higher Education Statistics Agency (HESA) website [Data and analysis | HESA](https://www.hesa.ac.uk/data-and-analysis). Data from the Students and Graduates open data sets have been used. Each notebook references the tables download for analysis.
Each notebook details the process undertaken for data cleaning and analysis.


  | HE Enrolment Jupyter Notebooks   | Data Files |
| ----------- | ----------- |
|HE student enrolments by subject of study.ipynb| HE student enrolments by HE provider 2014-5 FT.xlsx |
|HE Student Enrolment by Provider - Percentage of Female Students.ipynb|HE student enrolments by HE provider 2015-6 FT.xlsx|
|HE Student Enrolment by Provider - top and bottom 10 female students.ipynb|HE student enrolments by HE provider 2016-7 FT.xlsx|
|Total First Year Student Enrolments 2011-2021.ipynb|HE student enrolments by HE provider 2017-8 FT.xlsx|
|%change.ipynb|HE student enrolments by HE provider 2018-9 FT.xlsx|
|%change.ipynb|HE student enrolments by HE provider 2019-20 FT.xlsx|
|Initial HESA Student Data Review.ipynb | HE student enrolments by HE provider 2020-1 FT.xlsx|
| |HE student enrolments by subject of study 2019-0 PT.xlsx|
|| HE student enrolments by subject of study 2020-1 PT.xlsx
| |HE student enrolments by subject of study FT 2019-0.xlsx|
||HE student enrolments by subject of study FT 2020-1.xlsx|
||Percentage of HE student enrolments in science subjects by personal characteristics.xlsx|
||HESA Data - Personal Characteristics.xlsx|

| Graduate Outcomes   | Data Files |
| ----------- | ----------- |
| Graduate Data Cleaning.ipynb| Percentage of graduates in full-time paid employment in the UK by salary band and personal characteristics 2017-8.xlsx|
|Graduate Outcomes by Activity.ipynb | Percentage of graduates in full-time paid employment in the UK by salary band and personal characteristics 2018-9.xlsx |
| Graduate salaries.ipynb| Percentage of graduates in full-time paid employment in the UK by salary band and personal characteristics 2019-20.xlsx |
| Initial HESA Graduate Data Review.ipynb |PG Grad Outcomes 2018-9.xlsx |
| | PG Grad Outcomes 2019-0.xlsx|
| | UG FT Grad outcomes 2018-9.xlsx |
| | UG FT Grad outcomes 2019-20.xlsx |
  
</details>

<details>
<summary>API's & Mapping</summary>
  
  
  ## API Keys
For both the [UniDB](https://unidbapi.com/API) and the [Open Weather Geocoding](https://openweathermap.org/api/geocoding-api) API you will need to aquire your own keys. 
  
  In the create_password_file.py file, you will need to insert your API keys and run these first. The Jupyter Notebooks then pull the API keys from the file created. The keys are not to be uploaded to github, and must remain local, for security. 
  
  If you run out of calls during the run of the jupyter notebook, please obtain a new API key, update create_password_file.py, and re-run the sells to extract the API key and get endpoint.  
 

  ## uniDB_demographics.ipynb 
  All API work has been completed inside one notebook: uniDB_demographics.ipynb. 
  
  It is split into the following sections: 
  - API Keys 
  - Imports - of analytical libraries 
  - Degree demographic analysis - the ratio of males to females by course
  - University demographic analysis - percentage of males to females by university 
  - Geocoding - mapping results using the [OW API]((https://openweathermap.org/api/geocoding-api))
  
  Each section has functions defined at the top, and within the body. 
 
  
</details>

## Contributors
[Adelaide Baron](https://github.com/AdelaideBaron?tab=repositories) | 
[Sian Steen](https://github.com/srsteen) | 
[Claire Evans](https://github.com/Aereyelle) 

<br> 

The final project of our [CFGdegree (data)](https://codefirstgirls.com/courses/cfgdegree/). 

