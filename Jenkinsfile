pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vladfire.ru:latest"
	PROJECT_NAME = "vladfire.ru"
	DJANGO_SECRET_KEY = credentials('DJANGO_SECRET_KEY')
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                        docker build -t ${DOCKER_IMAGE} .
                    """
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    sh """
			CONTAINER_ID=$(docker ps -a -q -f "name=${PROJECT_NAME}")
                        if [ -n "${CONTAINER_ID}" ]; then
                            docker stop ${CONTAINER_ID}
                            docker rm ${CONTAINER_ID}
                        fi
                        docker run -d --name ${PROJECT_NAME} -p 8000:8000 -e DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY} $DOCKER_IMAGE
			"""
                }
            }
        }
    }
}
