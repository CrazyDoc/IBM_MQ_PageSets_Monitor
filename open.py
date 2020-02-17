import time
import pickle
import jcl_py3
import sqlib
import os
os.environ["SETTINGS_MODULE"] = 'settings'
from python_settings import settings

TSO = jcl_py3.TSO()

pagesets = {}

def update():

	global pagesets
	timestamp = int(time.time())

	result = TSO.JCL(settings.OHOST, settings.RHOST, settings.HOST, settings.FILENAME, settings.USERNAME, settings.PASSWORD)
	for i in result:
		if 'CSQI010I'.encode('utf-8') in i:
			sindex = result.index(i) + 3
			for string in result[sindex:]:
				if 'End of page set report'.encode('utf-8') in string:
					findex = result.index(string)
					for string in result[sindex:findex]:
						graph = []
						for n in string.decode('utf-8').split(' '):
							if n != '' and n != '_' and n != 'USER' and n != '\t':
								graph.append(int(n))
						PS = "PS" + str(graph[0])

						def updata():
							if pagesets.get(PS) and pagesets.get(PS).get('data') and len(pagesets.get(PS).get('data')) > 11:
								return (pagesets.get(PS).get('data')[1:] + [[timestamp, int(graph[3]*100/graph[2])]])
							else:
								if pagesets.get(PS) and pagesets.get(PS).get('data'):
									return (pagesets.get(PS).get('data') + [[timestamp, int(graph[3]*100/graph[2])]])
								else:
									return ([[timestamp, int(graph[3]*100/graph[2])]])

						con = sqlib.connection(settings.DATABASE)
						table_name = 'ps' + str(int(int(time.time()) / 86400))
						data = [(PS, timestamp, int(graph[3]*100/graph[2]))]
						print('insert: ', data)
						sqlib.insert(con, table_name, data)
						con.close()

						pagesets[PS] = dict(label = PS, data = updata())

					break

			break

	print(pagesets)

	with open("/tmp/some.txt", 'wb') as filehandle:
		pickle.dump(pagesets, filehandle)
	filehandle.close()

while 1:
    update()
    time.sleep(300)
