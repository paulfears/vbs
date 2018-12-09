set shelly = wscript.createobject("wscript.shell")
shelly.sendkeys wscript.arguments(0)
wscript.echo "done"