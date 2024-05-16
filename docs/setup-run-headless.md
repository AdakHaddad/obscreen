# <img src="https://github.com/jr-k/obscreen/blob/master/docs/img/obscreen.png" width="22"> Obscreen - Headless run on any server

> #### 👈 [back to readme](/README.md)

#### 🔵 You want to start browser and setup playlist url manually on your device and just want a slideshow manager ? You're in the right place.

---
## 🐳 Run with docker
### With docker (for test)
```bash
# Prepare application data file tree
mkdir -p obscreen/data/db obscreen/data/uploads && cd obscreen

# Run the Docker container
docker run --rm --name obscreen --pull=always \
  -e DEBUG=false \
  -e PORT=5000 \
  -e PLAYER_AUTOSTART_FILE=/app/var/run/play \
  -e SECRET_KEY=ANY_SECRET_KEY_HERE \
  -p 5000:5000 \
  -v ./data/db:/app/data/db \
  -v ./data/uploads:/app/data/uploads \
  -v /dev/null:/app/var/run/play \
  jierka/obscreen:latest
```

### With docker-compose
```bash
# Prepare application data file tree
mkdir -p obscreen/data/db obscreen/data/uploads && cd obscreen

# Download docker-compose.yml
curl https://raw.githubusercontent.com/jr-k/obscreen/master/docker-compose.headless.yml > docker-compose.yml

# Run
docker compose up --detach --pull always
```
---
## 📠 Run system wide
### Install
```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y git

# Get files
git clone https://github.com/jr-k/obscreen.git && cd obscreen

# Install application dependencies
pip3 install -r requirements.txt

# Add some sample data
cp data/db/slideshow.json.dist data/db/slideshow.json

# Customize server default values
cp .env.dist .env
```

### Configure
- Server configuration is editable in `.env` file.
- Application configuration will be available at `http://localhost:5000/settings` page after run.

### Start server (for test)
```bash
./obscreen.py
```

### Start server forever with systemctl
```bash
sudo ln -s "$(pwd)/system/obscreen-manager.service" /etc/systemd/system/obscreen-manager.service
sudo systemctl daemon-reload
sudo systemctl enable obscreen-manager.service
sudo systemctl start obscreen-manager.service
```

To troubleshoot you can check logs
```bash
sudo journalctl -u obscreen-manager -f 
```
---
## 👌 Usage
- Page which plays slideshow is reachable at `http://localhost:5000`
- Slideshow manager is reachable at `http://localhost:5000/manage`
