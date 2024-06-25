class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
    
    def __enter__(self):
        self.file = open(file=self.filename)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
    
    def getdata(self):
        data = []
        for line in self.file:
            data.append(line.strip(self.sep)[:-1])

        if self.header:
            data = data[1:]
        
        if self.skip_top:
            data = data[self.skip_top:]
        
        if self.skip_bottom:
            data = data[:self.skip_bottom]
            
        return data
    
    def getheader(self):
        self.file.seek(0)
        return self.file.readline().strip().split(self.sep)
