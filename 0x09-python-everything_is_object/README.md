# 0x09. Python - Everything is object
![](https://i.imgur.com/2nJvHBU.png)

```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```
OK. But what about this?
```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
```
