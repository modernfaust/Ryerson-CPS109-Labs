### -*- coding: utf-8 -*-
##"""
##Created on Fri Sep 20 19:40:59 2019
##
##@author: Edward Lee
##"""
import math
import itertools

def ryerson_letter_grade(pct):
    grade = ''
    if pct in range(0,50):
        grade = 'F'
    if pct in range(50,60):
        grade = 'D'
        if pct in range(50,53):
            grade += '-'
        if pct in range(57,60):
            grade += '+'
    if pct in range(60,70):
        grade = 'C'
        if pct in range(60,63):
            grade += '-'
        if pct in range(67,70):
            grade += '+'
    if pct in range (70,80):
        grade = 'B'
        if pct in range (70,73):
            grade += '-'
        if pct in range (77,80):
            grade += '+'
    if pct in range (80,151):
        grade = 'A'
        if pct in range (80,85):
            grade+= '-'
        if pct in range (90,151):
            grade += '+'
    return grade
        
def is_ascending(items):
    prev_index = 0
    if len(items) > 1:
        list_items = items[::-1]
        for index in range(1,len(list_items)):
            prev_index = list_items[index - 1]
            if list_items[index] >= prev_index:
                return False
    return True

def riffle(items, out = True):
    cut_1 = items[0:(len(items)//2)]
    cut_2 = items[(len(items)//2):len(items)+1]
    faro_shuffle = []
    if out:
        for i in range(len(cut_1)):
            faro_shuffle.append(cut_1[i])
            faro_shuffle.append(cut_2[i])
    else:
        for i in range(len(cut_1)):
            faro_shuffle.append(cut_2[i])
            faro_shuffle.append(cut_1[i])
    return faro_shuffle

def only_odd_digits(n):
    number = n
    for i in range(len(str(n))):
        if number>9:
            if ((number%10)%2)==0:
                return False
        else:
            if number%2==0:
                return False
        number = number//10
    return True

def pyramid_blocks(n, m, h):
    
    total = n*m*1
    calls = h-1
    #calculate top rect
    for i in range(calls):
        n+=1
        m+=1
        total+= n*m*1
    return total

def is_cyclops(n):
    first_n = n
    #CHECK IF 0
    count=0
    while first_n >= 10: 
        count+=1
        first_n = first_n // 10
    
    if n > 9:
        if (count+1)%2 == 0:
            return False
        #GET FIRST NUMBER
        elif first_n == 0 or n%10 == 0:
            return False
        #CHECK IF 0
        count -=1
        return is_cyclops( (n//10)-(first_n*(10**count)))
    else:
        if n == 0:
            return True
        else:
            return False

def domino_cycle(tiles):
    if len(tiles) > 0:
        if tiles[0][0] != tiles[-1][1]:
            return False
        else:
            for pair in range(len(tiles)):
                try:
                    if tiles[pair][1] != tiles[pair+1][0]:
                        return False
                except:
                    pass
    return True

def count_dominators(items):
    if len(items) == 0:
        return 0
    count=1
    dominator = items[-1]
    for i in reversed (items):
        if dominator < i:
            count+=1
            dominator = i
    return count

def taxi_zum_zum(moves):
    x = 0
    y = 0
    go_north = lambda x,y: (x,y+1)
    go_east = lambda x,y: (x+1,y)
    go_south = lambda x,y: (x,y-1)
    go_west = lambda x,y: (x-1,y)
    orientation = {0:go_north,90:go_east,180:go_south,270:go_west}
    angle = 0
    
    for d in moves:
        if d == 'L':
            angle -= 90
        if d == 'R':
            angle += 90
        if d == 'F':
            angle = angle%360
            x,y = orientation[angle](x,y)
    return (x,y)
    
def tukeys_ninthers(items):
    if len(items)==1:
        return items[0]
    done=False
    start = 0
    end = 3
    med_list=items
    while not done:
        try:
            to_add = med_list[start:end]
            if to_add[2] > to_add[1] and to_add[2]>to_add[0]:
                    if to_add[1] > to_add[0]:
                        med_list.append(to_add[1])
                    else:
                        med_list.append(to_add[0])
            if to_add[0] > to_add[1] and to_add[0] > to_add[2]:
                    if to_add[1] > to_add[2]:
                        med_list.append(to_add[1])
                    else:
                        med_list.append(to_add[2])
                    
            if to_add[1] > to_add[0] and to_add[1] > to_add[2]:
                if to_add[0] > to_add[2]:
                    med_list.append(to_add[0])
                else:
                    med_list.append(to_add[2])
            start=end
            end+=3
        except:
            return med_list[-1]
def suppressed_digit_sum(n): 
    n_temp = n
    head = 0
    n_list = []
    digits = 0
    while n_temp !=0:
        digits+=1
        n_temp = n_temp//10
    n_temp = n
    if n//10 == 0:
        return n//10
    for d in range(digits):
        string_n=str(n)
        head = string_n[:d]
        check_n = head+string_n[d+1:]
        if int(check_n) not in n_list:
            n_list.append(int(check_n))
    return sum(n_list)
def scrabble_value(word, multipliers = None):
    word_multiplier = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10 }
    score = 0
    mult = 1
    for letter in range (0,len(word)):
        if multipliers:
            mult = multipliers[letter]
        score += word_multiplier.get(word[letter])*mult
    return score

def is_permutation(items, n): 
    start = 1
    save = set([])
    for value in items:
        if value > n or value < start:
            return False
        save.add(value)
    for count in range (start,n+1):
        if count not in save:
            return False
    return True

def tribonacci(n, start = (1, 1, 1)):
    n_copy = n
    start_copy = start
    element = 0
    if n == 0:
        return start[0]
    if n == 1:
        return start[1]
    if n == 2:
        return start[2]
    while n_copy > 2:
        element = sum(start_copy)
        start_copy = (start_copy[1],start_copy[2],element)
        n_copy -= 1
    return element

def squares_intersect(s1, s2):
    x,y,z = 0,1,2
    bottom_left,top_right = 0,1
    s1_square = ((s1[x],s1[y]),(s1[x]+s1[z],s1[y]+s1[z])) #create s1 square
    s2_square = ((s2[x],s2[y]),(s2[x]+s2[z],s2[y]+s2[z])) #create s2 square
    if s2_square[bottom_left][x] > s1_square[top_right][x]:
        return False
    if s2_square[bottom_left][y] > s1_square[top_right][y]:
        return False
    if s2_square[top_right][x] < s1_square[bottom_left][x]:
        return False
    if s2_square[top_right][y] < s1_square[bottom_left][y]:
        return False
    return True

def sum_of_two_squares(n):
    root = 0
    while root*root < n:
        root+=1
        leftover = n-(root*root)
        if leftover <= 0:
            return None
        leftover_root = math.sqrt(leftover)
        if leftover_root%1 == 0:
            output = (root,int(leftover_root))

            if output[0] > output[1]:
                return output
            else:
                return (int(leftover_root),root)
    else:
        return None

def three_summers(items, goal):
    cut = -1
    while cut< len(items)-1:
        cut+=1
        i = cut+1
        j = len(items)-1
        while i < j:
            total = items[cut]+items[i] + items[j]
            if total == goal:
                return True
            elif total < goal:
                i+=1
            else:
                j-=1
    return False
def first_missing_positive(items):
    storage = set([])
    for number in items:
        storage.add(number)
    
    start = 1
    if 1 < min(storage):
        return 1
    for value in range(0,len(storage)):
        if start in storage:
            start+=1
        else:
            return start


def count_distinct_sums_and_products(items):
    storage = set([])
    if len(items) == 0:
        return 0
    if len(items) == 1:
        return 2
    for number in items:
        for number_2 in range(0,len(items)):
            storage.add(number+items[number_2])
            storage.add(number*items[number_2])
    return len(storage)

def first_preceded_by_smaller(items, k = 1):
    for value in range (k,len(items)):  
        lessers  = 0
        storage = items[:value]
        for to_compare in storage:
            if items[value] > to_compare:
                lessers +=1
            if lessers == k:
                return items[value]
def safe_squares_rooks(n, rooks):
    rows,columns = set(range(0,n)),set(range(0,n))
    x,y = 0,1
    for piece in rooks:
        if piece[x] in columns:
            columns.remove(piece[x])
        if piece[y] in rows:
            rows.remove(piece[y])    
    return len(rows) * len(columns)

def double_until_all_digits(n, giveup = 1000):
    if n == 1234567890:
        return 0
    for i in range(1,giveup+1):
        save = set([])
        n*=2
        string_n = str(n)
        for number in string_n:
            save.add(number)
        if len(save) == 10:
            return i
    return -1
def iterated_remove_pairs(items):
    return_list = items
    for i in range(0,len(items)+1):
        try:
            if items[i] == items[i+1]:
                del return_list[i]
                del return_list[i]
                return_list = iterated_remove_pairs(return_list)
                return return_list
        except:
            return return_list

def safe_squares_knights(n, knights):
    move_set = set([])
    knight_moves = [(2,1),(1,2),(2,-1),(-1,2),(-2,1),(1,-2),(-2,-1),(-1,-2)]
    row,column = 0,1
    for k in knights:
        move_set.add(k)
        for moves in knight_moves:
            move_add = (moves[row]+k[row],moves[column]+k[column])
            if move_add[row] >=0 and move_add[column] >=0 and move_add[row] < n and move_add[column] <n:
                move_set.add(move_add) #uniquely orders the available moves for all the knights
    total = (n**2)-len(move_set) #the dimensions of the board less the # of possible moves less the # of pieces
    if total < 0: #to ensure function returns a positive value
        return 0
    else:
        return total
def reverse_ascending_sublists(items):
    if items == []:
        return items
    ascending_list = [items[0]]
    start_index= 0
    return_list = []
  
    for i in range(1,len(items)+1):
        try:
            if items[i] <= items[start_index]:
                return_list += ascending_list[::-1]
                ascending_list = []
            ascending_list.append(items[i])
            start_index = i
        except:
            return return_list + ascending_list[::-1]
def count_consecutive_summers(n):
    counter = 0
    start = 0
    count_sum = start+counter
    var_ways = 0
    while start != n:
        start+=1
        count_sum = 0
        for i in range(start,n+1):          
            if count_sum > n:
                break
            elif count_sum == n:
                var_ways+=1
                break
            count_sum += i
    if n>0:
        return var_ways+1
    else:
        return var_ways
def expand_intervals(intervals):
    start,end = 0,2
    return_list = []
    work_list = [interval.strip() for interval in intervals.split(',')]
    for interval in work_list:
        if interval.find('-') == -1:
            return_list.append([int(interval)])
        else:
            work_string = interval.partition('-')
            return_list.append((list(range(int(work_string[start]),int(work_string[end])+1))))
    return list(itertools.chain(*return_list)) 
def frequency_sort(elems):
    freq = {}
    for x in elems:
        freq[x] = freq.get(x,0) + 1
    elems.sort(key = lambda x: (-freq[x], x))    
    return elems
def collapse_intervals(items):
    consec = False #must iterate form the n-1 to nth element, because it keeps getting out of range
    if len(items) == 0: #this implementation is honestly disgusting. I need to make this code cleaner
        return ''
    if len(items) == 1:
        return items[0]
    return_string = str(items[0])
    
    for n in range(1,len(items)):
        if n == len(items)-1:
            if items[n-1]+1 == items[n]:
                return_string+='-'+str(items[n])
            else:
                if consec == True:
                    return_string+= '-'+str(items[n-1])
                return_string+=','+str(items[n])
            return return_string
        
        
        if items[n-1]+1 == items[n]:       
            consec = True
        
        elif items[n-1]+1 != items[n]:
            if consec == True:
                return_string+= '-'+str(items[n-1])
                consec = False
                
            return_string+= ','+str(items[n])
            
def count_divisibles_in_range(start, end, n):
    if start%n == 0:
        return end//n - start//n +1
    
    return end//n - start//n