# -*- coding: utf-8 -*-

import urllib2
import shutil
import sys


def main():
    if len(sys.argv)<>2:
        print "Usage: python dump_any_file.py <txt-file-contains-all-urls>"
        sys.exit(0)
    links = loadLinesFromFile(str(sys.argv[1]))
    for link in links:
        print link
        download(link)

def loadLinesFromFile(fileName):
    lines = []
    with open (fileName, "r") as myfile:
        lines = [line.strip() for line in myfile]
    return lines

def download(url, fileName=None):
    def getFileName(url,openUrl):
        if 'Content-Disposition' in openUrl.info():
            # If the response has Content-Disposition, try to get filename from it
            cd = dict(map(
                lambda x: x.strip().split('=') if '=' in x else (x.strip(),''),
                openUrl.info()['Content-Disposition'].split(';')))
            if 'filename' in cd:
                filename = cd['filename'].strip("\"'")
                if filename: return filename
        # if no filename was found above, parse it out of the final URL.
        return os.path.basename(urlparse.urlsplit(openUrl.url)[2])

    r = urllib2.urlopen(urllib2.Request(url))
    try:
        fileName = fileName or getFileName(url,r)
        with open(fileName, 'wb') as f:
            shutil.copyfileobj(r,f)
    finally:
        r.close()

if __name__ == "__main__":
    main()
