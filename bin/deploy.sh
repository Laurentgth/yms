# =============================================================================
# YMS Deployment on the system
# =============================================================================

# Set up configuration 
# Define constants: $PATH_ROOT, $PATH_CONFIG, $PATH_PYTHON, $PATH_ASSETS
# Define routines: copy_folder, create_directory
source bin/setup.sh

# Copy Python modules
cp python/module* $PATH_PYTHON
cp python/yms.py $PATH_PYTHON

# Create Bash executable
echo "python3 $PATH_PYTHON/yms.py \$@" > "$PATH_ROOT/yms-execution.sh"
chmod +x "$PATH_ROOT/yms-execution.sh"

# Create user's bin folder if necessary
create_directory ~/bin

# Create `yms` symlink to use as a command in user's executable folder
ln -fs "$PATH_ROOT/yms-execution.sh" ~/bin/yms
