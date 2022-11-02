try:
    print("Hello")
    print(10/"Ten")
except Exception as e:
    print("Handling",e)
else:
    print("Else block")
finally:
    print("cleanup")

output:
Hello
Handling unsupported operand type(s) for /: 'int' and 'str'
cleanup