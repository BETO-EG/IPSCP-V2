import sys
import requests
import ctypes
from multiprocessing.pool import ThreadPool
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

IPS = sys.argv[1]
good = 0
bad = 0
totalnum = len(IPS)

def CHK(IP):
    global good
    global bad
    global totalnum
    ctypes.windll.kernel32.SetConsoleTitleA('CPANEL IPS CHECKER BETO |THANKS FOR SIR.BUGS||IPS {} | {} |BAD CHECKED {}'.format(good, totalnum, bad))
    try:

		r = requests.get('https://{}/cpanel'.format(IP), verify=False, timeout=6)
    except:

        print '{} -> NotFound.'.format(IP)
        bad += 1
        pass

    else:
		if 'cpanel' in r.content:
			print '{} -> Cpanel.'.format(IP)
			file = open("CPANELSIPS.txt", "a").write(IP + '\n')
			good += 1
		else:
			print '{} -> NotFound.'.format(IP)
			bad += 1
if __name__ == '__main__':
    IPS = open(IPS, 'r').read().split('\n')
    totalnum = len(IPS)
    pool = ThreadPool(1500)
    for _ in pool.imap_unordered(CHK, IPS):
        pass
