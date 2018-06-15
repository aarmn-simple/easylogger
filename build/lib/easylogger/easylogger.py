from datetime import datetime as _datetime
import os as _os

# log:            [(number in session , number over session , date , time) >>> title : message]
# title:          **************** {your title} ****************
# des:            ---
#                 {your describe}
#                 ---
# session:        ================ Session {session code} ================
#title detail session 0
#


class _degrees:
    def __init__(self,leveln):
        _degrees.leveln=leveln
    def __str__(self):
        if (_degrees.leveln==0):
            return "trace"
        if (_degrees.leveln==1):
            return "debug"
        if (_degrees.leveln==2):
            return "info"
        if (_degrees.leveln==3):
            return "warn"
        if (_degrees.leveln==4):
            return "err"
        if (_degrees.leveln==5):
            return "fatal"
        return ("level"+str(leveln))
class logs:
    def __init__(self,filename="log.txt",logname="",logdet=""):
        logs.filename=filename
        logs.logname=logname
        logs.logdet=logdet
        logs.numlogs=0
        ##########################################
        x=False
        if _os.path.isfile(filename):
            x=True
        if (x==False):
            logs.logfile = open(filename, 'a+',encoding="utf-8")
            if (logs.logname != ""):
                logs.logfile.write("%s%s%s"%("**************** ",logs.logname," ****************\n"))
            if (logs.logdet != ""):
                logs.logfile.write("%s%s%s"%("----------------\n",logs.logdet,"\n----------------\n"))
            logs.logfile.write("%s%s%s"%("================ Session:0[",str(_datetime.now()),"] ================\n"))
            logs.logfile.close()
        else:
            numcurse=0
            logs.logfile = open(filename, 'a+',encoding="utf-8")
            tmp = open(filename, 'r',encoding="utf-8")
            for tmps in tmp:
                if (tmps[0:16]=="================"):
                    numcurse+=1
            tmp.close()
            logs.logfile.write("%s%s%s%s%s%s"%("================ Session:",str(numcurse),"[",str(_datetime.now()),"]"," ================\n"))
            logs.logfile.close()
    def logwrite(self,title="",message="",deg=0):
        degree=_degrees(deg)
        logs.logfile = open(logs.filename,'a+',encoding="utf-8")
        logs.logfile.write("%s%d%s%s%s%s%s%s%s%s%s"%("[(",logs.numlogs,",{",str(_datetime.now()),"}) ",str(degree)," >>> ",title," : \"",message,"\"]\n"))
        logs.logfile.close()
        logs.numlogs+=1

    __all__=["logs","logs.logwrite"]
