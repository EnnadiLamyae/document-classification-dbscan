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
    
    def allremove(self):	
		array = self.files('data')						
		length = len(array)
		for k in range(length):
			progr=(k+1)/length
			in1 = 'data/'+array[k];
			out1 = 'ponctuation_removed/'+array[k];		
			self.remove_stop(in1,out1)
			#self.drawProgressBar(progr)
		print("\nAll files done!")

if __name__ == '__main__':
	rp = remove_ponctuations()
	rp.allremove()

            



        
