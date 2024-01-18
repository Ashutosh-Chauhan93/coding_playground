

# def sort_using_recursion(L):
#     # !!! Base condition - Do until L.size = 1 
#     # VAL = REMOVE the last element from L 
#     # SORT() L1 ( new list after removal )
#     # INSERT() back the VAL at appropriate location in L1
#         # !!! Base condition - Do until L1.size == 0 OR L1's last element is smaller than VAL , in either case just append the list 
#         # VAL1 = REMOVE the last element L1
#         # INSERT() back the VAL in in L2 ( new list after n-1 L1 )
          # Append back the VAL1
#     pass



def insert(sorted_li: list, last_val: int):
    
    if len(sorted_li) == 0 or sorted_li[-1] <= last_val:
        sorted_li.append(last_val)
        return
    
    popped_last_val = sorted_li.pop()

    insert(sorted_li, last_val)

    sorted_li.append(popped_last_val)



def sort_using_recursion(unsorted_li: list):

    if len(unsorted_li) == 1:
        return unsorted_li

    last_val = unsorted_li.pop()
    sorted_li = sort_using_recursion(unsorted_li)

    insert(sorted_li, last_val)

    return sorted_li


if __name__ == '__main__':
    sorted_list = sort_using_recursion([5, 4, 9, 1, 0, 3])
    print(sorted_list)




