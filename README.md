# spotify-search app
### Build and run docker container

Clone repo `git clone https://github.com/ebruipek/spotify-search-api.git`

Chande directory `cd spotify-search`

Build image `docker build --no-cache -t spotify-search .` 
  
Run container in detached mode and publish port 5000 `docker run -d -p 5000:5000 spotify-search`
  
API should be accessible on port 5000 `curl -i http://localhost:5000/tracks/rock`


### Included third party Python Libraries
flask==1.0.2
Flask-RESTful==0.3.5
pytest==3.0.7
requests
flask-cors
nose