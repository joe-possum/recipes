import sys
import getopt

name_prefix = 'net-weight'

def add_prefix(p,l) :
    rc = []
    for i in l :
        rc.append(p+i)
    return rc

vessels = add_prefix('saucepan-',['1Qt','1Qt5','2Qt5']) + add_prefix('pot-',['3Qt','6Qt','10Qt']) + add_prefix('Lodge-',['6in','8in','10in']) + ['InstantPot']

weights = {
  'saucepan-1Qt':13.75,
  'saucepan-1Qt5':20.89,
  'saucepan-2Qt5':38.29,
  'pot-3Qt':22.46,
  'pot-6Qt':46.89,
  'pot-10Qt':56.5,
  'Lodge-6in':31.69,
  'Lodge-8in':48.65,
  'Lodge-10in':98.69,
  'InstantPot':27.7
}

def exit_list(dictionary=False) :
    if dictionary :
        body = []
    for vessel in vessels :
        if dictionary :
            weight = weights.get(vessel)
            if None == weight : weight = 0.0
            body.append('\'%s\':%.2f'%(vessel,weight))
        else :              
            print(vessel)
    if dictionary :
        print('weights = {\n  '+',\n  '.join(body)+'\n}\n')
    quit()
    
weight = None
if '.py' != sys.argv[0][-3:] :
    fn = sys.argv[0]
    if '/' == fn[0] :
        fn = fn.split('/')[-1]
    if len(fn) > len(name_prefix)+1 :
        vessel = fn[1+len(name_prefix):]
        weight = weights.get(vessel)
long_opts = ['metric','list','name-prefix'] + vessels

def exit_help(message=None) :
    if None != message :
        print('Error: %s'%message)
    str = 'Usage: %s [ -h ][ -m ]'%(sys.argv[0])
    offset = 0
    for opt in long_opts :
        this = '[ --%s ]'%(opt)
        if len(str) - offset + len(this) > 80 :
            str += '\n'
            offset = len(str)
            str += '  '
        str += this
    print(str + ' <gross-weight>')
        
opts,params = getopt.getopt(sys.argv[1:],'hm',long_opts)
for opt,param in opts :
    if '-h' == opt :
        exit_help()
    elif '-m' == opt or '--metric' == opt :
        metric = false
    elif '--name-prefix' == opt :
        print(name_prefix)
        quit()
    elif '--list' == opt :
        exit_list()
    elif '--' == opt[:2] :
        for vessel in vessels :
            if vessel == opt[2:] :
                weight = weights[vessel]
    else :
        print('failure')
        print(sys.argv)

if None == weight :
    exit_help('Unknown vessel')
if 0 == len(params)  :
    exit_help('Missing <gross-weight>')
if len(params) > 1 :
    exit_help('Too many parameters: %s'%(params.__str__()))

gross_weight = float(params[0])
net_weight = gross_weight - weight
print('%.1f oz net weight (%.1f cups)'%(net_weight,net_weight/8))
