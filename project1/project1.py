"""
Math 590
Project 1
Fall 2018

Partner 1: Walker Harrison (weh18)
Partner 2: Lisa Lebovici (lrl22)
Date: November 2, 2018
"""

# Import time, random, plotting, stats, and numpy.
import time
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy

"""
SelectionSort

This function takes in an unsorted list and returns a sorted list after
implementing SelectionSort.

To implement SelectionSort, the algorithm divides the list into a sorted
and unsorted component, initially treating the whole list as unsorted. On
each iteration, it finds the minimum element of the unsorted component and
places it at the end of the sorted component. The starting index of the
unsorted component then increments by 1 until the whole list is sorted.

INPUTS
A: a non-empty unsorted list

OUTPUTS
A: the sorted list
"""
def SelectionSort(A):
    # if the list is just a single element, it's sorted by default
    # so just return as is
    if len(A) > 1:

        # store the index separating the sorted and unsorted components,
        # starting at the front of the list
        k = 0

        # iterate through the unsorted component
        while k != len(A) - 1:
            # find the location of the minimum element in the unsorted
            # component. Initially, just assume it's the first element
            min_idx = k

            for i in range(k, len(A)):
                if A[i] < A[min_idx]:
                    min_idx = i

            # swap the element at location k (the end of the sorted
            # component) with the minimum element
            if k != min_idx:
                temp = A[k]
                A[k] = A[min_idx]
                A[min_idx] = temp

            # increment k and repeat until list is sorted
            k += 1

    return A


"""
InsertionSort

This function takes in an unsorted list and returns a sorted list after
implementing InsertionSort.

To implement InsertionSort, the algorithm divides the list into a sorted
and unsorted component, initially treating the whole list as unsorted. On
each iteration, it takes the first unsorted element and inserts it into
the sorted component by searching backwards for its position. The remaining
sorted elements are then shifted 1 to the right.

INPUTS
A: a non-empty unsorted list

OUTPUTS
A: the sorted list
"""
def InsertionSort(A):
    # if the list is just a single element, it's sorted by default
    # so just return as is
    if len(A) > 1:
        k = 0

        # store the index separating the sorted and unsorted components,
        # starting at the front of the list
        while k != len(A) - 1:
            # find the index at which (k+1)th element should be sorted
            for i in reversed(range(0, k + 1)):
                if A[k + 1] >= A[i]:
                    insert_idx = i + 1
                    break
            else:
                insert_idx = 0

            # shift the remaining sorted elements one position to the
            # right and insert the (k+1)th element at that position
            if insert_idx != k + 1:
                temp = A[k + 1]

                for i in reversed(range(insert_idx, k + 1)):
                    A[i + 1] = A[i]

                A[insert_idx] = temp

            # increment k and repeat until list is sorted
            k += 1

    return A


"""
BubbleSort

This function takes in an unsorted list and returns a sorted list after
implementing BubbleSort.

To implement BubbleSort, we start at the beginning of the list and 
successively compare adjacent elements. If a larger element comes before 
a smaller element, we swap their positions. After iterating through the 
entire list, we start over from the beginning and repeat the process. 
When we pass through the whole list without making any swaps, the list 
is sorted and the algorithm is over.

INPUTS
A: a non-empty unsorted list

OUTPUTS
A: the sorted list
"""
def BubbleSort(A):
    # only lists with more than 1 element need sorting
    if len(A) > 1:
        # dummy value >0 for swaps to let us enter loop
        swaps = 99
        # initial max element to check; only need to check n-k each time
        max_idx = len(A) - 1

        # iterate until no swaps done
        while swaps > 0:
            # start at beginning of list
            k = 0
            swaps = 0

            # check first n-k elements
            while k < max_idx:

                # swap elements if first is larger
                if A[k] > A[k+1]:
                    temp = A[k+1]
                    A[k+1] = A[k]
                    A[k] = temp

                    # keep count of swaps
                    swaps += 1
                k += 1

            # decrement max index
            max_idx -= 1
    return A


