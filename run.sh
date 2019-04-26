clear
# !/usr/bin/env python3
sudo apt-get install python3-pip
sudo apt-get install python3.6
pip3 install efficient-apriori
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "$SCRIPT_DIR"
cd  "${SCRIPT_DIR}/Code"
python3 apriori.py

pip3 install pickle
pip3 install numpy
pip3 install scikit-learn
python3 clustering.py

echo "Go to Evals folder to see the results"