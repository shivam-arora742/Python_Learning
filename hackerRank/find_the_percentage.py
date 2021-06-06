if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Output:
    sum=0
    for i in student_marks[query_name]:
        sum+=i
    # to print value upto 2 floating values we use "{:.2f}".format(sum/3)
    print("{:.2f}".format(sum/3))