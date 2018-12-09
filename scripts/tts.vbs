set shelly = wscript.createobject("wscript.shell")
set speaker = createobject("sapi.spVoice")


speaker.speak(Wscript.arguments(0))
wscript.echo "done"