ADD_ACTION = 'add'
SUB_ACTION = 'sub'
MUL_ACTION = 'mul'
DEV_ACTION = 'dev'

print('Hello, World!')

a = input('Enter the first number: ')
b = input('Enter the second number: ')
act = input('Enter the action: ')

def action_func (f_num, s_num, action):
    if (action == ADD_ACTION):
        return f'Result is {float(f_num) + float(s_num)}'
    elif (action == SUB_ACTION):
        return f'Result is {float(f_num) - float(s_num)}'
    elif (action == MUL_ACTION):
        return f'Result is {float(f_num) * float(s_num)}'
    elif (action == DEV_ACTION):
        return f'Result is {float(f_num) / float(s_num)}'
    else:
        return 'Incorrect action!'

print(action_func(a,b,act))