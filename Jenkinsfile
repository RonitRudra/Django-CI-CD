
node('docker') {
	checkout scm
	stage('Pre-Check') {
		docker.image('python:3.6.4').inside {
			echo 'Pre-Checking...'
			sh 'python --version'
			sh 'cat config/requirements.txt'
		}
	}
}