clear
pip3 install efficient-apriori
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "$SCRIPT_DIR"
cd  "${SCRIPT_DIR}/Code"
python3 aprior.py
echo "Go to Evals folder to see the results"