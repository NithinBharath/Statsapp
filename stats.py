def print_grades(grades_input):
    print("[",end=" ")
    for grade in grades_input:
        print(grade,end=" ")
    print("]")


def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total


def grades_average(grades_input):
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average


def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for element in scores:
        variance += (average - element) ** 2
    variance /= len(scores)
    return variance


def grades_std_deviation(variance):
    return variance ** 0.5


print("*"*115)
print("      Welcome to stats app.com, This mini app will easily calculate statistics for your classroom!!")
print("    All you have to do is provide your class's marks/grades as a list and we will do the job for you!")
print("\n")
n = int(input("First we would like to ask how many students you have in your class?:"))
print("\n")

grades = list(map(int,input("Now we would like you to enter the grades of:").split()))
print("\n")
print("\n")

print("Heres your report and statistics of your class!")
print("$"*100)
print("            Grade Report")
print("\n")
print("Grades List:")
print_grades(grades)
print("\n")
print ("Sum of grades:",grades_sum(grades))
print("\n")
print("Average of class:",grades_average(grades))
print("\n")
varc=grades_variance(grades)
print ("Variance:",varc)
print("\n")
print("Standard deviation:",grades_std_deviation(varc))
print("\n")
print("$"*100)