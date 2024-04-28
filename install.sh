#!/usr/bin/bash
#
#           SABU Endpoint Installer Script v2.0.0
#
#   GitHub: https://github.com/sabu-ws/endpoint
#   Issues: https://github.com/sabu-ws/endpoint/issues
#
#   This script installs SABU Endpoint to your system.
#   Usage:
#
#   	$ wget -qO- https://get.endpoint.sabu.it/ | bash
#   	  or
#   	$ curl -fsSL https://get.endpoint.sabu.it/ | bash
#
#   In automated environments, you may want to run as root.
#   If using curl, we recommend using the -fsSL flags.
#

# VARS
NAME_ENDPOINT=""
SERVER_IP=""
API_TOKEN=""
PACKAGES_PART_1="dirmngr apt-transport-https lsb-release ca-certificates gnupg nodejs nginx openssl python3 python3-pip python3-venv nftables rsyslog gnupg wget ipcalc"

# DEFINE COLORS
readonly COLOUR_RESET='\e[0m'
readonly COLOURS=(
    '\e[38;5;154m' # green
    '\e[1m'        # Bold white
    '\e[90m'       # Grey
    '\e[91m'       # Red
    '\e[33m'       # Yellow
    '\e[36m'       # Blue Cyan
)

readonly GREEN_LINE=" ${COLOURS[0]}─────────────────────────────────────────────────────$COLOUR_RESET"
readonly GREEN_BULLET=" ${COLOURS[0]}-$COLOUR_RESET"


show() {

    # OK
    if (( $1 == 0 ))
    then
        echo -e "${COLOURS[2]}[$COLOUR_RESET${COLOURS[0]}  OK  $COLOUR_RESET${COLOURS[2]}]$COLOUR_RESET $2"
    
    # FAILED
    elif (( $1 == 1 ))
    then
        echo -e "${COLOURS[2]}[$COLOUR_RESET${COLOURS[3]}FAILED$COLOUR_RESET${COLOURS[2]}]$COLOUR_RESET $2"
        exit 1

    # INFO
    elif (( $1 == 2 ))
    then
        echo -e "${COLOURS[2]}[$COLOUR_RESET${COLOURS[5]} INFO $COLOUR_RESET${COLOURS[2]}]$COLOUR_RESET $2"

    # NOTICE
    elif (( $1 == 3 ))
    then
        echo -e "${COLOURS[2]}[$COLOUR_RESET${COLOURS[4]}NOTICE$COLOUR_RESET${COLOURS[2]}]$COLOUR_RESET $2"
    
    # ASK
    elif (( $1 == 4))
    then
        echo -e "${COLOURS[2]}[${COLOURS[4]} ASK  ${COLOURS[2]}]${COLOUR_RESET} $2"
 
    fi
}

color_reset() {

    echo -e "$COLOUR_RESET\c"
}

color_gray() {

    echo -e "${COLOURS[2]}\c"
}

color_red() {

    echo -e "${COLOURS[3]}\c"
}

# BANNER
banner() {

    echo -e "

     _____         ____  _    _   ______ _   _ _____  _____   ____ _____ _   _ _______ 
    / ____|  /\   |  _ \| |  | | |  ____| \ | |  __ \|  __ \ / __ \_   _| \ | |__   __|
   | (___   /  \  | |_) | |  | | | |__  |  \| | |  | | |__) | |  | || | |  \| |  | |   
    \___ \ / /\ \ |  _ <| |  | | |  __| | .   | |  | |  ___/| |  | || | | .   |  | |   
    ____) / ____ \| |_) | |__| | | |____| |\  | |__| | |    | |__| || |_| |\  |  | |   
   |_____/_/    \_\____/ \____/  |______|_| \_|_____/|_|     \____/_____|_| \_|  |_|   

                      --- Made by CyberCrackito with ❤️  ---
    "                                                                                                                                                                                             
}

