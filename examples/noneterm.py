
import sys 
sys.path.append('../py')

import talkterm 

class NoneTerm(talkterm.TalkTerm) :
    _name_ = 'NoneTerm'
    _version_ = 'v0'
    _comment_ = 'copyright (c) Nothing at all'

    def none(self) :
        """
        None -> None
        Just nothing.
        """
        print("Method none of NoneTerm.")


if __name__ == '__main__' :
    n = NoneTerm()
    n.run()