"""
MergeSort

This function takes in an unsorted list and returns a sorted list after
implementing MergeSort.

To implement MergeSort, recursively divide the list into two halves until
the base cases of length 1 or length 2 are reached. To merge halves back
together, iterate through simultaneously; each time, compare the smallest
elements and insert the smaller of the two into the merged list.

INPUTS
A: a non-empty unsorted list

OUTPUTS
A: the sorted list
"""
def MergeSort(A):
    # if the list is just a single element, it's sorted by default
    # so just return as is
    if len(A) == 1:
        return A

    # if the list has two elements, swap if necessary and then return
    elif len(A) == 2:
        if A[0] > A[1]:
            temp = A[0]
            A[0] = A[1]
            A[1] = temp

        return A

    # otherwise, split the list in two halves and recurse
    else:
        n = len(A) // 2
        A1 = MergeSort(A[:n])
        A2 = MergeSort(A[n:])

        # merge the halves back together
        # i = index of the smallest element of A1
        # j = index of the smallest element of A2
        i = j = 0

        # iterate through A1 and A2, comparing their smallest elements.
        # the smaller of the two gets inserted into the merged list.
        # if we've iterated entirely through one of the lists, just insert
        # the remaining elements from the other
        for k in range(len(A)):
            if i == len(A1):
                A[k] = A2[j]
                j += 1

            elif j == len(A2):
                A[k] = A1[i]
                i += 1

            elif A1[i] < A2[j]:
                A[k] = A1[i]
                i += 1

            else:
                A[k] = A2[j]
                j += 1

    return A


"""
QuickSort

This function takes in an unsorted list and two indices, and sorts the
elements between those two indices by implementing QuickSort. To implement
QuickSort, pick an element to serve as a pivot value. Elements greater than
this value are placed to the right  of it, while elements smaller are placed
to the left. Then recursively apply this logic to the two new lists created
on either side of the pivot.

INPUTS
A: a non-empty unsorted list
i: the lower index of the range of elements to be sorted
j: the higher index of the range of elements to be sorted

OUTPUTS
A: the list sorted between indices i and j
"""
def QuickSort(A, i, j):
    # Base case: if the list is a single element, return
    if j-i == 1:
        return A

    else:
        # set indices at limits of incoming list
        left = i
        right = j-1
        # set pivot as rightmost element
        pivot = A[right]

        # iteratively check elements from the outside in
        while (right > left):

            # if value on left is greater than pivot, put it on right
            if A[left] > pivot:

                # if values are adjacent, just use traditional swap
                if right == left + 1:
                    temp = A[left]
                    A[left] = A[right]
                    A[right] = temp
                    right -= 1

                # otherwise we need to make room
                # push element immediately below right to beginning
                else:
                    temp = A[right-1]
                    A[right-1] = A[right]
                    A[right] = A[left]
                    A[left] = temp
                    right -= 1
            else:
                left += 1

        # recurse on two smaller lists created
        if right > 0:
            QuickSort(A, i, right)
        QuickSort(A, right, j)

        return A


"""
isSorted

This function will take in an original unsorted list and a sorted version of
that same list, and return whether the list has been properly sorted.

Note that this function does not change the unsorted list.

INPUTS
unA: the original unsorted list
sA:  the supposedly sorted list

OUTPUTS
returns true or false
"""
def isSorted(unA, sA):
    # Copy the unsorted list.
    temp = unA.copy()
    
    # Use python's sort.
    temp.sort()

    # Check equality.
    return temp == sA

