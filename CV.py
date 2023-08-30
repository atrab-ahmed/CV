class Experience:
    def __init__(self,company,job_title,start_date,end_date):
        self.company=company
        self.job_title=job_title
        self.start_date=start_date
        self.end_date=end_date

    def display_experience(self):
        print(f"{self.company:15}  {self.job_title:10}  {self.start_date:10}  {self.end_date:10}  ")

class Education:
    def __init__(self,degree,institution,completion_date):
        self.degree=degree
        self.institution=institution
        self.completion_date=completion_date

    def display_education(self):
        print(f"{self.degree:15}  {self.institution:11}  {self.completion_date:10}  ")

class Skill:
    def __init__(self,skill,percentage):
        self.skill=skill
        self.percentage=percentage

    def display_skill(self):
        print( f"{self.skill:15}  {self.percentage:10}")

class CV:
    def __init__(self):      
        self.experiences=[]
        self.educations=[]
        self.skills=[]
    def add_experience(self):
        company=input("enter the company name")
        job_title=input("enter the job title ")
        start_date=input("enter the start date ")
        end_date=input("enter the end date ")
        experience=Experience(company,job_title,start_date,end_date)
        self.experiences.append(experience)
        user_choise=input("Do you want to add new experience? (y/n) ")
        if user_choise == 'y' or user_choise=='Y':
            self.add_experience()

    def add_education(self):
        degree=input("enter the degree")
        institution=input("enter the institution ")
        completion_date=input("enter the completion_date ")
        education=Education(degree,institution,completion_date)
        self.educations.append(education)
        user_choise=input("Do you want to add new education? (y/n) ")
        if user_choise == 'y' or user_choise=='Y':
            self.add_education()

    def add_skill(self):
        skill=input("enter the skill")
        percentage=input("enter the percentage ")
        skill=Skill(skill,percentage)
        self.skills.append(skill)
        user_choise=input("Do you want to add new skill? (y/n) ")
        if user_choise == 'y' or user_choise=='Y':
            self.add_skill()

    def display_cv(self):
        if self.experiences != []:
            print("----------------- Experience -----------------")
            print(f"{'Company name':15}  {'Job title':10}  {'Start date':10}  {'End date':10}  ")
            for experience in self.experiences:
                experience.display_experience()
           

        if self.educations != []:
                print("\n----------------- Education -----------------")
                print(f"{'Degree':15}  {'Institution':10}  {'Completion date':10}  ")
                for education in self.educations:
                    education.display_education()

        if self.skills != []:
                print("\n----------------- Skill -----------------")
                print(f"{'Skill':15}  {'Percentage':10}  ")
                for skill in self.skills:
                    skill.display_skill()
        
user_name=input("Enter Your name")          
cv=CV()
user_choise=input("Do you want to add your experience? (y/n)")
if  user_choise=='y' or user_choise=='Y':
    cv.add_experience()

user_choise=input("Do you want to add your education? (y/n)")
if  user_choise=='y' or user_choise=='Y':
    cv.add_education()

user_choise=input("Do you want to add your education? (y/n)")
if  user_choise=='y' or user_choise=='Y':
    cv.add_skill()

print(f"Name: {user_name} ")  
cv.display_cv()




