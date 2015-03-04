# Allows for abstract methods
from abc import ABCMeta, abstractmethod
import random as rand


class Sorter:
    # This ensures that direct instances of Sorter raise an error
    __metaclass__ = ABCMeta

    def __init__(self, verbose=False):
        self.verbose = verbose

    @abstractmethod
    def sort(self, elements):
        pass


class InsertionSorter(Sorter):
    def __init__(self, verbose=False):
        """Creates a new InsertionSorter

        :param verbose: Whether to print more information
        """
        super(InsertionSorter, self).__init__(verbose)

    def sort(self, elements):
        """Sorts `elements` using insertionsort

        :param: elements, the list that has to be sorted using insertionsort
        :return: the list that was sorted using insertionsort
        :rtype: list
        """
        if self.verbose:
            print("InsertionSort of array: {}".format(elements))

        # Replace this with a useful piece of code that actually sorts elements
        # the test assumes that you return something
        for i in range(len(elements)):
            for j in range(1,len(elements)):
                v=elements[j]
                i=j-1 #now insert v into sorted E[0,j]
                while i>=0 and elements[i]>v:
                    elements[i+1]=elements[i]
                    i=i-1
                    elements[i+1]=v                
        return elements


class QuickSorter(Sorter):
    def __init__(self, verbose=False):
        super(QuickSorter, self).__init__(verbose)

    def sort(self, elements):
        """Sorts `elements` using quicksort

        :param: elements, the list that has to be sorted using quicksort
        :return: the list that was sorted using quicksort
        :rtype: list
        """
        if self.verbose:
            print("QuickSort of array: {}".format(elements))

        # Replace this with a useful piece of code that actually sorts elements
        # the test assumes that you return something
        self.sortQuick(elements, 0, len(elements)-1)
        
        return elements
    
    def sortQuick(self, elements, left, right):
        if right > left:
            i=self.partition(elements, left, right)
            self.sortQuick(elements, left, i-1)
            self.sortQuick(elements, i+1, right)    
    
    def partition(self, list, start, end):
        pivot = list[end]                          # Partition around the last value
        bottom = start-1                           # Start outside the area to be partitioned
        top = end                                  # Ditto

        done = 0
        while not done:                            # Until all elements are partitioned...
            while not done:                        # Until we find an out of place element...
                bottom = bottom+1                  # ... move the bottom up.

                if bottom == top:                  # If we hit the top...
                    done = 1                       # ... we are done.
                    break

                if list[bottom] > pivot:           # Is the bottom out of place?
                    list[top] = list[bottom]       # Then put it at the top...
                    break                          # ... and start searching from the top.

            while not done:                        # Until we find an out of place element...
                top = top-1                        # ... move the top down.
            
                if top == bottom:                  # If we hit the bottom...
                    done = 1                       # ... we are done.
                    break

                if list[top] < pivot:              
                    list[bottom] = list[top]       
                    break                          

        list[top] = pivot                          
        return top  
    

# if you dont want to run the test
# if __name__ == "__main__":
#     pass # put your code here

Ins = InsertionSorter(Sorter)
Quick = QuickSorter(Sorter)
list = [5,1,4,37,3456,1,45,2456,135,3]
list2 = [5,1,4,37,4,1,45,10,135,3]
print(Ins.sort(list))
print(Quick.sort(list2))