"""
testingSuite

This function will run a number of tests using the input algorithm, check if
the sorting was successful, and print which tests failed (if any).

This is not an exhaustive list of tests by any means, but covers the edge
cases for your sorting algorithms.

INPUTS
alg: a string indicating which alg to test, the options are:
    'SelectionSort'
    'InsertionSort'
    'BubbleSort'
    'MergeSort'
    'QuickSort'

OUTPUTS
Printed statements indicating which tests passed/failed.
"""
def testingSuite(alg):
    # First, we seed the random number generator to ensure reproducibility.
    random.seed(1)

    # List of possible algs.
    algs = ['SelectionSort', 'InsertionSort', \
            'BubbleSort', 'MergeSort', 'QuickSort']

    # Make sure the input is a proper alg to consider.
    if not alg in algs:
        raise Exception('Not an allowed algorithm. Value was: {}'.format(alg))
    
    # Create a list to store all the tests.
    tests = []

    # Create a list to store the test names.
    message = []

    # Test 1: singleton array
    tests.append([1])
    message.append('singleton array')

    # Test 2: repeated elements
    tests.append([1,2,3,4,5,5,4,3,2,1])
    message.append('repeated elements')

    # Test 3: all repeated elements
    tests.append([2,2,2,2,2,2,2,2,2,2])
    message.append('all repeated elements')

    # Test 4: descending order
    tests.append([10,9,8,7,6,5,4,3,2,1])
    message.append('descending order')

    # Test 5: sorted input
    tests.append([1,2,3,4,5,6,7,8,9,10])
    message.append('sorted input')

    # Test 6: negative inputs
    tests.append([-1,-2,-3,-4,-5,-5,-4,-3,-2,-1])
    message.append('negative inputs')

    # Test 7: mixed positive/negative
    tests.append([1,2,3,4,5,-1,-2,-3,-4,-5,0])
    message.append('mixed positive/negative')

    # Test 8: array of size 2^k - 1
    temp = list(range(0,2**6-1))
    random.shuffle(temp)
    tests.append(temp)
    message.append('array of size 2^k - 1')

    # Test 9: random real numbers
    tests.append([random.random() for x in range(0,2**6-1)])
    message.append('random real numbers')

    # Store total number of passed tests.
    passed = 0

    # Loop over the tests.
    for tInd in range(0,len(tests)):
        # Copy the test for sorting.
        temp = tests[tInd].copy()

        # Try to sort, but allow for errors.
        try:
            # Do the sort.
            eval('%s(tests[tInd])' % alg) if alg != 'QuickSort' \
            else eval('%s(tests[tInd],0,len(tests[tInd]))' % alg)
            
            # Check if the test succeeded.
            if isSorted(temp, tests[tInd]):
                print('Test %d Success: %s' % (tInd+1, message[tInd]))
                passed += 1
            else:
                print('Test %d FAILED: %s' % (tInd+1, message[tInd]))

        # Catch any errors.
        except Exception as e:
            print('')
            print('DANGER!')
            print('Test %d threw an error: %s' % (tInd+1, message[tInd]))
            print('Error: ')
            print(e)
            print('')

    # Done testing, print and return.
    print('')
    print('%d/9 Tests Passed' % passed)
    return

