credentials = {
    "login": "spidermind",
    "password": "lolkekcheburek"
}

wrong_credentials = {
    "login": "spidermind",
    "password": "password"
}

correct_token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2Nlc3NfdG9rZW4iOiJzcGlkZXJtaW5kIiwidG9rZW5fdHlwZSI6ImJlYXJlciJ9.epJcNkwzHUfuwRDHk2rA43SxHPQjqJKht8YlY-LqD8w'

incorrect_token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2Nlc3NfdG9rZW4iOiJzcGlkZXJtaW5kIiwidG9rZW5fdHlwZSI6ImJlYXJlciJ9.cLvMt8kbJyvr80e2zPcR_rD-3XyM4OCQotn-yCeG6N8'

image = {'img': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAA'
        'CACAYAAADDPmHLAAACeElEQVR4nO3dvS8EQRiAcUQjUYlWovPRKBU'
        'SOuE6rVYUGoUQrZ6ITqVUKXRHriMapY5OorpEVFdK+A9mxGvM3j3Pr'
        '73s2d08meSdu1tDQ5IkSZIkiWK49gmUdty++4ocf9BaGeh7NFL7BFSX'
        'AcAZAJwBwBkAnAHAGQBc38+40Tk/qt/3CVwB4AwAzgDgDADOAOAMAM4A'
        '4Eajb/A620rO4dPP7eScnDs+5ypy8D/4WF1IXt9E5yl5f6LH57gCwBkAn'
        'AHAGQCcAcAZAJwBwIU/y47O8aVdnR6Gjo9+3p+b40vL7RO4AsAZAJwBwBk'
        'AnAHAGQCcAcAN/D7AzsNn1b9/udlNvu73AVSVAcAZAJwBwBkAnAHAGQBc+H'
        'cByy8rydfvZ+6KHl/bzWQnOYdf5J5f0Elff2muAHAGAGcAcAYAZwBwBgBnAH'
        'DhfYCops/5Oevvq8k5/2Ay/buC7HMOz3Z/cVY/5woAZwBwBgBnAHAGAGcAcAY'
        'AF94HGPTP+0vLPX9gq/DzBVwB4AwAzgDgDADOAOAMAM4A4Ip/H6D2nH+0vVf0/R'
        'ev1/y/gepfBgBnAHAGAGcAcAYAZwBwxWfY0s8R7M6V/d58jvsA6msGAGcAcAYAZw'
        'BwBgBnAHDVZ9jcPkF0zo/O6Y8bt6F9jKbvE7gCwBkAnAHAGQCcAcAZAJwBwFWfUXN'
        'zdtPn6JymX58rAJwBwBkAnAHAGQCcAcAZAFzx5wP0TqaSc/D5/Fj6Da7/8mz+3/12+'
        'vp6S+n7M77/VnSfwBUAzgDgDADOAOAMAM4A4AwALjxj5ub8qNJzcGlNvz+uAHAGAGcA'
        'cAYAZwBwBgBnAJIkSZIkSRDf7FV0A7g53CQAAAAASUVORK5CYII='}

image_kek = {'img': 'data:image/png;base64,iVBORw0KGgo'
                    'AAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAA'
                    'CbklEQVR4nO3dMUoDQRhA4SjWYhcQD2AktQdQ'
                    'CFh4AS+wIFgLNmIj5AKBXMALWAiCHsBaogeQgJ'
                    '0XED2AMH/xO8wu731tSDIJj4GZ2WxGI0mSJEmSR'
                    'LHRegCRs9eDn9ZjyLibrnr9HW+2HoDaMgA4A4AzA'
                    'DgDgDMAOAOAS69Rl+NJcZ3efb4V3yNa50fr6PPdy+'
                    'Lzvx7vSw+HdmanxccX63nVz1ebMwCcAcAZAJwBwBkA'
                    'nAHAGQDcVusBROvg8HqAWfn1o3V8Vnad3+3fVr3eYfl'
                    '+VXx/ZwA4A4AzADgDgDMAOAOAMwC45vsAkfi8fFV8NLp'
                    'eIBKd94+mmVdvzxkAzgDgDADOAOAMAM4A4AwArvk+QHad'
                    'Xlvt8S2C8/roeoHovD/iDABnAHAGAGcAcAYAZwBwBgDXfB'
                    '8gEp3Ht95H6Pv4Is4AcAYAZwBwBgBnAHAGAGcAcOE+QHQfw'
                    'Ozzu+i6+4HL7hN8/+9w/nAGgDMAOAOAMwA4A4AzADgDgAv3A'
                    'aL7/Wf/L4Au2ifotuveR9AZAM4A4AwAzgDgDADOAOAMAK73vw'
                    'uIjCcXbQewnrd9/yRnADgDgDMAOAOAMwA4A4AzALj0PkDt8/6b'
                    '449e/74+Gt/1016vr4dwBoAzADgDgDMAOAOAMwA4A4Ab/PUArdf'
                    'Ztfcpsv8HEHEGgDMAOAOAMwA4A4AzADgDgGt+Vj308/RI3z+fMwC'
                    'cAcAZAJwBwBkAnAHAGQBc9TXoy/ND6rz88Ohk0PsAff/8zgBwBgBn'
                    'AHAGAGcAcAYAZwBw6d8FZNe5Kou+3+w+gTMAnAHAGQCcAcAZAJwBwB'
                    'mAJEmSJEkSxC+w/HojDgBf3AAAAABJRU5ErkJggg=='}
