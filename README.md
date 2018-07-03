# Django-CI-CD
## A test project for CI/CD Pipeline
### This test project includes the following:
+ A Django Project inside __src__
+ Project configurations in __config__
+ A *Jenkinsfile* for setting up Jenkins Pipeline
+ A *Dockerfile* for configuring the docker image
+ A *docker-compose.yaml* for configuring the docker container

### The stack contains:
+ Django
+ Docker
+ Gunicorn
+ Jenkins
+ MySQL
+ NGINX

Deployment is on a Ubuntu 16.04 server

#### NOTE: Config files under __config__ are not committed to VC
+ config
	+ nginx
		+ testproj.conf (x contains nginx configuration)
	+ requirements.txt (contains required python modules)
	+ development.env (x contains configuration for development)
	+ production.env (x contains configuration for production)