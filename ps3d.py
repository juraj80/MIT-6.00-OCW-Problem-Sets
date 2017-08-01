from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'


def subStringMatchExact(target,key):
    index=find(target,key)
    result=()
    while index>=0:
        result=result+(index,)
        index=find(target,key,index+1)
    return result


key1 ='a'
key2 ='g'
length = len(key1)
        
first = subStringMatchExact(target1,'a')
second = subStringMatchExact(target1,'g')

def constrainedMatchPair(firstMatch,secondMatch, length):
    result = ()
    m = length
    for n in firstMatch:
        for k in secondMatch:
            if n + m + 1 == k:
                result = result + (n,)
    return result
            
#print constrainedMatchPair(first,second,length)



### the following procedure you will use in Problem 3


def subStringMatchExactlyOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    result = ()
    exactMatch = subStringMatchExact(target,key)
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
                     
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        
        print 'possible matches for',key1,key2,'start at',filtered

    print 'exactMatch', exactMatch

    for miss in allAnswers:
        if miss not in exactMatch:
            result = result + (miss,)
        else:
            return None
    return result
        
print subStringMatchExactlyOneSub('atg','abgctagtcadgc')
