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

#Cesa Salaam
def bSearch (List, element):
    bottom = 0
    top = len(List)
    middle = 0
    if element < List[len(List)- 1] and element >= List[0]:
        if top != 0:
            while top >= bottom :
                middle = (bottom+top)//2
                if List[middle] == element:
                    return middle
                elif List[middle] < element:
                    bottom = middle + 1
                    
                else:
                    top = middle - 1
        else:
            return str(-1)+  " Your element was not found in the list,sorry try again."
    else:
        return str(-1) + " Your element was not found in the list, sorry try again."
#myList = [9,10,12,14]
#print bSearch(myList,9)













