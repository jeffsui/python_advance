import io
s = 'hwjewo'
sio = io.StringIO(s)
print(sio)
sio.write('abcdefg')
print(sio.getvalue())
sio.seek(3)
print(sio.tell())
sio.write('123')
print(sio.getvalue())