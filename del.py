# %%
def perfect_number(n: int)  -> bool:
    sum_ = 0
    for i in range(1, n):
        # print(i+1)
        if n % (i) == 0:
            sum_ += i
            # print(i+1)
            
    # print(sum_)
    return sum_ == n
# %%
iteration = 2
fibonace = ( '0 1' if iteration > 1 else '0' if iteration == 1 else ['err'] )
iteration -=2
numCur = 0
numNext = 1
while iteration > 0:
    sum = numCur + numNext
    numCur = numNext
    numNext = sum 
    fibonace += ' ' + str(sum)
    iteration -= 1

print (fibonace)

# %%
number = input('Enter numbers separating by comma: ').split(',')

def get_square(ls: list) -> list:
    square = []
    for i in ls:
        square.append(float(i)**2)
    return square


try:
    square = get_square(number)
except Exception as e:
    print(e)


def test_square():
    assert get_square([1, 2, 3]) == [1, 4, 9]
    assert get_square([1.2, 2, 3]) == [1.44, 4, 9]

# %%
def filter_list(ls: list) -> list:
    only_numbers = []
    for i in ls:
        if not isinstance(i, str):
            only_numbers.append(i)
    return only_numbers

def filter_list(ls: list) -> list:
    return [i for i in ls if not isinstance(i, str)]

# def filter_list(ls: list) -> list:
#     only_numbers = []
#     for i in ls:
#         if i.isnumeric():
#             only_numbers.append(i)
#     return only_numbers

def test():
    assert filter_list([1,2,'a','b']) == [1,2]
    assert filter_list([1,'a','b', 0, 15]) == [1, 0, 15]
    assert filter_list([1,2,'asd','1', '123', 123]) == [1, 2, 123]

test()
# %%
def count_odd_in_range(a, b):
    return (b + 1 - a) // 2
    # return [i for i in range(a, b+1) if i % 2 == 0]

def calc_salary(x: list) -> float:
    return sum([i for i in x[1:-1]]) / len(x[1:-1])

# task 3
def get_duplicate(x: list):
    res = [i for i in x if x.count(i) > 1]
    return res[0] if len(res) > 0 else None

# task 4
def get_common(a: list, b: list):
    return len(set(a) & set(b))

# %%
# key = find
# task 5 ►
def rle(s: str) -> str:
    uniques = ''
    [uniques:= uniques+i for i in s if i not in uniques ]
    # print(uniques)
    counts = [s.count(i) for i in uniques]
    res = ''
    e = 0
    for i in uniques:
        res += i
        res += str(counts[e])
        e += 1

    return res
    
# pop прореживание
# task 5-1 ►
def rle2(s: str) -> str:
    uniques = set(s)
    uniques = list(uniques)
    uniques.sort(key=s.find)
    counts = [s.count(i) for i in uniques]
    res = ''
    for a, b in zip(uniques, counts):
        res += (a+str(b))

    return res

def rle3(s: str) -> str:
    uniques = set(s)
    uniques = list(uniques)
    uniques.sort(key=s.find)
    res = ''
    for a in uniques:D
        res += (a+str(s.count(a)))

    return res
# %%
# [i if (i % 2 == 0) else c.append(i) for i in x]

x = [int(i)  for i in '1 2 4 5 3 5 6'.split()]

c = []

for i in x:
    if i % 2 == 0:
        c.append(i)
    else:
        c.insert(-1,i)

print(c)
# %%
x = 'lksdfeiIHH'

c = [i.islower() for i in x]
low = (sum(c)/len(c))
upper = 1 - low

print(f'Малих {low*100:.2f}%, великих {upper*100:.2f}%')

# %%
arr = [1,2,5,10]
trg = 3

def func(trg, arr):
    if trg in arr:
        return arr.index(trg)
    elif trg > arr[-1]:
        return len(arr)
    else:
        return [i>trg for i in arr].index(1)




# %%

def check(candidate:str) -> bool:
    '''
    check if it has a permutation which is a palindrome
    '''
    x = set(candidate)
    cumcount = 0
    for i in x:
        cumcount += candidate.count(i) % 2
    return cumcount <=1

check('civci')
# %%

def check(candidate:str) -> bool:
    '''
    check if it has a permutation which is a palindrome
    '''
    return sum([candidate.count(i) % 2 for i in set(candidate)]) <=1
    

check('civci')

def test_check():
    assert check('civic') == True 
    assert check('civicc') == False 
    assert check('civci') == True 
    assert check('c') == True
    assert check('cc') == True

test_check()

# %%
x = 'aassbbc'

c= x[0]
[c == (c:=i) for i in x[1:]][::2]