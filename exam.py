# def test_exc_return():
#     try:
#         print('in try....')
#         raise KeyError()
#         return 1
#
#     except KeyError:
#         print('key error')
#         return 2
#
#     else:
#         return 3
#
#     finally:
#         print('finally')
#
#
# if __name__ == "__main__":
#     a = test_exc_return()
#     print(a)
a =['foo','aa','baz','qux','corge']
print(len(a))
while a:
    if len(a) < 5:
        break
    print(a.pop())
# print('done')
# a.pop(0)
# a.pop(1)
# print(a.pop(0))
# print(len(a))