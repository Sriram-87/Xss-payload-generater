import urllib.parse

def url_encode(payload):
    return urllib.parse.quote(payload)

def hex_encode(payload):
    return ''.join([f"\\x{ord(char):02x}" for char in payload])

def base64_encode(payload):
    import base64
    return base64.b64encode(payload.encode()).decode()

def encode_payloads(payloads):
    encoded_payloads = []
    encoders = [url_encode, hex_encode, base64_encode]
    
    for payload in payloads:
        for encoder in encoders:
            encoded_payloads.append(encoder(payload))
        # Add original payload to ensure all base payloads are included
        encoded_payloads.append(payload)
    
    return encoded_payloads
