class Node:
    def __init__(self, label):
        self.label = label
        self.map = {}
        self.output = set()
        self.fail = None
    def get_label(self):
        return self.label
 
    def get_children(self):
        return self.map.iteritems()
 
    def add_output(self, word):
        self.output.add(word)
 
    def get_child(self, char):
        return self.map.get(char, None)
 
    def get_or_add_child(self, char):
        p = self.get_child(char)
        if not p:
            p = self.add_child(char)
        return p
 
    def add_child(self, char):
        if self.map.has_key(char):
            return self.map[char]
        else:
            n = Node(char)
            self.map[char] = n
        return n
 
    def get_fail(self):
        return self.fail
 
    def set_fail(self, f):
        self.fail = f
 
    def is_world(self):
        return bool(self.output)
 
    def get_out_put(self):
        return self.output
 
    def __str__(self):
        return 'label: {}, map:{}'.format(self.label, str(self.map))
 
 
class ACAutomaton:
   def __init__(self):
        self.root = Node('-1')
        self.has_built = False
 
   def add_word(self, word):
        p = self.root
        for i in range(len(word)):
            c = word[i]
            p = p.get_or_add_child(c)
            if i == len(word) - 1:
                p.add_output(word)
 
   def build_fail(self):
        # print self.root
        # print self.root.get_children()
        self.root.set_fail(self.root)
        q = []
        chilren = self.root.get_children()
        for k, v in chilren:
            v.set_fail(self.root)
            q.append(v)
 
        while q:
            p = q.pop()
            for k, v in p.get_children():
                q.append(v)
                pf = p.get_fail()
                pfc = pf.get_child(k)
                print 'aaaa', pfc == v, k, pf.label, pfc
                while not pfc and pf != self.root:
                    pf = pf.get_fail()
                    pfc = pf.get_child(k)
                if pfc:
                    v.set_fail(pfc)
                else:
                    v.set_fail(self.root)
 
   def build(self, words):
        for w in words:
            self.add_word(w)
        self.build_fail()
        self.has_built = True
 
   def traverse(self, word):
        p = ac.root
        i = 0
        res = []
        while i < len(word):
            c = word[i]
            pc = p.get_child(c)
            # print pc
            while not pc:
                p = p.get_fail()
                pc = p.get_child(c)
                if p == self.root and not pc:
                    i += 1
                    break
            if pc:
                p = pc
                i += 1
                res.extend(p.get_out_put())
        return res

# words = ['he', 'she', 'his', 'her', 'hers']
words = ['aardva']
ac = ACAutomaton()
ac.build(words)
res = ac.traverse('shherishers')
print res
#['he', 'her', 'she', 'her', 'hers']
res = ac.traverse('shershehishers')
print res
#['she', 'her', 'hers', 'she', 'his', 'she', 'her', 'hers']