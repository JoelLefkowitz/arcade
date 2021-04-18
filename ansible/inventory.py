#!/usr/bin/env python
import os

from digitalocean_inventory import fetch

# export DO_ENV=staging;
# export ANSIBLE_SSH_RETRIES=5

if __name__ == "__main__":
    os.environ.setdefault("DO_PROJECT", "arcade")
    os.environ.setdefault("DO_SSH_DIR", "~/.ssh/arcade")
    inventory = fetch(stdout=False)
    print(inventory)
