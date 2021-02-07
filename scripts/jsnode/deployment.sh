if [$(whoami) != "root" ]
then
    echo "Please run this shell script from root user or with sudo privilages"
    exit 1
fi

sudo su 
{{username}}
{{password}}