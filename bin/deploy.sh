# ======================================================================
# Created in July 2023
# Author: L. Gauthier @ FizzDevS Designs
# License: MIT
# Description: Youtube Metadata Script (YMS) - A Python script to
#              extract Youtube video metadata
# ======================================================================
# --> Shell script deploying the script as a CLI command in the system
# ======================================================================

# Set up configuration 
# Define constants: $PATH_ROOT, $PATH_CONFIG, $PATH_PYTHON, $PATH_ASSETS
# Define routines: copy_folder, create_directory
source bin/setup.sh

# Copy Python modules
cp python/module* $PATH_PYTHON
cp python/yms.py $PATH_PYTHON

# Create Bash executable
chmod +x "$PATH_CONFIG/yms-execution.sh"

# Create user's bin folder if necessary
create_directory ~/bin

# Create `yms` symlink to use as a command in user's executable folder
ln -fs "$PATH_CONFIG/yms-execution.sh" ~/bin/yms
