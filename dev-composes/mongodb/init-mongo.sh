#!/bin/bash
echo "Initializing MongoDB..."

mongosh <<EOF
use console
EOF

echo "MongoDB initialization complete."
