import os
class FileStream:
    def __init__(self,path,mode):
        self.path = path
        self.mode = mode
        self.file_handler = None

    def __enter__(self):
        print("enter:", self.path,self.mode)
        self.file_handler = open(file=self.path,mode=self.mode)
        return self.file_handler

    def __exit__(self,exc_type,exc_val,exc_tb):
        print("exit:", exc_type, exc_val, exc_tb)
        if self.file_handler:
            self.file_handler.close()
        return True

file_path = os.getcwd()
with FileStream('file.txt','w') as f:
    f.write("test input2")

print(f.closed)