# CHECK_REQUIREMENTS
check_requirements() {

    show 2 "Checking requirements..."

    # GET NAME ENDPOINT
    show 2 "Checking endpoint name..."
    show 4 "What is the name of the endpoint ?"
    read -p "- " NAME_ENDPOINT
    show 2 "Endpoint name : ${COLOURS[2]}(${NAME_ENDPOINT})${COLOUR_RESET}"

    if [ -z "$NAME_ENDPOINT" ]
    then
        show 1 "The endpoint name has not been set, cancel installation."
    else
        show 2 "The endpoint name has been set successfully"
    fi

    # GET SERVER IP
    show 2 "Checking server IP..."
    show 4 "What is the server IP address ?"
    read -p "- " SERVER_IP
    show 2 "Server IP : ${COLOURS[2]}(${SERVER_IP})${COLOUR_RESET}"

    if [ -z "$SERVER_IP" ]
    then
        show 1 "The server IP address has not been set, cancel installation."
    else
        show 2 "The server IP address has been set successfully"
    fi

    # GET API TOKEN
    show 2 "Checking API token ..."
    show 4 "What is the API token ?"
    read -p "- " API_TOKEN
    show 2 "API Token : ${COLOURS[2]}(${API_TOKEN})${COLOUR_RESET}"

    if [ -z "$API_TOKEN" ]
    then
        show 1 "The API token has not been set, cancel installation."
    else
        show 2 "The API token has been set successfully"
    fi

        # CHECK USERS
    show 2 "Checking users..."
    id sabu > /dev/null 2>&1

    if [ $? -eq 0 ]
    then
        while true
        do

        show 4 "A user named ${COLOURS[4]}sabu ${COLOUR_RESET}was found. This user was deleted and recreate. (${COLOURS[0]}yes${COLOUR_RESET}/${COLOURS[3]}no${COLOUR_RESET})"
        read -p "- " choice1

        case $choice1 in 
            yes ) 
                show 2 "User sabu was recreated after."
                deluser sabu > /dev/null 2>&1
                break;;
            no )
                show 1 "Installation was cancelled"
                exit 1;;
            * )
                show 4 "Invalid response";;
        esac

        done

    else
        show 0 "User sabu check"
    fi

    id svc-sabu > /dev/null 2>&1

    if [ $? -eq 0 ]
    then
        while true
        do

        show 4 "A user named ${COLOURS[4]}svc-sabu ${COLOUR_RESET}was found. This user was deleted and recreate. (${COLOURS[0]}yes${COLOUR_RESET}/${COLOURS[3]}no${COLOUR_RESET})"
        read -p "- " choice2

        case $choice2 in 
            yes ) 
                show 2 "User svc-sabu was recreated after."
                deluser svc-sabu > /dev/null 2>&1
                break;;
            no )
                show 1 "Installation was cancelled"
                exit 1;;
            * )
                show 4 "Invalid response";;
        esac

        done

    else
        show 0 "User svc-sabu check"
    fi

    id kiosk-sabu > /dev/null 2>&1

    if [ $? -eq 0 ]
    then
        while true
        do

        show 4 "A user named ${COLOURS[4]}kiosk-sabu ${COLOUR_RESET}was found. This user was deleted and recreate. (${COLOURS[0]}yes${COLOUR_RESET}/${COLOURS[3]}no${COLOUR_RESET})"
        read -p "- " choice3

        case $choice3 in 
            yes ) 
                show 2 "User kiosk-sabu was recreated after."
                deluser kiosk-sabu > /dev/null 2>&1
                break;;
            no )
                show 1 "Installation was cancelled"
                exit 1;;
            * )
                show 4 "Invalid response";;
        esac

        done

    else
        show 0 "User kiosk-sabu check"
    fi
}

