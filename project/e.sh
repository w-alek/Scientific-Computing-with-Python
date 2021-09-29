#!/usr/bin/env bash
export PNAME="SciCompPy"
export ROOT="$( cd "$(dirname "$BASH_SOURCE")" ; pwd -P )"
echo "Welcome to $PNAME rooted at $ROOT"
echo "-"

# Prepare environment
python3 -m venv venv
source venv/bin/activate
echo "Installing requirements"
echo "-"
python3 -m pip install --no-cache-dir -r requirements.txt

# Configures paths. Adapt to your needs!
export DATA_DIR=$ROOT/data
export RESULTS_DIR=$ROOT/results


if [ ! -d "${RESULTS_DIR}" ]; then
  echo "Creating ${RESULTS_DIR}"
  mkdir -p ${RESULTS_DIR}
fi

if [ ! -d "${DATA_DIR}" ]; then
  echo "Creating ${DATA_DIR}"
  mkdir -p ${DATA_DIR}
fi
