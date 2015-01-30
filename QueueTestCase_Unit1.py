# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently 
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold 
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#
# Your test function should run assertion checks and throw an 
# AssertionError for each of the 5 incorrect Queues. Pressing 
# submit will tell you how many you successfully catch so far.

import random

from queue_test import *

def test():
    ###Your code here.
    q = Queue(3)
    is_empty = q.empty()
    assert (is_empty == True)

    value = q.dequeue()
    assert (value == None)
    
    succeeded = q.enqueue(10)
    assert (succeeded == True)
    is_full = q.full()
    assert (is_full == False)
    value = q.dequeue()
    assert (value == 10)
    succeeded = q.enqueue(20)
    assert (succeeded == True)  
    
    is_empty = q.empty()
    succeeded = q.enqueue(30)
    assert (succeeded == True)
    succeeded = q.enqueue(40)
    assert (succeeded == True)
    succeeded = q.enqueue(50)
    assert (succeeded == False)

    value = q.dequeue()
    assert (value == 20)
    value = q.dequeue()
    assert (value == 30)
    succeeded = q.enqueue(1)
    assert (succeeded == True)
    value = q.dequeue()
    assert (value == 40)
    
    r = Queue(-1)
    is_empty = r.empty()
    assert (is_empty == True)
    r = Queue(0)
    succeeded = r.enqueue(10)
    assert (succeeded == False)

    maxLength=1000
    q3 = Queue(maxLength)

    assert not q3.full(), "Warning 1 - Queue length 1 FULL when empty!"
    assert q3.empty(), "Warning 2 - Queue length 1 empty when empty!"
    assert not (q3.dequeue()), "Warning 3 - Dequeuing an empty queue threw no error"

    for i in range(0, maxLength):
        theElem=(100+i)*(-1)
        print "- Enqueuing element "+repr(theElem)+" at pos. "+repr(i)
        queueOk=q3.enqueue(theElem)
        assert queueOk, "Warning 4 - Returned ERROR when enqueuing "+repr(theElem)+" in pos. "+repr(i)+" - queue length: "+repr(maxLength)+" - msg: "+repr(queueOk)+"!"

    succeeded = q3.enqueue(55)
    assert succeeded == False
    
    for j in range(0, maxLength):
        theElem=(100+j)*(-1)
        print "- Dequeuing element "+repr(theElem)+" at pos. "+repr(i)
        queueVal=q3.dequeue()
        assert queueVal == theElem, "Warning 4 - Returned ERROR when dequeuing "+repr(theElem)+" in pos. "+repr(i)+" - queue length: "+repr(maxLength)+" - msg: "+repr(queueOk)+"!"

    maxLength2 = 17
    theElem = 2
    for i in range(0, maxLength2):
        theElem=theElem*2
        print "- Enqueuing element "+repr(theElem)+" at pos. "+repr(i)
        queueOk=q3.enqueue(theElem)
        assert queueOk, "Warning 4 - Returned ERROR when enqueuing "+repr(theElem)+" in pos. "+repr(i)+" - queue length: "+repr(maxLength)+" - msg: "+repr(queueOk)+"!"

    maxLength2 = 17
    theElem = 2
    for i in range(0, maxLength2):
        #theElem = 0
        theElem=(random.randint(1, 100))
        print "- Enqueuing element "+repr(theElem)+" at pos. "+repr(i)
        queueOk=q3.enqueue(theElem)
        assert queueOk, "Warning 4 - Returned ERROR when enqueuing "+repr(theElem)+" in pos. "+repr(i)+" - queue length: "+repr(maxLength)+" - msg: "+repr(queueOk)+"!"

    q4 = Queue(10)
    maxLength3 = 1000
    theElem = 2

    for i in range(0, 10):
        theElem=theElem+1
        print "- Enqueuing element "+repr(theElem)+" at pos. "+repr(i)
        queueOk=q4.enqueue(theElem)
        assert queueOk, "Warning 4 - Returned ERROR when enqueuing "+repr(theElem)+" in pos. "+repr(i)+" - queue length: "+repr(maxLength)+" - msg: "+repr(queueOk)+"!"

    queueOk=q4.enqueue(theElem)
    assert (queueOk==False), "Warning 4 - Returned ERROR when enqueuing "+repr(theElem)+" in pos. "+repr(i)+" - queue length: "+repr(maxLength)+" - msg: "+repr(queueOk)+"!"

    for i in range(1, maxLength3):
        theElem=1+theElem
        print "- Enqueuing element "+repr(theElem)+" at pos. "+repr(i)
        queueOk=q4.enqueue(theElem)
        assert (queueOk == False), "Warning 4 - Returned ERROR when enqueuing "+repr(theElem)+" in pos. "+repr(i)+" - queue length: "+repr(maxLength)+" - msg: "+repr(queueOk)+"!"    
        
    print "Successful end"
