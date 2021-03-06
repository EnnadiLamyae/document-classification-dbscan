import nltk,re,pprint
import sys,glob,os
from imp import reload
from nltk.corpus import stopwords

reload(sys)
sys.setdefaultencoding('latin1')

class remove_ponctuations:

    def __init__(self):
        from nltk.corpus import stopwords
        self.swords = set(stopwords.words('english'))
        print(len(self.swords),"stopwords present!")

    def files(self,foldername):	
        cwd = os.getcwd()
        folder = foldername + "/"
        os.chdir(folder)
        array = []
        for file in glob.glob("*.txt"):
            array.append(file)
        os.chdir(cwd)
        print("All filenames extracted!")
        return array
    
    def remove_stop(self,fname,filename):
        rows = open(fname).readlines()
        length = len(rows)
        open_file = open(filename,'w')
        for r in range(length):
            origin = rows[r]
            row = "".join(char for char in origin if char not in ('!','.',':',',','?',';','``','&','-','"','(',')','[',']','0','1','2','3','4','5','6','7','8','9'))
            final = row.split()
            progress = (r+1)/len(rows)
            for s in range(len(final)):
                noword = final[s].lower()
                if noword not in self.swords:
                    open_file.write(noword)
                    open_file.write(" ")

    def drawProgressBar(self,percent, barLen = 30):
	    sys.stdout.write("\r")
	    progress = ""
	    for i in range(barLen):
	        if i<int(barLen * percent):
	            progress += "="
	        else:
	            progress += " "
	    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100)+"\n")
	    sys.stdout.flush()
    
    def allremove(self):	
		array = self.files('data')						
		length = len(array)
		for k in range(length):
			progr=(k+1)/length
			files_in = 'data/'+array[k]
			files_out = 'ponctuation_removed/'+array[k];		
			self.remove_stop(files_in,files_out)
			self.drawProgressBar(progr)
		print("\nAll files done!")

if __name__ == '__main__':
	rp = remove_ponctuations()
	rp.allremove()

            



        
