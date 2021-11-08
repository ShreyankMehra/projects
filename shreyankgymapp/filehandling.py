import json
class fh:
    def open_user(self):
        con={}
        fp=open('user.json','r')
        try:
            con = json.loads(fp.read())
        except:
            print("")
        return con

    def upd_user(self,dict1):

        dump_data = json.dumps(dict1)
        fp = open('user.json', 'w+')

        fp.write(dump_data)
        fp.close()

    def open_members(self):
        con={}
        fp=open('members.json','r')
        try:
            con = json.loads(fp.read())
        except:
            print("")
        return con

    def upd_members(self,dict1):

        dump_data = json.dumps(dict1)
        fp = open('members.json', 'w+')

        fp.write(dump_data)
        fp.close()




    def open_bmi(self):
        con = {}
        fp = open('bmi.json', 'r')
        try:
            con = json.loads(fp.read())
        except:
            print("")
        return fh.convertdictkeytotuple(con)

    def upd_bmi(self,dict1):
        a = fh.convertdictkeytostr(dict1)
        dump_data = json.dumps(a)
        fp = open('bmi.json', 'w+')

        fp.write(dump_data)
        fp.close()
    @staticmethod
    def converttotuple(s):
        t = []
        for i in s.split(','):
            st = ''
            for j in i:
                if j not in ["(", ")"]:
                    st += j
            t.append(float(st))
        return tuple(t)

    @staticmethod
    def convertdictkeytostr(di):
        l = []
        for i in di:
            l.append((i, di[i]))
        di = {}
        for i, j in l:
            di[str(i)] = j
        return di

    @staticmethod
    def convertdictkeytotuple(di):
        l = []
        for i in di:
            l.append(((i), di[i]))
        di = {}
        for i, j in l:
            di[fh.converttotuple(i)] = j
        return di


