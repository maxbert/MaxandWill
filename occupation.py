import random
JOBS = {}

def opener():
    a = open("occupations.csv", "r")
    b = a.read().split("\n")
    b = b[1:]
    for i in range(len(b) -2):
        if b[i][0] == "\"":
            JOBS[b[i].split("\"")[1]] = float(b[i].split("\"")[2][1:])
        else:    
            JOBS[b[i].split(",")[0]] = float(b[i].split(",")[1])

opener()

def chooser():
    choices = []
    jobs = JOBS.keys()
    for i in range(len(JOBS) -1 ):
        x = jobs[i]
        print x
        for j in range(int(JOBS[jobs[i]] * 10) -1 ):
            choices[j] = jobs[i]
    a = random.randrange(len(choices))
    return choices[a]

print chooser()
