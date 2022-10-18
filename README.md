# Construction-Management-Firm-Evaluator


### Steps involved in development of this Mini-Project:

### Link for Deployed Flask Web App on my AWS EC2 Instance: http://ec2-34-228-37-227.compute-1.amazonaws.com:8080/



1) This is a python code using selenium for scraping very small data from the source and converted it into a csv file which includes the following data fields.

### Dataset Attributes:

**The Data comprises of top 100 Construction Management for Fee firms in the United States with the following attributes.**

[Data Source]( https://www.enr.com/Toplists/2021-Top-100-CM-for-Fee-Firms-Preview )

``````````````````````````````````````````````````````````````
Rank_2019 : Ranking of the following firm for the year 2019. (0 where no data available)
Rank_2018 : Ranking of the following firm for the year 2018. (0 where no data available)
`````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````
Firm_Type :  Key to Type of Firm: A= Architect; C= Contractor; CM= Construction Management Firm; E= Engineer; EC= Engineer-Contractor; ENV= Environmental 
             Firm. Other Combinations Are Possible.
`````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````
Total_2018_Revenue($ MILL.) :  Revenue of the Firm in the year 2018. (In millions(USD $).
Firm_Name :                    Name of the Firm.
`````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````
Headquarters : Headquater’s Location of Firm.
State :        U.S State code for the respective Firm.
`````````````````````````````````````````````````````````````````
`````````````````````````````````````````````````````````````````
Target : Target = 1 || If it’s worth considering for Investment.
         Target = 0 || If it’s NOT worth Investing in that respective Firm. 
``````````````````````````````````````````````````````````````````````````````

2) After getting the CSV, I have performed some Exploratory Data Analysis on the Dataset and implemented a Machine Learning Model to predict if the Firm is worth Investing and vice versa.

3) I have built an interactive Flask Web Application including two fields I.e, Rank and Revenue using the model developed in the previous step.

4) Deployed the Machine Learning Flask Web Application on a free-tier AWS EC2 instance server.

