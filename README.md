
## Project URLs

- ### [🐳 Production Deployment](https://alecks.dev)
- ### [📦 Public Analytics Page](https://umami.alecks.dev/share/Rmx0xBhRJUEsqdpH/alecks.dev)

## About this project
- We track website analytics on a self-hosted instance of umami
- This page is open source for maximium transparency and to provide inspiration
- It is not built for self-hosting but its fairly easy anyway due to the software I use

## Docker compose stack
Reverse proxy is not included, simply just set nginx routes to the ips below
- 10.42.0.3 (Website)
- 10.42.0.2 (Media Server)

The stack below deploys a network, volume and 2 containers
```yaml
version: '3.8'

services:
  website:
    restart: always
    image: ghcr.io/atomic2ds/alecks-website:latest
    hostname: website
    container_name: alecks-website
    networks:
      alecks:
        ipv4_address: 10.42.0.3

  media:
    restart: always
    image: ghcr.io/atomic2ds/alecks-media:latest
    hostname: media
    volumes:
      - alecks-media-data:/app/uploads
    container_name: alecks-media
    networks:
      alecks:
        ipv4_address: 10.42.0.2

volumes:
  alecks-media-data:

networks:
  alecks:
    driver: bridge
    ipam:
     config:
       - subnet: 10.42.0.0/16
         gateway: 10.42.0.1
```
