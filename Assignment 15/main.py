'''
Luis Morales
CSCI 3309
May 7,2023
'''
'''==================================== Import data ===================================='''
# Open file stream and populate table
score_table = [[0.0 for j in range(6)] for i in range(15)]
with open('grades_input.dat', 'r') as f:
    for line in f:
        code, score = line.split()
        row = int(code[0:2])
        col = int(code[2:4])
        score_table[row][col] = float(score)
'''===================================================================================='''

'''================================= Subjects and names =============================== '''
# define the subjects and student names
subjects = ['English', 'Math', 'History', 'Geography', 'Science', 'Programming']
students = ['Carlos Jackson', 'Monte Solaris', 'Jacob Sean', 'Molly Albertson', 'Susan Hutchingson', 'Coby Arnold', 'Maria Blurgson', 'Parker Harris', 'Melroy Peraira', 'Harris Williams', 'Joseph Makenzie', 'Amelia Proctor', 'Eleanor Stuart', 'Sophia Aurora', 'Luna Zuckerman']
'''===================================================================================='''

'''========================== Student Totals =========================================='''
student_totals = [0.0 for i in range(len(students))]
subject_totals = [0.0 for j in range(len(subjects))]
for i in range(len(students)):
    for j in range(len(subjects)):
        student_totals[i] += score_table[i][j]
        subject_totals[j] += score_table[i][j]
'''===================================================================================='''

'''================================= Header Variable =================================='''
hed1 = "Developer: Luis Morales"
hed2 = "School Name: Winston Churchill High School"
hed3 = "Teacher: Mrs. Hazel Meadowglen"
hed4 = "Grade: 10"
hed5 = "Semester/Year: Spring 2023"
'''===================================================================================='''

'''============================= Report Variables ====================================='''
i=0
# Default Number of A's, B's, C's, D's, and F's
As = 0; Bs = 0; Cs = 0; Ds = 0; Fs = 0
# Default Individual Student Subject Grades
engGra = score_table[i][0];matGra = score_table[i][1];hisGra = score_table[i][2];geoGra = score_table[i][3];sciGra = score_table[i][4];proGra = score_table[i][5];
# Default Individual Subject Totals
engTot = 0;matTot = 0;hisTot = 0;geoTot = 0;sciTot = 0;proTot = 0;totTot = 0
# Default Individual Subject Averages
avgEng = 0;avgMat = 0;avgHis = 0;avgGeo = 0;avgSci = 0;avgPro = 0;avgTot = 0;
'''===================================================================================='''

'''===========================================  PRINTOUT  ========================================='''
print("=========================================================================================")
print(hed1.center(90,' '))
print("=========================================================================================")
print(hed2.center(90,' '))
print(hed3.center(90,' '))
print(hed4.center(90,' '))
print(hed5.center(90,' '))
print("=========================================================================================")
print('{0:20}{1:8}{2:8}{3:8}{4:11}{5:9}{6:14}{7:7}{8}'.format('Student Name', 'English', 'Math', 'History', 'Geography', 'Science', 'Programming', 'Total', 'Rank'))
print("-----------------------------------------------------------------------------------------")
'''==================================== Calculate Ranks ===================================='''
# calculate the rank for each student based on their total score
ranks = ['F' for i in range(len(students))]
for i in range(len(students)):
    total = student_totals[i]
    if total >= 540.0:
        ranks[i] = 'A'
        As = As + 1
    elif total >= 480.0:
        ranks[i] = 'B'
        Bs = Bs + 1
    elif total >= 420.0:
        ranks[i] = 'C'
        Cs = Cs + 1
    elif total >= 360.0:
        ranks[i] = 'D'
        Ds = Ds + 1
    elif total < 360.0:
        Fs = Fs + 1
'''=========================================================================================='''
# print rows
for i in range(len(students)):
    student_totals = score_table[i][0] + score_table[i][1] + score_table[i][2] + score_table[i][3] + score_table[i][4] + score_table[i][5]
    print('{0:<18s}{1:>7.2f}{2:>8.2f}{3:>8.2f}{4:>9.2f}{5:>11.2f}{6:>12.2f}{7:>10.2f}{8:>4}'.format(students[i], score_table[i][0], score_table[i][1], score_table[i][2], score_table[i][3], score_table[i][4], score_table[i][5], student_totals, ranks[i]))

'''========================================= Grand Totals ================================================'''
count = 0
while (count < len(students)):
    engTot = 0
    matTot = 0
    hisTot = 0
    geoTot = 0
    sciTot = 0
    proTot = 0
    totTot = 0
    i=0
    while (i < len(students)):
        engTot = engTot + score_table[i][0]
        matTot = matTot + score_table[i][1]
        hisTot = hisTot + score_table[i][2]
        geoTot = geoTot + score_table[i][3]
        sciTot = sciTot + score_table[i][4]
        proTot = proTot + score_table[i][5]
        totTot = engTot + matTot + hisTot + geoTot + sciTot + proTot
        i = i+1
    count = count + 1
print("-----------------------------------------------------------------------------------------")
# Print Grand Total line
granTot = "{0:18}{1:>7.2f}{2:>8.2f}{3:>8.2f}{4:>9.2f}{5:>11.2f}{6:>12.2f}{7:>10.2f}".format("Grand Totals", engTot, matTot, hisTot, geoTot, sciTot, proTot, totTot)
print(granTot)
print("-----------------------------------------------------------------------------------------")
'''============ Calculate Averages ============'''
# Take total per subject and divide by number of students
avgEng = engTot/len(students)
avgMat = matTot/len(students)
avgHis = hisTot/len(students)
avgGeo = geoTot/len(students)
avgSci = sciTot/len(students)
avgPro = proTot/len(students)
avgTot = totTot/len(students)
'''============================================='''
# Print Averages line
avgTotLine = "{0:17}{1:>8.2f}{2:>8.2f}{3:>8.2f}{4:>9.2f}{5:>11.2f}{6:>12.2f}{7:>10.2f}".format ("Averages", avgEng, avgMat, avgHis, avgGeo, avgSci, avgPro, avgTot)
print(avgTotLine)
print("=========================================================================================")
# Print Ranks line
rankCount = "Ranks   A's: {}   B's: {}   C's: {}   D's: {}   F's: {}".format(As,Bs,Cs,Ds,Fs)
print(rankCount.center(90, " "))
print("==================================== End of Report ======================================")