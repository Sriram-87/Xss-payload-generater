from payloads.generators import generate_base_payloads
from payloads.variations import apply_variations
from payloads.encoders import encode_payloads
import os

def save_payloads(payloads, output_file):
    with open(output_file, 'w') as f:
        for payload in payloads:
            f.write(f"{payload}\n")

def main():
    num_payloads = 10000
    output_file = "output/xss_payloads.txt"
    
    # Generate base payloads
    base_payloads = generate_base_payloads(num_payloads)
    
    # Apply variations
    varied_payloads = apply_variations(base_payloads)
    
    # Encode payloads
    final_payloads = encode_payloads(varied_payloads)
    
    # Save to file
    if not os.path.exists('output'):
        os.makedirs('output')
    save_payloads(final_payloads, output_file)
    
    print(f"Generated {len(final_payloads)} XSS payloads and saved to {output_file}")

if __name__ == "__main__":
    main()
