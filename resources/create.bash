
cp -R ../nginx .
cd nginx
docker build -t frontend:toymoderation .
cd ..
cp -R ../flask .
cd flask
docker build -t backend:toymoderation .
cd ..
rm -rf flask nginx