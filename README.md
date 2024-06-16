## Dynamic DNS Updater for Cloudflare

This container is designed to keep your Cloudflare DNS records up to date by automatically updating them whenever your external IP address changes.

### Key Features

- **Automatic IP Detection**: Continuously monitors your external IP address and detects any changes.
- **Seamless Cloudflare Integration**: Automatically updates the specified DNS records in your Cloudflare account using the Cloudflare API.
- **Environment Variable Configuration**: Easily configure your Cloudflare API token, zone ID, record ID, and record name through environment variables for secure and flexible setup.
- **Cron Job Scheduling**: Built-in support for cron jobs allows you to schedule the IP check and update process at your preferred intervals.
- **Lightweight and Efficient**: Based on the slim Python image, this container is optimized for performance and minimal resource usage.

### Getting Started

#### Docker Compose Configuration

To get started, add the following service definition to your `docker-compose.yml` file:

```yaml
services:
  dns-updater:
    image: plonxyz/cloudflare-ddns:stable
    container_name: cloudflare-ddns
    environment:
      - CLOUDFLARE_API_TOKEN= 
      - CLOUDFLARE_ZONE_ID=
      - CLOUDFLARE_RECORD_ID=
      - CLOUDFLARE_RECORD_NAME=