"""
measureTime

This function will generate lists of varying lengths and sort them using your
implemented fuctions. It will time these sorting operations, and store the
average time across 30 trials of a particular size n. It will then create plots
of runtime vs n. It will also output the slope of the log-log plots generated
for several of the sorting algorithms.

INPUTS
sortedFlag: set to True to test with only pre-sorted inputs
    (default = False)
numTrials: the number of trials to average timing data across
    (default = 30)

OUTPUTS
A number of generated runtime vs n plot, a log-log plot for several
algorithms, and printed statistics about the slope of the log-log plots.
"""
def measureTime(sortedFlag = False, numTrials = 30):
    # Print whether we are using sorted inputs.
    if sortedFlag:
        print('Timing algorithms using only sorted data.')
    else:
        print('Timing algorithms using random data.')
    print('')
    print('Averaging over %d Trials' % numTrials)
    print('')
    
    # First, we seed the random number generator to ensure consistency.
    random.seed(1)

    # We now define the range of n values to consider.
    if sortedFlag:
        # Need to look at larger n to get a good sense of runtime.
        # Look at n from 20 to 980.
        # Note that 1000 causes issues with recursion depth...
        N = list(range(1,50))
        N = [20*x for x in N]
    else:
        # Look at n from 10 to 500.
        N = list(range(1,51))
        N = [10*x for x in N]

    # Store the different algs to consider.
    algs = ['SelectionSort', 'InsertionSort', \
            'BubbleSort', 'MergeSort', \
            'QuickSort', 'list.sort']

    # Preallocate space to store the runtimes.
    tSelectionSort = N.copy()
    tInsertionSort = N.copy()
    tBubbleSort = N.copy()
    tMergeSort = N.copy()
    tQuickSort = N.copy()
    tPython = N.copy()

    # Create some flags for whether each sorting alg works.
    correctFlag = [True, True, True, True, True, True]

    # Loop over the different sizes.
    for nInd in range(0,len(N)):
        # Get the current value of n to consider.
        n = N[nInd]
        
        # Reset the running sum of the runtimes.
        timing = [0,0,0,0,0,0]
        
        # Loop over the 30 tests.
        for test in range(1,numTrials+1):
            # Create the random list of size n to sort.
            A = list(range(0,n))
            A = [random.random() for x in A]

            if sortedFlag:
                # Pre-sort the list.
                A.sort()

            # Loop over the algs.
            for aI in range(0,len(algs)):
                # Grab the name of the alg.
                alg = algs[aI]

                # Copy the original list for sorting.
                B = A.copy()
                
                # Time the sort.
                t = time.time()
                eval('%s(B)' % alg) if aI!=4 else eval('%s(B,0,len(B))' % alg)
                t = time.time() - t

                # Ensure that your function sorted the list.
                if not isSorted(A,B):
                    correctFlag[aI] = False

                # Add the time to our running sum.
                timing[aI] += t

        # Now that we have completed the numTrials tests, average the times.
        timing = [x/numTrials for x in timing]

        # Store the times for this value of n.
        tSelectionSort[nInd] = timing[0]
        tInsertionSort[nInd] = timing[1]
        tBubbleSort[nInd] = timing[2]
        tMergeSort[nInd] = timing[3]
        tQuickSort[nInd] = timing[4]
        tPython[nInd] = timing[5]

    # If there was an error in one of the plotting algs, report it.
    for aI in range(0,len(algs)-1):
        if not correctFlag[aI]:
            print('%s not implemented properly!!!' % algs[aI])
            print('')

    # Now plot the timing data.
    for aI in range(0,len(algs)):
        # Get the alg.
        alg = algs[aI] if aI != 5 else 'Python'

        # Plot.
        plt.figure()
        eval('plt.plot(N,t%s)' % alg)
        plt.title('%s runtime versus n' % alg)
        plt.xlabel('Input Size n')
        plt.ylabel('Runtime (s)')
        if sortedFlag:
            plt.savefig('%s_sorted.png' % alg, bbox_inches='tight')
        else:
            plt.savefig('%s.png' % alg, bbox_inches='tight')

    # Plot them all together.
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(N,tSelectionSort, label='Selection')
    ax.plot(N,tInsertionSort, label='Insertion')
    ax.plot(N,tBubbleSort, label='Bubble')
    ax.plot(N,tMergeSort, label='Merge')
    ax.plot(N,tQuickSort, label='Quick')
    ax.plot(N,tPython, label='Python')
    legend = ax.legend(loc='upper left')
    plt.title('All sorting runtimes versus n')
    plt.xlabel('Input Size n')
    plt.ylabel('Runtime (s)')
    if sortedFlag:
        plt.savefig('sorting_sorted.png', bbox_inches='tight')
    else:
        plt.savefig('sorting.png', bbox_inches='tight')

    # Now look at the log of the sort times.
    logN = [(numpy.log(x) if x>0 else -6) for x in N]
    logSS = [(numpy.log(x) if x>0 else -6) for x in tSelectionSort]
    logIS = [(numpy.log(x) if x>0 else -6) for x in tInsertionSort]
    logBS = [(numpy.log(x) if x>0 else -6) for x in tBubbleSort]
    logMS = [(numpy.log(x) if x>0 else -6) for x in tMergeSort]
    logQS = [(numpy.log(x) if x>0 else -6) for x in tQuickSort]

    # Linear regression.
    mSS, _, _, _, _ = stats.linregress(logN,logSS)
    mIS, _, _, _, _ = stats.linregress(logN,logIS)
    mBS, _, _, _, _ = stats.linregress(logN,logBS)

    # Plot log-log figure.
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(logN,logSS, label='Selection')
    ax.plot(logN,logIS, label='Insertion')
    ax.plot(logN,logBS, label='Bubble')
    legend = ax.legend(loc='upper left')
    plt.title('Log-Log plot of runtimes versus n')
    plt.xlabel('log(n)')
    plt.ylabel('log(runtime)')
    if sortedFlag:
        plt.savefig('log_sorted.png', bbox_inches='tight')
    else:
        plt.savefig('log.png', bbox_inches='tight')

    # Print the regression info.
    print('Selection Sort log-log Slope (all n): %f' % mSS)
    print('Insertion Sort log-log Slope (all n): %f' % mIS)
    print('Bubble Sort log-log Slope (all n): %f' % mBS)
    print('')

    # Now strip off all n<200...
    logN = logN[19:]
    logSS = logSS[19:]
    logIS = logIS[19:]
    logBS = logBS[19:]
    logMS = logMS[19:]
    logQS = logQS[19:]

    # Linear regression.
    mSS, _, _, _, _ = stats.linregress(logN,logSS)
    mIS, _, _, _, _ = stats.linregress(logN,logIS)
    mBS, _, _, _, _ = stats.linregress(logN,logBS)
    mMS, _, _, _, _ = stats.linregress(logN,logMS)
    mQS, _, _, _, _ = stats.linregress(logN,logQS)

    # Print the regression info.
    print('Selection Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mSS))
    print('Insertion Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mIS))
    print('Bubble Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mBS))
    print('Merge Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mMS))
    print('Quick Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mQS))

    # Close all figures.
    plt.close('all')
