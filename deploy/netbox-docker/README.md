# NewDoc on netbox-docker 5.0.x

Install **netbox-documents-4.6-fork** (NetBox 4.6.x / netbox-docker 5.0.x) using the official [netbox-docker plugin workflow](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

## Prerequisites

- netbox-docker `release` branch (5.0.x, NetBox 4.6.x)
- Docker Compose v2
- Secrets configured in `env/netbox.env` (required since netbox-docker 5.0.0 — no default secrets)

## Install

1. Clone netbox-docker:

```bash
git clone -b release https://github.com/netbox-community/netbox-docker.git
cd netbox-docker
```

2. Copy these files into the netbox-docker root:

```bash
cp /path/to/netbox-documents-4.6-fork/deploy/netbox-docker/plugin_requirements.txt .
cp /path/to/netbox-documents-4.6-fork/deploy/netbox-docker/Dockerfile-Plugins .
cp /path/to/netbox-documents-4.6-fork/deploy/netbox-docker/docker-compose.override.yml .
cp /path/to/netbox-documents-4.6-fork/deploy/netbox-docker/configuration/plugins.py configuration/plugins.py
```

3. Configure secrets in `env/netbox.env` (see `docker-compose.override.yml.example` in netbox-docker).

4. Build and start (both `netbox` and `netbox-worker` must use the custom image):

```bash
docker compose build --no-cache
docker compose up -d
```

5. Run migrations:

```bash
docker compose exec netbox python /opt/netbox/netbox/manage.py migrate netbox_documents
```

## Local development (editable install)

To test unreleased changes, replace `plugin_requirements.txt` with a path install and adjust `Dockerfile-Plugins`:

```dockerfile
FROM netboxcommunity/netbox:v4.6.2-5.0.1
COPY ./plugin-src /opt/netbox/plugin-src
RUN /usr/local/bin/uv pip install /opt/netbox/plugin-src
```

Copy your plugin source into `netbox-docker/plugin-src/` before building.

## Notes

- The pip package is `netbox-documents-4.6-fork`, but NetBox still loads `netbox_documents` in `PLUGINS`.
- API endpoint: `/api/plugins/netbox-documents/documents/`
- UI paths: `/plugins/documents/documents/`
