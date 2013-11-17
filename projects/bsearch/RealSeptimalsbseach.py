# Alston Clark

def bsearch(list,search):




  top = len(list)

  bottom = 0

  
 

  if (top >= search >= bottom):
    return -1 

   
  while ( bottom != top):
    # when bottom == top then you have found the index

    mid = (top + bottom) / 2

    if (search < list[mid]):
      top = mid - 1


    elif ( search > list[mid]):
      bottom = mid + 1


    else:
      return mid

#Cesa Salaam's bsearch

myList = [9,10,12,14]
def bSearch (List, element):
    bottom = 0
    top = len(List)
    middle = 0
    if element < List[len(List)- 1] and element >= List[0]:
        if top != 0:
            while top >= bottom :
                middle = (bottom+top)//2
                if List[middle] == element:
                  # When List[middle] is eual to the element the function stops and middle (the index that the element is in) is brought out of the function.
                    return middle
                elif List[middle] < element:
                    bottom = middle + 1
                else:
                    top = middle - 1
        else:
            return str(-1)+  " Your element was not found in the list,sorry try again." 
    else:
        return str(-1) + " Your element was not found in the list, sorry try again."
# This is my test list: myList = [9,10,12,14]
# This is an example of how you would call the function: print bSearch(myList,9)













