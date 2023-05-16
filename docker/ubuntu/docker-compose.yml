version: '3.5'

services:
    ubuntu-xfce-vnc:
        container_name: xfce
        image: imlala/ubuntu-xfce-vnc-novnc:latest
        shm_size: "2gb"
        ports:
            - 5555:5900
            - 6666:6080
        environment: 
            - VNC_PASSWD=shopifyisfine
            - GEOMETRY=1920x1080
            - DEPTH=24
        volumes: 
            - ./Downloads:/root/Downloads
        restart: unless-stopped
