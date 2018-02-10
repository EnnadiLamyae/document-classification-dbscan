import glob,os,sys

class distance:
    def __init__(self):
        print("Distance module initialized!")

    def sum_weight(self,file):
        file = open(file,'r')
        rows = file.readlines()
        rows_length = len(rows)
        weight = 0.0
        for index in range(rows_length):
            origin = rows[index]
            final = origin.split()
            weight = weight + float(final[1])
        return weight

    def allfiles(self,foldername):
        cwd = os.getcwd()
        folder = foldername + "/"
        os.chdir(folder)
        array = []
        for file in glob.glob("*.txt"):
            array.append(file)
        os.chdir(cwd)
        return array

    def positive(self,score):
        if score < 0 :
            return -score
        else:
            return score
    
    def handle_one(self,total,p,sumweight):
        tot = total + p/float(sumweight)
        return tot
    
    def handle_both(self,total,p,q,sumweight1,sumweight2):
        score = p/float(sumweight1) - q/float(sumweight2)
        points = self.positive(score)
        return total + points
    
    def find_fileid(self,str):
        str2 = str[5:]
        lenstr = len(str2)
        if lenstr == 5:
            return str2[0]
        elif lenstr == 6:
            return str2[:2]
        else:
            return str2[:3]
    
    def matchscore(self,str1,str2):
        file1 = open(str1,'r')
        flines1 = file1.readlines()
        len1 = len(flines1)
        file2 = open(str2,'r')	
        flines2 = file2.readlines()
        len2 = len(flines2)
        words1 = []
        words2 = []
        scores1 = []
        scores2 = []
        for j in range(len1):
			linex1 = flines1[j].split()
			words1.append(linex1[0])
			scores1.append(float(linex1[1]))
        for k in range(len2):
			linex2 = flines2[k].split()
			words2.append(linex2[0])
			scores2.append(float(linex2[1]))
        common = []
        diff1 = []
        diff2 = []
        for g1 in range(len1):
            if words1[g1] in words2:
                common.append(words1[g1])
            else:
                diff1.append(words1[g1])
        for g2 in range(len2):
            if(words2[g2] not in words1):
                diff2.append(words2[g2])
        lenx = len(common)
        lenx1 = len(diff1)
        lenx2 = len(diff2)
        sumweight1 = self.sum_weight(str1)
        sumweight2 = self.sum_weight(str2)
        totx = 0
        for gx1 in range(lenx):
            term1 = common[gx1]
            ind1 = words1.index(term1)
            ind2 = words2.index(term1)
            totx = self.handle_both(totx, scores1[ind1],scores2[ind2],sumweight1,sumweight2)
        for gx2 in range(lenx1):
            term2 = diff1[gx2]
            indx2 = words1.index(term2)
            totx = self.handle_one(totx,scores1[indx2],sumweight1)
        for gx3 in range(lenx2):
            term3 = diff2[gx3]
            indx3 = words2.index(term3)
            totx = self.handle_one(totx,scores2[indx3],sumweight2)
        return totx
    
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

    def main(self):
		oscores = open('scores.txt','w')
		filex = self.allfiles('tf_idf')
		lenn = len(filex)
		total = lenn*lenn
		for g in range(lenn):
			file1 = 'tf_idf/' + filex[g]
			for h in range(lenn):
				prog = (g*lenn+h)/total 
				file2 = 'tf_idf/' + filex[h]
				if file1!=file2:
					scr = self.matchscore(file1,file2)
					fx1 = self.find_fileid(file1)
					fx2 = self.find_fileid(file2)
					oscores.write(fx1)
					oscores.write("	")
					oscores.write(fx2)
					oscores.write("	")
					oscores.write(str(scr))
					oscores.write("\n")	
					self.drawProgressBar(prog)

if __name__ == '__main__':
	dist = distance()
	dist.main()

