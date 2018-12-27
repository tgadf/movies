from fsUtils import setDir, isDir, mkDir, setFile, isFile, setSubFile

##############################################################################################################################
# Movie Base Class
##############################################################################################################################
class movieDB():
    def __init__(self, basedir=None, dbdir=None, datadir="data", resultsdir="results"):
        self.dbdir = dbdir
        self.datadir = datadir
        self.resultsdir = resultsdir
        if basedir is None:
            from os import getcwd
            self.basedir = getcwd()
        else:
            self.basedir = basedir

    def setDBDir(self, dbdir):
        self.dbdir=dbdir

    def setDataDir(self, datadir):
        self.datadir=datadir

    def setResultsDir(self, resultsdir):
        self.resultsdir=resultsdir

            
    def getMovieDir(self):
        dirname = self.basedir
        if not isDir(dirname): mkDir(dirname)
        return dirname
    
    def getMovieDBDir(self):
        dirname = setDir(self.getMovieDir(), self.dbdir)
        if not isDir(dirname): mkDir(dirname)
        return dirname

    def getDataDir(self):
        dirname = setDir(self.getMovieDBDir(), self.datadir)
        if not isDir(dirname): mkDir(dirname)
        return dirname

    def getResultsDir(self):
        dirname = setDir(self.getMovieDBDir(), self.resultsdir)
        if not isDir(dirname): mkDir(dirname)
        return dirname