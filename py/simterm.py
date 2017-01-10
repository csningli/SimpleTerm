##!/Users/ln/anaconda3/envs/abodel/bin python

# talkterm.py
# copyright 2016-2017, NiL, csningli@gmail.com

import sys

class SimpleTerm :
    """ 
    SimpleTerm is a terminal-like interface class. One can subclass \'SimpleTerm\' 
    to create a personalized interface. 
    """

    _name_ = 'SimpleTerm'
    _version_ = 'v0.0'
    _date_ = '2016.01.01'
    _comment_ = 'copyright (c)' 

    _width_ = 60

    def __init__(self) :  
        pass

    def test(self) :
        """
        Test TalkTerm.
        """
        print('Here is just a test.')

    def run(self) :
        self.__println('%s %s %s' % (self.__class__._name_, self.__class__._version_, self.__class__._date_)) 
        self.__println('%s' % (self.__class__._comment_))
        self.__printsep()
        
        while True :

            if sys.version_info[0] == 2 :
                op = raw_input('[\033[1m%s\033[0m] >> ' % self.__class__._name_).strip()
            elif sys.version_info[0] == 3 :
                op = input('[' + self.__class__._name_ + '] >> ').strip()
            else :
                break

            if len(op) < 1 :
                continue
                
            ol = op.split(' ')
            cmd = ol[0].strip()
            paras = ol[1:]
            if cmd[0] == '_':
                self.__println('Prefix \'_\' is not allowed in the name of customized command.')
                continue
            elif cmd == 'quit' or cmd == 'q':
                break
            act = getattr(self, cmd, None) 
            if act is not None :
                try :
                    act(*paras)
                except Exception as e:
                    self.__println('Error in execution. %s' % e)
            else :
                self.__println('Command is inavailable.')

        self.__printsep()
        self.__println('Quit.')
    
    def __printsep(self) :
        """
        Print a separator.
        """
        print('-' * int(self.__class__._width_ * 1.2))

    def __println(self, line) :
        """
        Print the argument \'line\'.
        """
        line = line.strip().replace('\n', ' ').replace(' '*5, ' ').replace(' '*4, ' ').replace(' '*2, ' ')
        limit = int(self.__class__._width_ * 1.2) 
        while len(line) > 0 : 
            print('%-100s' % line[:limit].strip())
            line = line[limit:]

    def __printll(self, lead, line) :
        """
        Print the arguments \'lead\' and \'line\'.
        """
        if lead is None :
            lead = 'None'
        if line is None :
            line = lead
        line = line.strip().replace('\n', ' ').replace(' '*5, ' ').replace(' '*4, ' ').replace(' '*2, ' ')
        limit = int(self.__class__._width_) 
        while len(line) > 0 : 
            print('\033[1m %+10s\033[0m\t%-100s' % (lead.strip(), line[:limit].strip()))
            line = line[limit:]
            lead = ''

    def help(self, topic = None) :
        """
        str -> None 
        Print help information of the given topic.
        """
        fa = self.__class__ 
        if topic is not None and len(topic.strip()) > 0:
            fa = getattr(self, topic.strip(), None)
            if fa is None :
                fa = getattr(self, '_' + topic.strip(), None)
            if fa is None :
                fa = getattr(self, topic.strip() + '_', None)
        if fa is not None :
            doc = fa.__doc__
            self.__printll(fa.__name__, doc)
            subtopics = []
            for a in dir(fa) :
                if a[0] != '_' :
                    subtopics.append(a)
            if len(subtopics) > 0 :
                self.__printsep()
                for a in subtopics :
                    if len(a) > 2 and a[:2] != '__' and a[:3] != 'im_':
                        doc = getattr(fa, a).__doc__
                        if doc is not None :
                            self.__printll(a, doc)
        else :
            self.__println('Invalid argument for help.')
        
if __name__ == '__main__' :
    t = SimpleTerm()
    t.run()


