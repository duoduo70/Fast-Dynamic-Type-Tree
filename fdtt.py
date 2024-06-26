class Type:
        def __init__(self, type_ = None, CLASS = None):
                self.type_ = type_
                self.CLASS = CLASS
                self.from_ = []
                self.to = []
                self.subtypes = []

class Universe:
        __types = {None : Type()}
        __iters = {}
        __constructors = []
        __reverse_construct_type_funcs = []
        __reverse_construct_arrow_funcs = []

        def add_type(self, name, type_ = None, CLASS = None):
                self.__types[name] = Type(type_, CLASS)
                self.__types[type_].subtypes.append(name)
                return self

        def add_arrow(self, from_type, to_type, arrow_name = None):
                if from_type not in self.__types.keys():
                        self.__types[from_type] = Type()
                if to_type not in self.__types.keys():
                        self.__types[to_type] = Type()
                
                self.__types[from_type].to.append((to_type, arrow_name))
                self.__types[to_type].from_.append((from_type, arrow_name))
                return self

        def add_iter(self, itername, iterfunc):
                self.__iters[itername] = iterfunc
                return self
        
        def add_revc_type_func(self, revc_type_func):
                self.__reverse_construct_type_funcs.append(revc_type_func)
                return self
        
        def add_revc_arrow_func(self, revc_arrow_func):
                self.__reverse_construct_arrow_funcs.append(revc_arrow_func)
                return self

        def use_iter(self, itername, *args):
                self.__iters[itername](self, *args)
                return self

        def add_ctor(self, constructorfunc):
                self.__constructors.append(constructorfunc)
                return self
        
        def set_type(self, type_, type_type):
                self.__types[type_].type_ = type_type
                return self
        
        def set_CLASS(self, type_, CLASS):
                self.__types[type_].type_ = CLASS
                return self

        def refresh(self):
                for f in self.__constructors:
                        f(self)
                return self
        
        def get_subtypes(self, typename):
                return self.__types[typename].subtypes
        
        def get_CLASS(self, typename):
                return self.__types[typename].CLASS
        
        def track(self, arrowname, typename):
                for (to, to_arrowname) in self.__types[typename].to:
                        if to_arrowname == arrowname:
                                return to

                for f in self.__reverse_construct_type_funcs:
                        if f(self, typename) == True:
                                break
                
                for f in self.__reverse_construct_arrow_funcs:
                        if f(self, arrowname) == True:
                                break
                
                self.refresh()

                for (to, to_arrowname) in self.__types[typename].to:
                        if to_arrowname == arrowname:
                                return to

                raise "Can not find `" + arrowname + "` with `" + typename + "`"

        def __str__(self):
                types_str = ""
                arrows_str = ""
                for tname, t in self.__types.items():
                        types_str += ('        ' +
                                      str(tname) +
                                      ': ' + str(t.type_) +
                                      ' = ' + str(t.CLASS) +
                                      '\n')
                        for (from_, arrowname) in t.from_:
                                arrows_str += ('        ' + 
                                             str(arrowname) + ': ' +
                                             str(from_) + ' -> ' + str(tname) + 
                                             '\n')
                return f'Types:\n{types_str}arrows:\n{arrows_str}'
