
cp -R ../nginx .
cd nginx
docker build -t ghcr.io/iuaui71/frontend:latest .
cd ..
cp -R ../flask .
cd flask
docker build -t ghcr.io/iuaui71/backend:latest .
cd ..
rm -rf flask nginx