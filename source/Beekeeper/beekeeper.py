def calculateVowel(n):
    jobs = []
    for i in range(n):
        job = input()
        jobs.append(job)
    jobChoosen = jobs[0]
    totalVowel = 0
    for job in jobs:
        num = 0
        num += job.count('aa')
        num += job.count('ee')
        num += job.count('ii')
        num += job.count('oo')
        num += job.count('uu')
        num += job.count('yy')
        if num > totalVowel:
            totalVowel = num 
            jobChoosen = job
    return jobChoosen

while True:
    n = int(input())
    if n == 0:
        break
    else:
        jobChoosen = calculateVowel(n)
        print(jobChoosen)