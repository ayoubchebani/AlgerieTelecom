#!/usr/bin/env python
# Author: R&D AT

import re
from editconfig import editconfig

class Params():
    def __init__(self):
        pass

    def getcats(self):
        f = open("cat.list",'r').readlines()
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
    #mode = "unconfined"
    mode = "mandatory"
    if mode == "mandatory":
        man = Mandatory()
        f = open("mandatory.conf","w")
        for temp in  man.mandatory_dest():
            f.write(temp)
        f.write(man.mandatory_acl())
        f.close()
        print "[+] mandatory.conf created successfuly"
    elif mode == "unconfined":
        unconf = Unconfined()
        f = open("unconfined.conf","w")
        f.write(unconf.unconfined())
        f.close()
        print "[+] unconfined.conf created successfuly"
if __name__ == "__main__":
    main()

