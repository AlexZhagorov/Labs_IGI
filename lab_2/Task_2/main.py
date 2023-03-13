import json

import user_flow as u_f
import commands as com

try:
    while True:
        username = u_f.authorize()
        if username == False: quit()
        if com.do_commands(username) == False: quit()
except OSError:
    print("Problem with a data file")
    quit()
except json.decoder.JSONDecodeError:
    print("Problem with a data file")
    quit()