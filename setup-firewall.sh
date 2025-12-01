#!/bin/bash
# UFW rules to allow all ports from trusted subnet and restrict specific ports elsewhere

# Ports to restrict (only accessible from localhost and subnet)
PORTS=(4000 8000)

# Trusted subnet (all ports allowed)
SUBNET="172.16.16.0/22"

echo "Setting up UFW rules..."

# Ensure UFW is enabled
if ! ufw status | grep -q "Status: active"; then
    echo "Warning: UFW is not active. Enable it with: sudo ufw enable"
fi

# Allow all traffic from the trusted subnet
ufw allow from $SUBNET
echo "All ports: allowed from $SUBNET"

echo ""

# Restrict specific ports for all other networks
for PORT in "${PORTS[@]}"; do
    # Deny all incoming connections to this port from outside
    ufw deny $PORT/tcp

    # Allow connections from localhost
    ufw allow from 127.0.0.1 to any port $PORT proto tcp

    echo "Port $PORT: restricted to localhost only (other networks)"
done

echo ""
echo "UFW rules applied successfully!"
echo ""
echo "Summary:"
echo "  - All ports accessible from $SUBNET"
echo "  - Ports 4000, 8000 only accessible from localhost for other networks"
echo ""
echo "To verify, run: sudo ufw status numbered"
echo ""
echo "To remove these rules later, use: sudo ufw status numbered"
echo "Then delete by number: sudo ufw delete [number]"
