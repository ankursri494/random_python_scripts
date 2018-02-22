import libnfs

nfs = libnfs.NFS('nfs://127.0.0.1/data/tmp/')
a = nfs.open('/foo-test', mode='w+')
a.write("Test string")
a.close()
print (nfs.open('/foo-test', mode='r').read())
'''
a=nfs.listdir('/')
for i in a:
    print(a)
'''


