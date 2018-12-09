import vbs

vbs.tts("hello world")
continute_tests = vbs.alert("continute_tests", "yesno")
if(continute_tests == "yes"):
	vbs.sendkeys("these keys are sentthesethese")