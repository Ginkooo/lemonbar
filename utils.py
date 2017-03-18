import random

def reset_color():
    return '%{F-}%{B-}%{U-}'

def puts(string):
    sys.stdout.write(str(string))

def shift(amount):
    ret = ' ' * amount
    return ret

def color(rgb, ground, string):
    return "%{" + ground + rgb + "}" + string + reset_color()

def align(to, string):
    return "%{" + to + "}" + string

def rand_color():
    nums = '89ABCDEF'
    final_color = '#'
    for i in range(len(nums)):
        rand_num = random.randint(0, len(nums) - 1)
        final_color += nums[rand_num]
    return final_color