# INSTALL_PACKAGES
install_packages() {

    # UPDATE & UPGRADE
    show 2 "Updating and upgrade package manager..."
    color_red
    apt-get update > /dev/null 2>&1
    apt-get upgrade -y > /dev/null 2>&1
    show 0 "Updating and upgrade package manager complete."

    # REQUIREMENTS PKG
    apt-get install gpg curl git sudo -y > /dev/null 2>&1

    # INSTALL
    show 2 "Install necessary packages: ${COLOURS[4]}${PACKAGES_PART_1}"
    color_red
    apt-get install ${PACKAGES_PART_1} -y > /dev/null 2>&1
    show 0 "Install necessary packages complete."

    # REMOVE & CLEAN
    show 2 "Remove and cleaning packages..."
    color_red
    apt-get autoremove -y > /dev/null 2>&1
    apt-get clean > /dev/null 2>&1
    show 0 "Remove and cleaning complete."
}

# USERS
users() {

    # SABU
    show 2 "Creating users..."
    color_red
    useradd sabu --home /home/sabu --create-home --shell /bin/bash --password '$1$Av4Qv9gg$flzrWXMp0qC8aVEuu6XBF1' > /dev/null 2>&1
    usermod -a -G adm sabu > /dev/null 2>&1

    # SVC-SABU
    mkdir -p /sabu/
    useradd svc-sabu --home /sabu/ --shell /bin/false > /dev/null 2>&1
    usermod -a -G adm svc-sabu > /dev/null 2>&1

    # KIOSK-SABU
    useradd kiosk-sabu --home /home/kiosk-sabu --create-home --shell /bin/bash --password '$1$Av4Qv9gg$flzrWXMp0qC8aVEuu6XBF1' > /dev/null 2>&1

    chown -R svc-sabu:svc-sabu /sabu/ > /dev/null 2>&1
    chmod -R 0750 /sabu/ > /dev/null 2>&1
    show 0 "Creating complete."
}

# GIT CLONE
clone_git() {

    # CLONE REPO
    show 2 "Clone git repository"
    cd /sabu
    git clone https://github.com/sabu-ws/endpoint.git > /dev/null 2>&1
    show 0 "Clone complete."
}

# CONFIG SYSTEM
config_system() {

    # DISABLE IPV6
    show 2 "IPV6 setup..."
    cp /sabu/server/deploy/10-disable-ipv6.conf /etc/sysctl.d/10-disable-ipv6.conf > /dev/null 2>&1
    sysctl -p -f /etc/sysctl.d/10-disable-ipv6.conf > /dev/null 2>&1
    show 0 "IPV6 setup Complete"

    # SSH CONFIGURATION
    show 2 "SSH setup..."
    cp /sabu/server/deploy/sshd_config /etc/ssh/sshd_config > /dev/null 2>&1
    systemctl enable ssh > /dev/null 2>&1
    systemctl restart ssh > /dev/null 2>&1
    show 0 "SSH setup Complete"

    # SUDO COMMAND
    show 2 "Sudo setup..."
    cp /sabu/endpoint/deploy/sabu.sudo /etc/sudoers.d/sabu > /dev/null 2>&1
    show 0 "Sudo setup Complete"
}

# DEPLOY NGINX
deploy_nginx() {

    # NGINX CONF
    show 2 "Nginx setup..."
    rm /etc/nginx/sites-available/default > /dev/null 2>&1
    rm /etc/nginx/sites-enabled/default > /dev/null 2>&1

    mkdir -p /sabu/nginx/
    mkdir -p /sabu/logs/server/nginx/
    cp /sabu/endpoint/deploy/nginx/maintenance.html /sabu/nginx/maintenance.html
    sed -i 's/www-data/svc-sabu/g' /etc/nginx/nginx.conf

    mkdir -p /sabu/ssl/private/

    # GEN AUTOIGN CERTIF
    show 0 "SSL Generate selfsign certificate"
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /sabu/ssl/private/sabu.key -out /sabu/ssl/sabu.crt -subj "/C=FR/ST=BRITTANY/L=Rennes/O=SABU/OU=SABU/CN=sabu.local" > /dev/null 2>&1

    cp /sabu/server/deploy/nginx/sabu.conf /etc/nginx/sites-available/sabu.conf > /dev/null 2>&1
    ln -s /etc/nginx/sites-available/sabu.conf /etc/nginx/sites-enabled/sabu.conf > /dev/null 2>&1

    nginx -t > /dev/null 2>&1
    systemctl enable nginx > /dev/null 2>&1
    systemctl restart nginx > /dev/null 2>&1
    show 0 "Nginx setup Complete"
}

