[Unit]
Description=starts the containers up and updates them on startup

[Service]
ExecStart=/home/xilinx/StartupScript/ContainerScript.sh

[Install]
WantedBy=multi-user.target

