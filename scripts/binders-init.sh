#!/usr/bin/env bash

set -e

# Create an admin user
fabmanager create-admin --app binders $@

# Initialize the database
binders db upgrade

# Create default roles and permissions
binders init
