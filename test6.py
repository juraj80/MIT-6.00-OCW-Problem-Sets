def loadSubjects(filename):
    subjDict={}
    inputFile = open(filename)
    for line in inputFile:
        line=line.strip().split(',')
        subject = str(line[0])
        value = int(line[1])
        work = int(line[2])
        subjDict[subject]=(value,work)
    return subjDict

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE] # 0 from tuple
        work = subjects[s][WORK] # 1 from tuple
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

VALUE,WORK = 0,1


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2


def greedyAdvisor(subjects, maxWork,comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...

    resDict={}
    subNames=subjects.keys()
    while len(subNames)>0 and maxWork>=0:
        maxKey=subNames[0]
        maxTup=subjects[maxKey]
        
        for subj in subNames:
            if comparator(subjects[subj],maxTup):
                maxKey = subj


        if subjects[maxKey][WORK]<=maxWork:   
            resDict[maxKey]=subjects[maxKey]
            maxWork=maxWork-subjects[maxKey][WORK]      

        subNames.remove(maxKey)
        
        
        
    print resDict
    print subNames
         


subjects = loadSubjects('subjects1.txt')
#print len(subjects)
#print printSubjects(subjects)
print greedyAdvisor(subjects,15,cmpWork)


  
