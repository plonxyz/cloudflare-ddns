#!/bin/bash

# Create the crontab file with environment variables
cat <<EOF > /etc/cron.d/dnsupdate-cron
# Set environment variables
CLOUDFLARE_API_TOKEN=${CLOUDFLARE_API_TOKEN}
CLOUDFLARE_ZONE_ID=${CLOUDFLARE_ZONE_ID}
CLOUDFLARE_RECORD_ID=${CLOUDFLARE_RECORD_ID}
CLOUDFLARE_RECORD_NAME=${CLOUDFLARE_RECORD_NAME}

# Run the python script every minute
* * * * *   /usr/local/bin/python /app/update_dns.py >> /var/log/cron.log 2>&1
EOF

# Give execution rights on the cron job
chmod 0644 /etc/cron.d/dnsupdate-cron

# Apply cron job
crontab /etc/cron.d/dnsupdate-cron

# Create the log file to be able to run tail
touch /var/log/cron.log
