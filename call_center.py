class call(object):
    def __init__(self,unique_id,caller_name,phone_number,time_call,reason_call):
        self.unique_id=unique_id
        self.caller_name=caller_name
        self.phone_number=phone_number
        self.time_call=time_call
        self.reason_call=reason_call
    def displayInfo(self):
        print "unique_id:",self.unique_id
        print "caller_name:",self.caller_name
        print "phone_number:",self.phone_number
        print "time_call:",self.time_call
        print "reason_call:",self.reason_call
class CallCenter(object):
    def __init__(self):
        self.calls=[]
        self.queue=len(self.calls)
    def add_call(self,call):
        self.calls.append(call)
        return self
    def remove_call(self):
        self.calls.pop(0)
        return self
    def displayCallInfo(self):
        for i in self.calls:
            print i.caller_name
            print i.phone_number
        print len(self.calls)

#call1=call(1,"Bob",1111111,5,"Hello")
callcenter1=CallCenter().add_call(call(1,"bob",1111111,5,"none")).displayCallInfo()
