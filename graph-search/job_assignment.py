# The assignment order of jobs should be decreasing in weight - length
# i.e. The job with the biggest difference (weight - length) should be allocated first
# If two jobs have the same difference, then the job with the higher weight should be first
# The completion time (C) of job i should be the sum of the lengths of all the preceeding jobs plus the length of job i

# Jobs will be in the format [weight, length]
file = open("./jobs.txt","r")
jobs = []

for line in file:
    job = [float(i) for i in line.split()]

    if len(job) > 1:
        jobs.append(job)

def compareDifference(jobA, jobB):
    diffA = jobA[0] - jobA[1]
    diffB = jobB[0] - jobB[1]

    if diffA == diffB:
        return jobB[0] - jobA[0]

    else: 
        return diffB - diffA

def compareRatio(jobA, jobB):
    ratioA = jobA[0] / jobA[1]
    ratioB = jobB[0] / jobB[1]

    if ratioB > ratioA:
        return 1
    elif ratioA > ratioB:
        return -1
    else: 
        return 0

sortedJobs = sorted(jobs, cmp=compareRatio)

completionTime = 0
weightedTotal = 0

for j in sortedJobs:
    completionTime += j[1]
    weightedTotal += completionTime * j[0]

print(weightedTotal)
