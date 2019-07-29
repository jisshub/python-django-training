def student_grade(grade):
    val = 0
    for each_gr in grade:
        if each_gr >= 38:
            while (each_gr + val) % 5 is not 0:
                val += 1
            final_grade = each_gr + val
            print(final_grade)
        else:
            print(each_gr)


student_grade([73, 64, 33, 52])
