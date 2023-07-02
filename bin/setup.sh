# =============================================================================
# YMS - Setting up configuration on the machine
# =============================================================================
# Define routine to create folder if it does not exist
create_directory() {
    echo "Enter creation routine for directory: $1"
    if ! [ -d $1 ]
    then
        echo "=> Creating"
        mkdir $1
    else
        echo "=> Already exists"
    fi
}

# Create YMS folders
PATH_ROOT="$HOME/.yms"
PATH_CONFIG="$PATH_ROOT/config"
PATH_PYTHON="$PATH_ROOT/python"
PATH_ASSETS="$PATH_ROOT/assets"
create_directory $PATH_ROOT
create_directory $PATH_CONFIG
create_directory $PATH_PYTHON
create_directory $PATH_ASSETS


# =============================================================================
# Define routine to duplicate project's folders into `.yms`
copy_folder(){
    cp -R "$1/" "$PATH_ROOT/$1/"
}

# Copy projet's relevant folders
copy_folder config
copy_folder assets


# =============================================================================
# Prompt user for Youtube API key, replace in config if given 
read -r -s -p "Enter API key [use dev key as default]: " key
if [ -n "$key" ]
then
    echo $key > "$PATH_CONFIG/api.key"
fi
printf "\n"