# DEPLOY PYTHON
deploy_python() {

    # PYTHON CONF
    show 2 "Python setup..."
    cd /sabu/
    python3 -m venv venv-sabu > /dev/null 2>&1
    source /sabu/venv-sabu/bin/activate > /dev/null 2>&1
    show 0 "Python setup complete"

    # PIP INSTALL
    show 2 "Installing requirements..."
    pip3 install -r /sabu/endpoint/requirements.txt > /dev/null 2>&1
    # pip3 freeze
    show 0 "Install requirements complete"
}

# DEPLOY NFTABLES
deploy_nftables() {

    show 2 "Nftables setup..."
    systemctl start nftables.service > /dev/null 2>&1
    systemctl enable nftables.service > /dev/null 2>&1
    show 0 "Nftables setup complete"
}

# DEPLOY SABU
deploy_sabu() {

    # UPDATE .ENV
    cp /sabu/endpoint/.env.model /sabu/endpoint/.env > /dev/null 2>&1
    sed -i 's|^HOSTNAME_ENDPOINT=.*|HOSTNAME_ENDPOINT="'"$NAME_ENDPOINT"'"|' /sabu/endpoint/.env
    sed -i 's|^SERVER_IP=.*|SERVER_IP="'"$SERVER_IP"'"|' /sabu/endpoint/.env
    sed -i 's|^TOKEN_API=.*|TOKEN_API="'"$API_TOKEN"'"|' /sabu/endpoint/.env

    # CONFIG AUTOSTART BROWSER
    echo -e "[autostart]
          chromium = chromium-browser https://localhost --kiosk --noerrdialogs --disable-infobars --no-first-run --ozone-platform=wayland --enable-features=OverlayScrollbar --start-maximized
          screensaver = false
          dpms = false" >> /home/kiosk-sabu/.config/wayfire.ini

    # SABU SERVICE & DIR
    show 2 "SABU setup..."
    mkdir -p /sabu/logs/endpoint
    
    cp /sabu/endpoint/deploy/sabu.service /etc/systemd/system/sabu.service > /dev/null 2>&1
    
    systemctl daemon-reload > /dev/null 2>&1
    
    systemctl start sabu.service > /dev/null 2>&1
    systemctl enable sabu.service > /dev/null 2>&1
    
    show 0 "SABU setup complete"
}

# END INSTALL
end_install() {

    # FIX PERM
    show 2 "End install..."
    chown -R svc-sabu:svc-sabu /sabu/
    chmod -R 0750 /sabu/
    show 0 "End install complete"

    # APPLY FILETRING
    INT=$(ip -br a | tail -n 1 | awk '{print $1}')
    sh /sabu/endpoint/core/scripts/filtering_dev.sh $INT

    # REBOOT
    show 2 "Waiting reboot..."
    sleep 1
    show 2 "Press a ${COLOURS[4]}KEY ${COLOUR_RESET}to reboot"
    read -s -n 1
    reboot
}

# MAIN
# BANNER
banner

# REQUIREMENTS
check_requirements

# INSTALL PACKAGES
install_packages

# USERS
users

# GIT
clone_git

# SYSTEM CONFIG
config_system

# DEPLOY NGINX
deploy_nginx

# DEPLOY PYTHON
deploy_python

# DEPLOY SABU
deploy_sabu

# END INSTALL
end_install
