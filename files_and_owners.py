# 1 Python
# 1.1 Escreva uma funcão que dado um caminho de diretório ira retornar duas listas,
# uma lista com os arquivos deste diretório e outra lista com os donos desses
# arquivos, ambas na mesma ordem.
# 1.2 Agora, tomando a lista de nomes de arquivos e a lista de donos de arquivos (doitem 1.1),
# escreva uma funcão que agrupe os arquivos pelo dono, retornando um dicionário
# com a lista de arquivos de cada dono.

import os
from os import listdir, stat
from os.path import isfile, join
# only linux
if os.name != 'nt':
    from pwd import getpwuid
# only windows
if os.name == 'nt':
    from subprocess import Popen, PIPE
    from collections import namedtuple

def sliceit(iterable, tup):
    return iterable[tup[0]:tup[1]].strip()

def convert_cat(line):
    # Column Align Text indicies from cmd
    # Date time dir filesize owner filename
    Stat = namedtuple('Stat', 'date time directory size owner filename')
    stat_index = Stat(date=(0, 11), 
                      time=(11, 18), 
                      directory=(18, 27), 
                      size=(27, 35), 
                      owner=(35, 59), 
                      filename=(59, -1))

    stat = Stat(date=sliceit(line, stat_index.date),
                      time=sliceit(line, stat_index.time),
                      directory=sliceit(line, stat_index.directory),
                      size=sliceit(line, stat_index.size),
                      owner=sliceit(line, stat_index.owner),
                      filename=sliceit(line, stat_index.filename))
    return stat

def stats(path):
    if not os.path.isdir(path):
        dirname, filename = os.path.split(path)
    else:
        dirname = path
    cmd = ["cmd", "/c", "dir", dirname, "/q"]
    session = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    # cp1252 is common on my Norwegian Computer,
    # check encoding from your windows system
    result = session.communicate()[0].decode('cp1252')

    if os.path.isdir(path):
        line = result.splitlines()[5]
        return convert_cat(line)
    else:
        for line in result.splitlines()[5:]:
            if filename in line:
                return convert_cat(line)
        else:
            raise Exception('Could not locate file')

def file_and_owner(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    owners = []
    for x in onlyfiles:
        owners.append(find_owner(mypath+'\\'+x)) 
    return [onlyfiles, owners]

def find_owner(filename):
    # windows
    if os.name == 'nt':
        return stats(filename).owner
    # linux
    return getpwuid(stat(filename).st_uid).pw_name

def merge_arr(path):
    res = file_and_owner(path)
    thisdict = {}
    i = 0;
    for x in res[0]:
        thisdict[x] = res[1][i];
        i += 1
    return thisdict

# 1.1
print(file_and_owner('C:\workspace\pydir\\fotos'))

# 1.2
print(merge_arr('C:\workspace\pydir\\fotos'))




