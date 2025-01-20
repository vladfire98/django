pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vladfire.ru:latest"
	PROJECT_NAME = "vladfire.ru"
	DJANGO_SECRET_KEY = credentials('DJANGO_SECRET_KEY')
    }

    stages {
//        stage('Build Docker Image') {
//            steps {
//                script {
//                    sh """
//                        docker build -t ${DOCKER_IMAGE} .
//                    """
//                }
//            }
//        }

        stage('Deploy Container') {
            steps {
                script {
		            sh "docker ps -q -f 'name=${PROJECT_NAME}' | xargs -r docker stop"
		            sh "docker ps -a -q -f 'name=${PROJECT_NAME}' | xargs -r docker rm"
			    export DJANGO_SECRET_KEY=${env.DJANGO_SECRET_KEY}
			    sh "docker run -d --name ${PROJECT_NAME} -p 8000:8000  ${DOCKER_IMAGE}"
			}
                }
            }
        }
}
