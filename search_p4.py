from P4 import P4, P4Exception
from datetime import datetime

USER_NAME = "YOUR_USER_NAME"

def SearchMyChanges( toSearchFor ):
    p4 = P4()                     
    try:
        p4.connect()
    except P4Exception:
        print("Something went wrong in P4 connection. The errors are: ")
        for e in p4.errors:
            print(e)       
        return    

    if p4.connected():
        
        out = p4.run( "changes", "-u", USER_NAME, "-l" ) 
        
        if p4.errors:
            print(p4.errors)
        if p4.warnings:
            print(p4.warnings)

        matches = False
        for cl in out:
            if( cl["desc"].find(toSearchFor) != -1 ):
                if matches == False:
                    print("** MATCHING CHANGELISTS **")
                    matches = True
                print("CL " + cl["change"])
                print(datetime.utcfromtimestamp(int(cl["time"])).strftime('%Y-%m-%d'))
                print(cl["desc"])    

        if matches == False:
            print("No matching CLs found")
            
        p4.disconnect()    

toSearchFor = input("Search your P4 submission history for: ")
SearchMyChanges( toSearchFor )
