def readMat(fn='C:/Users/ASUS/Desktop/Elab/Data/gauss10.txt'):
    m = []
    with open(fn) as fp:
        for line in fp:
            m.append(line.strip().split(' '))
    return m

def printMat(m):
    for i in range(len(m)):
        row = ''
        for j in range(len(m[0])):
            row += f'{m[i][j]:^8}'
        print(row)
    print()
#======================= Below ===========================#
class Rowelc:
    def __init__(self, mat):
        self.mat = mat
        self.showmat = mat.copy()
    # def print_matrix(self,data):
    #     for i in range(len(data)):
    #         for j in range(len(data[0])):
    #             print(f'{data[i][j]:^7}', end=' ')
    #         print()
    #     print()
    def print_matrix(self,m):
        for i in range(len(m)):
            row = ''
            for j in range(len(m[0])):
                row += f'{m[i][j]:^8}'
            print(row)
        print()
    def mattoint(self):
        temp = []
        a = []
        for i in range(len(self.mat)): #012
            for j in self.mat[i]:
                a.append(int(j))
            temp.append(a.copy())
            a.clear()
        self.mat = temp
        self.showmat = temp.copy()
            
    #[1, -3, 4, 3]
    #[1, '-5/2', 3, 3]
    def minus(self,row1,row2):
        ans = []
        for i in range(len(row2)):
            if isinstance(row1[i],int) and isinstance(row2[i],int):
                ans.append(int(row1[i]-row2[i]))
            elif isinstance(row1[i],int) and isinstance(row2[i],str):
                s = f'{row1[i]}/1'
                a1,b1 = s.split('/')
                a2,b2 = row2[i].split('/')
                n = ((int(a1)*int(b2))-(int(b1)*int(a2)))
                m = (int(b1)*int(b2))
                #print('1')
                #print(f'{(int(a1)*int(b2))}-{(int(b1)*int(a2))}/{(int(b1)*int(b2))}')
                if n%m == 0:
                    ans.append(int(n/m))
                else:
                    l = self.findlow(n,m)
                    w = int(n)/l
                    p = int(m)/l
                    ans.append(f'{int(w)}/{int(p)}')
            elif isinstance(row1[i],str) and isinstance(row2[i],int):
                s = f'{row2[i]}/1'
                a2,b2 = s.split('/')
                a1,b1 = row1[i].split('/')
                n = ((int(a1)*int(b2))-(int(b1)*int(a2)))
                m = (int(b1)*int(b2))
                #print('2')
                #print(f'{(int(a1)*int(b2))}-{(int(b1)*int(a2))}/{(int(b1)*int(b2))}')
                if n%m == 0:
                    ans.append(int(n/m))
                else:
                    l = self.findlow(n,m)
                    w = int(n)/l
                    p = int(m)/l
                    ans.append(f'{int(w)}/{int(p)}')
            elif isinstance(row1[i],str) and isinstance(row2[i],str):
                a1,b1 = row1[i].split('/')
                a2,b2 = row2[i].split('/')
                n = ((int(a1)*int(b2))-(int(b1)*int(a2)))
                m = (int(b1)*int(b2))
                #print('1')
                #print(f'{(int(a1)*int(b2))}-{(int(b1)*int(a2))}/{(int(b1)*int(b2))}')
                if n%m == 0:
                    ans.append(int(n/m))
                else:
                    l = self.findlow(n,m)
                    w = int(n)/l
                    p = int(m)/l
                    ans.append(f'{int(w)}/{int(p)}')
        #print(f"R{row}->R{row}/({divide})" + ' ' + f"[{', '.join(str(e) for e in ans)}]")
        return(ans)
    
    def findlow(self,a, b):
        if(b == 0):
            return a
        else:
            return self.findlow(b, a % b) #16/6 6/4 4/2 2/0 =>2
    
    def divide(self,row,divide):
        ans = []
        temp = []
        for inmat in row:
            if isinstance(inmat,int):
                temp.append(f'{inmat}/1')
            else: temp.append(inmat)
        #print(temp)
        if isinstance(divide,str):
            for i in temp:
                #print(i)
                a1,b1 = i.split('/')
                a2,b2 = divide.split('/')
                n = (int(a1)*int(b2))
                m = (int(b1)*int(a2))
                if n%m == 0:
                    ans.append(int(n/m))
                else:
                    l = self.findlow(n,m)
                    w = int(n)/l
                    p = int(m)/l
                    ans.append(f'{int(w)}/{int(p)}')
        else:
            for i in temp:
                #print(i)
                a1,b1 = i.split('/')
                #print(a1,b1)
                n = int(a1)
                m = (int(b1)*int(divide))
                if n%m == 0:
                    data = n/m
                    ans.append(int(data))
                else:
                    l = self.findlow(n,m)
                    w = int(n)/l
                    p = int(m)/l
                    ans.append(f'{int(w)}/{int(p)}')
        return ans
    
    def opdivide(self,num,row,divide):
        temp = self.divide(row,divide)
        print(f"R{num+1}->R{num+1}/({divide})"+ ' ' + f"[{', '.join(str(e) for e in temp)}]")
        return temp
    
    def opminus(self,a,b):
        print(f"R{a} ==> R{a} - R{b}")
        
    def opdivide2(self,num,row,divide):
        temp = self.divide(row,divide)
        print(f"R{num+1} ==> R{num+1} / ({divide})")
        return temp
    def mul(self,data1,data2):
        ans = ''
        a1,b1 = data1.split('/')
        a2,b2 = data2.split('/')
        n = int(a1)*int(a2)
        m = int(b1)*int(b2)
        l = self.findlow(n,m)
        w = int(n)/l
        p = int(m)/l
        ans = f'{int(w)}/{int(p)}'
        return ans
    def op(self,data1,data2):
        ans = ''
        a1,b1 = data1.split('/')
        a2,b2 = data2.split('/')
        n = int(a1)*int(b2)+int(b1)*int(a2)
        m = int(b1)*int(b2)
        l = self.findlow(n,m)
        w = int(n)/l
        p = int(m)/l
        ans = f'{int(w)}/{int(p)}'
        return ans
    def chgop(self,data):
        ans = ''
        a1,b1 = data.split('/')
        if int(a1) > 0:
            return f'-{a1}/{b1}'
        else:
            return f'{a1[1:]}/{b1}'
    def findvalue(self,mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if isinstance(mat[i][j] , int):
                    mat[i][j] = f'{mat[i][j]}/{1}'
        text = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ans = {}
        temp = []
        edt = []
        edt1 = []
        for i in range(len(mat)):
            for j in range(len(mat[0])-1):
                if mat[i][j] == '1/1':
                    s = text[j]
                    mat[i][j] = s
                elif mat[i][j] == '0/1':
                    s = ''
                    mat[i][j] = s
                else:
                    s = [mat[i][j],text[j]]
                    mat[i][j] = s
        for i in mat:
            for j in i:
                if j != '':
                    temp.append(j)
            edt1.append(temp.copy())
            temp.clear()
        edt1.reverse() 
        for i in edt1:
            if len(i) == 2:
                ans[f'{i[0]}'] = f'{i[1]}'
            else:
                for j in range(1,len(i)-1):
                    if len(i[j]) == 1 and i[j] in text:
                        i[j] = ans[i[j]]
                    else:
                        if i[j][0] in text:
                            n = ans[i[j][0]] 
                        else:
                            n = i[j][0]
                        e = ans[i[j][1]]
                        m = e
                        s = self.mul(n,m)
                        i[j] = s
                val = '0/1'
                for j in range(1,len(i)-1):
                    s = self.op(i[j],val)
                    val = s
                ans[i[0]] = (self.op(self.chgop(val),i[len(i)-1]))
        ans = dict(reversed(list(ans.items())))
        
        for i in ans:
            s = ans[i]
            if len(s) != 1:
                a,b = s.split('/')
                if b == '1':
                    s = a
            print(f"{i} = {s}")

    def backs(self):
        temp = ['']*len(self.mat) # ['','','']
        print('Result from Gaussian Elimination:')
        self.print_matrix(self.mat)
        print('After Back-Substitution:')
        self.findvalue(self.mat)
    
    def main(self):
        g = 0
        n = 1
        start = True
        check = 0
        m = len(self.mat) #3
        self.mattoint()
        print('Augmented matrix:')
        self.print_matrix(self.mat)
        while g < len(self.mat[0]): #4
            for i in range(len(self.mat[0])-2): #2 - 0 1 
                for j in range(n,m): # [1,3] - [2,3]
                    #print(self.mat[j][i] , f'{j},{i}')
                    if self.mat[j][i] != 0: #[1,0] [2,0] [1,1] [2,1]
                        if start:
                            #print(f'j = {j}')
                            #print(f'n = {n}')
                            self.showmat[0] = self.opdivide(0,self.mat[0],self.mat[0][i])
                            self.showmat[j] = self.opdivide(j,self.mat[j],self.mat[j][i])
                            a = self.showmat[j]
                            b = self.showmat[i]
                            self.mat[j] = self.minus(a,b)
                            self.opminus(j+1,n)
                            self.print_matrix(self.mat)
                            start = False
                        elif j == n :
                            #print('1')
                            #print(f'j = {j}')
                            #print(f'n = {n}')
                            self.showmat[j-1] = self.opdivide(j-1,self.mat[j-1],self.mat[j-1][i])
                            self.showmat[j] = self.opdivide(j,self.mat[j],self.mat[j][i])
                            a = self.showmat[j]
                            b = self.showmat[j-1]
                            self.mat[j] = self.minus(a,b)
                            self.opminus(j+1,j)
                            self.print_matrix(self.mat)
                            check += 1
                        else:
                            #print(f'j = {j}')
                            #print(f'n = {n}')
                            self.showmat[j] = self.opdivide(j,self.mat[j],self.mat[j][i])
                            a = self.showmat[j]
                            b = self.showmat[i]
                            self.mat[j] = self.minus(a,b)
                            self.opminus(j+1,n)
                            self.print_matrix(self.mat)
                g+=1
                n+=1  
        if check != len(self.mat)-2:
                x = len(self.mat)-2
                self.showmat[x] = self.opdivide(x,self.mat[x],self.mat[x][x])
        for i in range(len(self.mat)):
            if self.mat[i][i]!= 1:
                self.mat[i] = self.opdivide2(i,self.mat[i],self.mat[i][i])
        self.print_matrix(self.mat)
        self.backs()
#===Main===#
#name = str(input('Enter filename: '))
mat = readMat()
#mat = readMat(name)
matrix = Rowelc(mat)
matrix.main()