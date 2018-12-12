# vbs
<h1>Visul basic script module for python</h1>
<h2>allows python to: synthesize keyboard input, create visual basic style alerts and use text-to-speech</h2>
<br>
<h2>Windows only</h2>
<br>
<h2>useage:</h2>

  Text to Speech
  '''python
  import vbs
  vbs.tts("words to speak")
  '''

  Alerts
  '''python
  import vbs
  vbs.alert("alert body", boxtype="yesno", title="title text")
  '''

  Synthesize keyboard input
  '''python
  import vbs
  vbs.sendkeys("keys to send")
  '''
<h2>Other infomation:</h2>

  <h3>all functions are blocking</h3>

  vbs.sendkeys:
    acts as if all keys in string are pressed in order near instantly.
    script contiunes once all keys are sent.
    sending special keys such as backspace ({bs}) or enter (~) can be found by referencing
    https://docs.microsoft.com/en-us/dotnet/api/microsoft.visualbasic.devices.keyboard.sendkeys?view=netframework-4.7.2
  
  vbs.alert:
    alert times out by default after 100 minutes.
    this can be changed by passing a different value to the timeout optional argument.
    which is passed as an integer number of secounds.
    
    you can change the type of alert by a value to the optional argument boxtype.
    possible values are
    "okay", "cancel", "cancelable", "retry", "yesnocancel", "yesno", "warning", "critical", "info"
    
    this function then returns one of the following strings:
    "ok", "cancel", "abort", "retry", "ignore", "yes", "no"
    
    you can change the title of the alert by passing a string to the option title argument
    
  vbs.tts
    calling tts freezes execution path untill entire messege is spoken
    then returns "done" as a string
