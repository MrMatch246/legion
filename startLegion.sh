#!/bin/bash

echo "Strap yourself in, we're starting Legion..."

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Set everything we might need as executable
chmod a+x -R "$REPO_DIR/deps/*"
chmod a+x -R "$REPO_DIR/scripts/*"

# Determine OS, version and if WSL
source "$REPO_DIR/deps/detectOs.sh"

# Determine and set the Python and Pip paths
source "$REPO_DIR/deps/detectPython.sh"

# Figure if fist run or recloned and install deps 
if [ ! -f ".initialized" ] | [ -f ".justcloned" ]
then
    echo "First run here (or you did a pull to update). Let's try to automatically install all the dependancies..."
    if [ ! -d "tmp" ]
    then
        mkdir tmp
    fi

    # Setup WSL bits if needed
    if [ ! -z $ISWSL ]
    then
        echo "WSL Setup..."
        bash "$REPO_DIR/deps/setupWsl.sh"
    fi

    # Install dependancies from package manager
    echo "Installing Packages from APT..."
    "$REPO_DIR/deps/deps/installDeps.sh"

    # Install python dependancies
    echo "Installing Python Libraries..."
    "$REPO_DIR/deps/deps/installPythonLibs.sh"

    # Patch Qt
    echo "Stripping some ABIs from Qt libraries..."
    "$REPO_DIR/deps/deps/fixQt.sh"

    # Determine if additional Sparta scripts are installed
    bash "$REPO_DIR/deps/deps/detectScripts.sh"

    touch "$REPO_DIR/.initialized"
    rm "$REPO_DIR/.justcloned" -f
fi

export QT_XCB_NATIVE_PAINTING=0
export QT_AUTO_SCREEN_SCALE_FACTOR=1.5

# Verify X can be reached
source "$REPO_DIR/deps/checkXserver.sh"

if [[ $1 != 'setup' ]]
then
    /usr/bin/env python3 "$REPO_DIR/legion.py"
fi
