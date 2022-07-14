# MD5 Tool
*不知道该起什么名字..就叫了MD5 Tool*

* **[BJDCTF2020]Easy MD5**~~(没错起因就是它)~~

一点也不EZ如果是第一遍做不看writeup的话，Response的Header里面给了hint:
`select * from 'admin' where password=md5($pass,true)`
writeup给的解法是令`$pass=ffifdyop`,
使得最终拼凑出`select * from 'admin' where password='' or'6蒥欓!r,b'`
这样一个怪异但是where条件恒真的sql语句.这个工具从原理层面解决了如何得到目标字符串的问题.

**存在的问题:**\
执行效率低下，每一层depth用时差不多是上一层的30倍，玩毛...\
本来还想改成OOP的，现在一想还是算了...没有必要.\
现在有三个办法：
1. 重构代码进行优化
2. 换成PyPy
3. C++重写

但是我一个也不想采用，等以后要用到这个工具了再来考虑这种问题：）