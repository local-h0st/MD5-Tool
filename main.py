import hashlib
import time

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

str_to_search = "'or'1"
# str_to_search = "O"


def how_slow_you_are(f):
    def warppedF(*args,**kwargs):
        t1 = time.time()
        rst = f(*args,**kwargs)
        t2 = time.time()
        print("so slow you ran :",t2-t1)
        return rst
    return warppedF


def str2hexstr(string):
    str_hex = ""
    for char in string:
        str_hex += str(hex(ord(char)))[2:]
    return str_hex


def check(s_short, s_long):
    for i in range(len(s_short)):
        if s_short[i:i + 1] != s_long[i:i + 1]:
            return False
    return True


def generateString(loop_times, alpha_bet):
    length = len(alpha_bet)
    total = pow(length, loop_times)
    for i in range(total):
        s_generated = ""
        for t in range(loop_times):
            pos = (i // pow(length, t)) % length
            s_generated += alpha_bet[pos:pos + 1]
        yield s_generated


@how_slow_you_are
def searchDepth(dep):
    print("searching depth :", depth)
    g = generateString(depth, alphabet)
    for string in g:
        if check(str_to_search_hex, hashlib.md5(string.encode('ascii')).hexdigest()):
            print(string)
            raise RuntimeError("success")


depth = 1
str_to_search_hex = str2hexstr(str_to_search)
while True:
    try:
        searchDepth(depth)
    except RuntimeError as R:
        print(R.args)
        break
    depth += 1

# 太慢了，每一层用时差不多是上一层的30倍，玩毛...
# 本来还想改成OOP的，现在一想还是算了...没有必要
# 三个办法：重构代码进行优化 换成PyPy C++重写

# print(hashlib.md5("ffifdyop".encode('ascii')).hexdigest())
# print(type(hashlib.md5("ffifdyop".encode('ascii')).hexdigest()))  str
