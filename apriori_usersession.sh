clear
# !/usr/bin/env python3
sudo apt-get install python3-pip
sudo apt-get install python3.6
pip3 install efficient-apriori
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "$SCRIPT_DIR"
cd  "${SCRIPT_DIR}/Code"
python3 apriori.py