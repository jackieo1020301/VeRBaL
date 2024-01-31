#import verbal

def DataToMessage(InputMessage):
    try:
#       modelconn = verbalmodel.connect("")
        print("connect to model")
    except:
        print("UnderConstruction")
        exit(-1)
    ret = "returned message" + InputMessage
    return ret

def DiffInputs(inputmessage):
    print("Input parsed")
    ret = "parsed input" + inputmessage
    return ret

