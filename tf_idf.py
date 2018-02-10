import math
import glob, os, sys

class tf_idf:

    def __init__(self):
        print("Initialized!")

    def allfiles(self,foldername):
        cwd = os.getcwd()
        folder = foldername + "/"
        os.chdir(folder)
        array = []
        for file in glob.glob("*.txt"):
            array.append(file)
        os.chdir(cwd)
        return array

    def extract_text(self,filex):
        file = open(filex,'r')
        text = file.read()
        file.close()
        return text
    
    def find_count(self,text,word):
        length = len(text)
        frequency = 0
        for j in range(length):
            if text[j] == word:
                frequency = frequency + 1
        return frequency
    
    def find_tf(self,text,word):
        length = len(text)
        frequency = 0
        for j in range(length):
            if text[j] == word:
                frequency = frequency + 1
        tf = math.log(1+frequency)
        return tf
    
    def find_idf(self,infile,word):
        array = self.allfiles('ponctuation_removed')
        length = len(array)
        wc = 0
        for i in range(length):
            fname = "ponctuation_removed/" + array[i]
            words1 = self.extract_text(fname)
            words2 = words1.split()
            if word in words2:
                wc = wc + 1
        fact = length/float(1+wc)
        idf = math.log(fact,10)
        return idf
    
    def find_tfidf(self,infile,text,word):
		tf = self.find_tf(text,word)		
		idf = self.find_idf(infile,word)
		tfidf = tf*idf				
		return tfidf
    
    def cluster_to_characteristic(self,infile,outfile):
        outx = open(outfile,'w')
        texta = self.extract_text(infile)
        textw = texta.split()
        lent = len(textw)
        textu = []
        for i in range(lent):
            if textw[i] not in textu:
                textu.append(textw[i])
        lentu = len(textu)
        for i2 in range(lentu):
            yy = self.find_tfidf(infile,textw,textu[i2])
            tff1 = self.find_count(textw,textu[i2])
            outx.write(textu[i2])
            outx.write("	")
            outx.write(str(yy))
            outx.write("\n")
    
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

    def allconvert(self):
        array = self.allfiles('ponctuation_removed')
        length = len(array)
        print"Got",length,"files!"
        for k in range(length):
            prog=(k+1)/length
            file_in = 'ponctuation_removed/'+array[k]
            file_out = 'tf_idf/'+array[k]
            self.cluster_to_characteristic(file_in,file_out)
            self.drawProgressBar(prog)
    
if __name__ == '__main__':
    tf=tf_idf()
    tf.allconvert()

