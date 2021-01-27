# The assignment order of jobs should be decreasing in weight - length
# i.e. The job with the biggest difference (weight - length) should be allocated first
# If two jobs have the same difference, then the job with the higher weight should be first
# The completion time (C) of job i should be the sum of the lengths of all the preceeding jobs plus the length of job i

# Jobs will be in the format [weight, length]
jobs = [[5,3],[8,0],[6,4], [10,2]]

def compare(jobA, jobB):
    diffA = jobA[0] - jobA[1]
    diffB = jobB[0] - jobB[1]

    if diffA == diffB:
        return jobB[0] - jobA[0]

    else: 
        return diffB - diffA

sortedJobs = sorted(jobs, cmp=compare)

completionTime = 0
weightedTotal = 0

for j in sortedJobs:
    completionTime += j[1]
    weightedTotal += completionTime * j[0]
