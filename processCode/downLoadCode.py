import os
from processCode import Flake8, ExtractZip
import urllib.parse
import urllib.request
from Gui import infoGui
from urllib.request import quote


def download_zip(js):
    try:
        savepath = ''
        for id in js:  # 获取user_id
            savepath = os.getcwd()+'\\'+'codePackages\\'+id
            os.mkdir(savepath)
            for case in js[id]['cases']:
                if case['final_score'] != 0:
                    user_id = id
                    filen = user_id + '-' + urllib.parse.unquote(os.path.basename(case['case_zip'])).split('_')[1]
                    url = quote(case['case_zip'], safe=";/?:@&=+$,*", encoding="utf-8")
                    # 下载zip
                    urllib.request.urlretrieve(url, filename=savepath + '\\' + filen)

        ExtractZip.openZip(savepath)
        Flake8.flake88(savepath)
        return True
    except Exception:
        infoGui.info_gui('代码下载失败！')
        return False

