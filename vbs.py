import os, time

def tts(words):
	return os.popen("cscript scripts/tts.vbs "+'"%s"'%words).read().split()[-1]

def sendkeys(key_stirng):
	return os.popen("cscript scripts/sendkeys.vbs "+'"%s"'%key_stirng).read().split()[-1]
def alert(messege, boxtype="ok", title="alert", timeout=6000):
	boxtypes = {"ok":0, "okay":0, "cancel":1, "cancelable":1, "retry":2, "yesnocancel":3, "yesno":4, "warning":48, "critical":16, "info":64}
	try:
		boxtype = boxtypes[boxtype]
	except KeyError:
		boxtype = 0

	returned_index = os.popen('cscript scripts/alert.vbs //T:%s "%s" "%s" "%s"'%(timeout, messege, boxtype, title)).read().split()[-1]
	if(returned_index == 'terminated.'):
		return "timed out"
	return_values = ["", "ok", "cancel", "abort", "retry", "ignore", "yes", "no"]
	returned_value = return_values[int(returned_index)]
	return returned_value


if __name__ == '__main__':
	print(alert("yello", boxtype="yesno"))
	