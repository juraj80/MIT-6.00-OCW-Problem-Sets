# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.

    subjDict = {}
    inputFile = open(filename)
    for line in inputFile:
        line = line.strip().split(",")
        subject = str(line[0])
        value = int(line[1])
        work = int(line[2])
        subjDict[subject]=(value,work)
    return subjDict 

    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).




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

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
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
    resDict = {}
    subNames = sorted(subjects.keys())
    while len(subNames)>0 and maxWork>=0:
        maxKey = subNames[0]
        maxTup = subjects[maxKey]
        for name in subNames:
            if comparator(subjects[name],maxTup):
                maxKey = name
        if subjects[maxKey][WORK]<maxWork:     
            resDict[maxKey] = subjects[maxKey] 
            maxWork=maxWork - subjects[maxKey][WORK]
        subNames.remove(maxKey)
    return resDict
    
  

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

   


def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
#    print '\n RUN bruteForceAdvisor with subsetValue ',subsetValue,'subsetWork',subsetWork
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
#            print 'Found a new best',subset[:]
            return subset[:], subsetValue
        else:
            # Keep the current best.
#            print 'Keep the current bestSubset,',bestSubset,'bestSubsetValue ',bestSubsetValue
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
#        print 's', s ,'i',i # tuple from tupleList
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork: 
            subset.append(i)
#            print 'subset.append(i)',subset
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
#            print 'subset ',subset
            subset.pop()
#            print 'subset.pop()'
#            print 'subset ',subset
#            print 'bestSubset ',bestSubset
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime(n):
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    # TODO...
    print 'bruteForceTime'
    for i in range(1,n+1):
        print 'Run Test ',i
        start_time = time.time()
        result = bruteForceAdvisor(subjects, i)
        end_time = time.time()
        total_time = end_time - start_time
        print printSubjects(result)
        print 'Total Time:    ',total_time,'\n'
        if total_time > 5:
            print 'Total Time exceeded 5 seconds'
            return
            



def greedyTime(n):
    print 'Greedy Time'
    for i in range(1,n+1):
        print 'Run Test ',i
        start_time = time.time()
        result = greedyAdvisor(subjects,i,cmpWork)
        end_time = time.time()
        total_time = end_time - start_time
        print printSubjects(result)
        print 'Total Time:    ',total_time,'\n'
        if total_time > 5:
            print 'Total Time exceeded 5 seconds'
            return
    


# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    nameList = subjects.keys()
    tupleList = subjects.values()
    memo = {}
    bestSubset, bestSubsetValue = dpAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0, memo)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def dpAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue, subset, subsetValue, subsetWork, memo):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            memoName = (i, subsetValue + s[VALUE], subsetWork + s[WORK], bestSubsetValue) 
            if not memo.has_key(memoName) :
               memo[memoName]= dpAdvisorHelper(subjects, maxWork, i+1, bestSubset, bestSubsetValue, subset, subsetValue + s[VALUE], subsetWork + s[WORK], memo)
            bestSubset, bestSubsetValue = memo[memoName]
            subset.pop()
        memoName = (i, subsetValue, subsetWork, bestSubsetValue) 
        if not memo.has_key(memoName) :
            memo[memoName] = dpAdvisorHelper(subjects, maxWork, i+1, bestSubset, bestSubsetValue, subset, subsetValue, subsetWork, memo)
        bestSubset, bestSubsetValue = memo[memoName]
        return bestSubset, bestSubsetValue


   
#
# Problem 5: Performance Comparison
#
def dpTime(n):
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...
    print 'dpTime'
    for i in range(1,n+1):
        print 'Run Test ',i
        start_time = time.time()
        result = dpAdvisor(subjects, i)
        end_time = time.time()
        total_time = end_time - start_time
        print printSubjects(result)
        print 'Total Time:    ',total_time,'\n'
        if total_time > 5:
            print 'Total Time exceeded 5 seconds'
            return

subjects = loadSubjects('subjects.txt')
bruteForceTime(10)
#greedyTime(10)
dpTime(10)

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

subjects = loadSubjects('subjects.txt')
bruteForceTime(10)
#greedyTime(10)
dpTime(10)
