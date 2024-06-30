import random

def apply_variations(payloads):
    varied_payloads = []
    event_handlers = ['onmouseover', 'onfocus', 'onblur', 'oninput', 'onchange']
    js_functions = ['console.log', 'document.write', 'eval', 'fetch']
    
    for payload in payloads:
        # Apply random event handlers
        for event in event_handlers:
            varied_payloads.append(payload.replace('alert', f"{event}=alert"))
        
        # Apply random JavaScript functions
        for func in js_functions:
            varied_payloads.append(payload.replace('alert', func))
        
        # Add original payload to ensure all base payloads are included
        varied_payloads.append(payload)
    
    return varied_payloads
