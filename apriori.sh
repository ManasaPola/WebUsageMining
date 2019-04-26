clear
# !/usr/bin/env python3
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "$SCRIPT_DIR"
cd  "${SCRIPT_DIR}/Code"


sudo apt-get -y install r-base
RScript aprioriAlgo.r

echo "Go to Evals folder to see the results"