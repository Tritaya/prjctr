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
    square  = get_square(number)
except Exception as e:
    print(e)

def test_square():
    assert square([1, 2, 3]) == [1, 4, 9]

