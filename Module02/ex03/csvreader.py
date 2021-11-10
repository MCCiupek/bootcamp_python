import readline
import sys
import errno
import os

class CsvReader(object):

    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.f = None

    def __enter__(self):
        try:
            self.f = open(self.filename, 'r+', newline='\n')
            lines = [line.split(self.sep) for line in self.f.readlines()]
            self.f.seek(0)
            if any(len(line) != len(lines[0]) for line in lines):
                return None
            return self
        except IOError as err:
            sys.stderr.write("I/O error({0}): {1}".format(err.errno, err.strerror))
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f:
            self.f.close()
    
    def getdata(self):
        """
        Retrieves the data/records from skip_top to skip bottom.
        Returns:
        nested list (list(list, list, ...)) representing the data.
        """
        lines = self.f.readlines()[self.skip_top:]
        if self.skip_bottom > 0:
            lines = lines[:-self.skip_bottom]
        data = [line.split(self.sep) for line in lines]
        self.f.seek(0)
        return data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        header = self.f.readline().split(self.sep)
        self.f.seek(0)
        return header
