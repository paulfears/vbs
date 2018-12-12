# vbs
<h1>Visul basic script module for python</h1>
<h2>allows python to: </h2>
  synthesize keyboard input, create visual basic style alerts and use text-to-speech
<br>
<h3>Windows only</h3>
<br>
<h3>useage:</h3>

  <h4>Text to Speech</h4>
  
  ```python
  import vbs
  vbs.tts("words to speak")
  ```

  <h4>Alerts</h4>
  
  ```python
  import vbs
  vbs.alert("alert body", boxtype="yesno", title="title text")
  ```

  <h4>Synthesize keyboard input</h4>
  
  ```python
  import vbs
  vbs.sendkeys("keys to send")
  ```
<h2>Other infomation:</h2>

  <h3>all functions are blocking</h3>

  vbs.sendkeys:
  
    acts as if all keys in string are pressed in order near instantly.
    script contiunes once all keys are sent.
    sending special keys such as backspace ({bs}) or enter (~) can be found by referencing
    
    KEY                       CODE
    
    BACKSPACE	                {BACKSPACE} or {BS}
    BREAK 	                  {BREAK}
    CAPS LOCK 	              {CAPSLOCK}
    CLEAR 	                  {CLEAR}
    DELETE	                  {DELETE} or {DEL}
    DOWN ARROW  	            {DOWN}
    END                     	{END}
    ENTER (numeric keypad)    {ENTER}
    ENTER 	                   ~
    ESC 	                    {ESCAPE} or {ESC}
    HELP  	                  {HELP}
    HOME  	                  {HOME}
    INS 	                    {INSERT}
    LEFT ARROW  	            {LEFT}
    NUM LOCK  	              {NUMLOCK}
    PAGE DOWN  	              {PGDN}
    PAGE UP  	                {PGUP}
    RETURN  	                {RETURN}
    RIGHT ARROW  	            {RIGHT}
    SCROLL LOCK  	            {SCROLLLOCK}
    TAB  	                    {TAB}
    UP ARROW  	              {UP}
    F1 through F15  	        {F1} through {F15}
  
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
    
  vbs.tts:
  
    calling tts freezes execution path untill entire messege is spoken
    then returns "done" as a string
