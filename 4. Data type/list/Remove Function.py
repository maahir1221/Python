alist=[123, 'xyz', 'Heyram', 'abc']
print("Alist:", alist.pop())
print(alist)

print("Blist:",alist.pop(2))
print(alist)

alist=[123, 'xyz', 'Heyram', 'abc', 'xyz']
alist.remove('xyz')
print(alist)