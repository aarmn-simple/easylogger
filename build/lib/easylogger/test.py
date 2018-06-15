if (__name__=='__main__'):

    import logger

    a=logger.logs("./xapp.log","X app log","all of things happening in X app is written here")
    a.logwrite("mouse move","127*148 RU",0)
    a.logwrite("hello","127*148 RU",0)

    a=None #simulating when app is closed

    a=logger.logs("./xapp.log","X app log","all of things happening in X app is written here")
    a.logwrite("mouse move","127*148 RU",0)
    a.logwrite("hello","127*148 RU",0)

else:
    return "Its not a lib run it directly"
