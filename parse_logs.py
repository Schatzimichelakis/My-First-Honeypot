import json
import os

LOG_FILE = 'YOUR LOG FILE PATH'
OUTPUT_FILE = 'YOUR OUTPUT FILE PATH'

sessions = {}

if os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'r') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                session_id = data.get('session')
                
                if not session_id:
                    continue

                if session_id not in sessions:
                    sessions[session_id] = {
                        'timestamp': data.get('timestamp'),
                        'username': '-',
                        'password': '-',
                        'client': 'Undefined',
                        'commands': []
                    }
                    
                eventid = data.get('eventid')
                
                if eventid == 'cowrie.client.version':
                    sessions[session_id]['client'] = data.get('version', 'Undefined')
                    
                elif eventid in ['cowrie.login.failed', 'cowrie.login.success']:
                    sessions[session_id]['username'] = data.get('username', '-')
                    sessions[session_id]['password'] = data.get('password', '-')
                    sessions[session_id]['timestamp'] = data.get('timestamp')
                    
                elif eventid == 'cowrie.command.input':
                    sessions[session_id]['commands'].append(data.get('input', ''))
                    
            except json.JSONDecodeError:
                continue

valid_attacks = [s for s in sessions.values() if s['username'] != '-']

valid_attacks.sort(key=lambda x: x['timestamp'])

recent_attacks = valid_attacks[-5:]

for attack in recent_attacks:
    if attack['commands']:
      
        attack['commands_str'] = " | ".join(attack['commands'])
    else:
        attack['commands_str'] = "No Commands Executed"

with open(OUTPUT_FILE, 'w') as out_f:
    json.dump(recent_attacks, out_f, indent=4)
