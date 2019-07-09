#!/usr/bin/env python
# Author: R&D AT

import re
from editconfig import editconfig

mode = 'mandatory'
class Params():
    def __init__(self):
        pass

    def getcats(self):
        global mode
        if mode == 'mandatory':
            f = open('blacklist.list','r').readlines()
        else:
            f = open('whitelist.list','r').readlines()

        catlist = []
        for catname in f:
            catlist.append(catname.strip())
        return catlist

    def default_template(self):
        pass


class Discretionary(Params):
    def __init__(self):
        Params.__init__(self)

    def discretionary(self):
        pass



class Unconfined(Params):
    def __init__(self):
        Params.__init__(self)

    def unconfined(self):
        allowallconf = """# allow all
        logdir /usr/local/squidGuard/log
        acl {
    	    default {
	        pass all
	    }
        }"""
        return allowallconf



class Mandatory(Params):
    def __init__(self):
        self.templates = []
        Params.__init__(self)
    
    def mandatory_dest(self):
        catlist = self.getcats()
        for catname in catlist:
            self.templates.append("""
            dest %s {
                domainlist %s 
            }\n"""%(catname,catname))

        return self.templates
    
    def mandatory_acl(self):
        catlist = self.getcats()
        mycats = ""
        for cat in catlist:
            mycats += "!%s "%cat
        acl_block_all = """acl {
	    default {
	        pass %s all
	        redirect http://www.algerietelecom.dz  
		}
	    }\n"""%mycats
        return acl_block_all
        



def main():
    global mode
    #mode = "unconfined"
    mode = "mandatory"
    if mode == "mandatory":
        man = Mandatory()
        f = open("mandatory.bkf","w")
        f.write("# squidguard mandatory mode config file")
        for temp in  man.mandatory_dest():
            f.write(temp)
        f.write(man.mandatory_acl())
        f.close()
        print "[+] mandatory.bkf created successfuly"
    elif mode == "unconfined":
        unconf = Unconfined()
        f = open("unconfined.bkf","w")
        f.write("# squidguard unconfined mode config file")
        f.write(unconf.unconfined())
        f.close()
        print "[+] unconfined.bkf created successfuly"
if __name__ == "__main__":
    main()

