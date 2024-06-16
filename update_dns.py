import os
import requests

# Configuration from environment variables
api_token = os.getenv('CLOUDFLARE_API_TOKEN')
zone_id = os.getenv('CLOUDFLARE_ZONE_ID')
record_id = os.getenv('CLOUDFLARE_RECORD_ID')
record_name = os.getenv('CLOUDFLARE_RECORD_NAME')

# Cloudflare API URLs
zone_url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}'

# Headers for the Cloudflare API
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json().get('ip')
    except requests.RequestException as e:
        print(f'Error fetching public IP: {e}')
        return None

def get_current_dns_ip():
    try:
        response = requests.get(zone_url, headers=headers)
        response.raise_for_status()
        return response.json().get('result', {}).get('content')
    except requests.RequestException as e:
        print(f'Error fetching DNS record: {e}')
        return None

def update_dns_record(ip):
    data = {
        'type': 'A',
        'name': record_name,
        'content': ip,
        'ttl': 1,  # Auto
        'proxied': False  # Change to True if you want Cloudflare's proxy enabled
    }
    try:
        response = requests.put(zone_url, headers=headers, json=data)
        response.raise_for_status()
        print(f'DNS record updated to {ip}')
    except requests.RequestException as e:
        print(f'Error updating DNS record: {e}')

def main():
    public_ip = get_public_ip()
    if not public_ip:
        print('Could not determine public IP. Exiting.')
        return

    current_dns_ip = get_current_dns_ip()
    if not current_dns_ip:
        print('Could not determine current DNS IP. Exiting.')
        return

    if public_ip == current_dns_ip:
        print('Public IP has not changed. No update needed.')
    else:
        print(f'Public IP has changed from {current_dns_ip} to {public_ip}. Updating DNS record.')
        update_dns_record(public_ip)

if __name__ == '__main__':
    main()
