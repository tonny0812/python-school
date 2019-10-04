
from pySmartDL import SmartDL

# url = "http://cdn12.bookln.cn/1323577_e0c4644d8bdbc5024a598ede1d318c09a77ea582.zip"
url = "http://megasearch.co/goto?id=1835535&slug=camila-cabello-liar-mp3"
dest = "Downloads"

obj = SmartDL(url, dest)
obj.start()
path = obj.get_dest()