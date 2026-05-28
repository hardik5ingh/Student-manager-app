import json
import os

SCRIPT_DIR=os.path.dirname(os.path.abspath(__file__))
dataFile = os.path.join(SCRIPT_DIR,"students.json")

if os.path.exists(dataFile):
    with open(dataFile, "r", encoding="utf-8") as file:
        student = json.load(file)
else:
    student = {}


while True:
    print("-----Student manager app-----")
    print("1. Add student ")
    print("2. View student")
    print("3. Check result")
    print("4. Delete student")
    print("5. exit")
    
    choice=input("Enter your choice: ")
    
    if choice=="1":
        name=input("Enter your name: ")
        rollNo=int(input("Enter your Roll number: "))
        
        subjectsMarks={}
        while True:
            subjectName=input("Enter subject name: or(type done to finish)")
            if subjectName=="done":
                break
            if not subjectName.strip():
                print("Cannot be empty")
                continue
            
            marks=int(input(f"Enter {subjectName} marks"))
            subjectsMarks[subjectName]=marks
            
        student[name]={
            "Roll no":rollNo,
            "Marks":subjectsMarks
        }
        
        with open(dataFile,"w", encoding="utf-8") as file:
            json.dump(student,file,indent=4)
        print(name,"Successfully addeed")
        
    elif choice == "2":
        if not student:
            print("no student found")
        else:
            for name, info in student.items():
                print(f"\nName: {name}")
                print(f"Roll No: {info['Roll no']}")
                print("Marks:")
                for subject, score in info["Marks"].items():
                    print(f"  {subject}: {score}")

        
    elif choice=="3":
        name=input("Enter student name: ")
        if name in student:
            info=student[name]
            if not info["Marks"]:
                print("No marks are recorded")
            else:
                scores=info["Marks"].values()
                totalSum=sum(scores)
                totalSubjects=len(scores)
                percentage=((totalSum/(totalSubjects*100))*100)
                print(f"Total: {totalSum}/{totalSubjects*100}")
                print(f"Percentage: {percentage:.2F}%")
        else:
            print("Student not found")
            
            
    elif choice=="4":
        name=input("Enter the student name you want to delete")
        if name in student:
            del student[name]
            with open(dataFile,"w",encoding="utf-8") as file:
                json.dump(student,file,indent=4)
            print(name,"student name deleted")
        else:
            print("Student not found")
            
    elif choice=="5":
        print("exiting...")
        break
    
    else:
        print("incorrect choice")