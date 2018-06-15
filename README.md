# easylogger
easylogger is the most simple way to write your logs . just make a **logs** object , we can handle session counting and count logs and 6 level of importance for logs (0,5).

## logs
the main method just write easylogger.logs("your file dest (default is ./log.txt)","your log name","your log details")
for example
a=easylogger.logs("./click.log","clicks log","here we have log of clicks from 2012")
## logwrite
ogger.logs.logwrite is the only function have three parameters title ,message and degree (0,5)
for example
a.logwrite("file IO","all of sdcard files are corrupted")
## degree
0>>trace
1>>debug
2>>info
3>>warn
4>>err
5>>fatal

## Sample Code

    import easylogger

    a=easylogger.logs("./xapp.log","X app log","all of things happening in X app is written here")
    a.logwrite("mouse move","127*148 RU",0)
    a.logwrite("hello","127*148 RU",0)

    a=None #simulating when app is closed

    a=easylogger.logs("./xapp.log","X app log","all of things happening in X app is written here")
    a.logwrite("mouse move","127*148 RU",0)
    a.logwrite("hello","127*148 RU",0)

## Sample Output
**xapp.log:**

    **************** X app log ****************
    ----------------
    all of things happening in X app is written here
    ----------------
    ================ Session:0[2018-06-15 04:00:05.612757] ================
    [(0,{2018-06-15 04:00:05.612954}) trace >>> mouse move : "127*148 RU"]
    [(1,{2018-06-15 04:00:05.613090}) trace >>> hello : "127*148 RU"]
    ================ Session:1[2018-06-15 04:00:05.613332] ================
    [(0,{2018-06-15 04:00:05.613445}) trace >>> mouse move : "127*148 RU"]
    [(1,{2018-06-15 04:00:05.613564}) trace >>> hello : "127*148 RU"]
