class Staff ():
        firstname=''
        lastname=''
        location=''
        role=''
        def __init__(self,a,b,c,d):
                self.firstname=a
                self.lastname=b
                self.location=c
                self.role=d
        def attributes(self):
                print('First name:%s. Last name:%s. Location:%s. Role:%s.'%(self.firstname,self.lastname,self.location,self.role))
p=Staff('Robert','Young','Edinburgh','Faculty')
p.attributes()



