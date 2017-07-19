# -*- coding: utf-8 -*-

import requests
import progressbar
# import requests.packages.urllib3

class DownloadHelper(object):
    def download(url, filePath):
        response = requests.request("GET", url, stream=True, data=None, headers=None)
                
        total_length = int(response.headers.get("Content-Length"))
        with open(requests, 'wb') as f:
            widgets = ['Progress: ', progressbar.Percentage(), ' ',
                    progressbar.Bar(marker='#', left='[', right=']'),
                    ' ', progressbar.ETA(), ' ', progressbar.FileTransferSpeed()]
            pbar = progressbar.ProgressBar(widgets=widgets, maxval=total_length).start()
            for chunk in response.iter_content(chunk_size=1):
                if chunk:
                    f.write(chunk)
                    f.flush()
                pbar.update(len(chunk) + 1)
            pbar.finish()
