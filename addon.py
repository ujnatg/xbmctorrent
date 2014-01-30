import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resources', 'site-packages'))

def get_params():
  param = []
  paramstring = sys.argv[2]
  if len(paramstring) >= 2:
    params = sys.argv[2]
    cleanedparams = params.replace("?","")
    if (params[len(params)-1] == "/"):
      params = params[0:len(params)-2]
    pairsofparams = cleanedparams.split("&")
    param = {}
    for i in range(len(pairsofparams)):
      splitparams = {}
      splitparams = pairsofparams[i].split("=")
      if (len(splitparams)) == 2:
        param[splitparams[0]] = splitparams[1]
                                
  return param

params = get_params()
REPO_DATA_DIR = "https://cloclo1.datacloudmail.ru/weblink/get/8c8ab386191a/repository/"

try:
    if "action" in params and params["action"] in ("install", "update", "uninstall") \
       and "package" in params and "version" in params:
        action, package, version = [params.get(k) for k in ["action", "package", "version"]]
        xbmc.log("Process %s addon:%s version:%s" % (action, package, version))
  
        from installer import AddonInstaller
        AddonInstaller(REPO_DATA_DIR).process(action, package, version)
    elif __name__ == '__main__':
        from xbmctorrent import plugin
        plugin.run()
except Exception, e:
    import xbmc
    import traceback
    map(xbmc.log, traceback.format_exc().split("\n"))
    raise
