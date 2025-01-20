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
			def containerExists = sh(script: "docker ps -a -q -f 'name=${PROJECT_NAME}'", returnStdout: true).trim()
	
	                // Если контейнер существует, останавливаем и удаляем его
	                if (containerExists) {
	                    echo "Stopping and removing existing container..."
	                    sh "docker stop ${containerExists}"
	                    sh "docker rm ${containerExists}"
	                } else {
	                    echo "No existing container found."
	                }
	
	                // Запуск нового контейнера
	                sh """
	                    docker run -d --name ${PROJECT_NAME} -p 8000:8000 ${DOCKER_IMAGE}
	                """
		            ///sh """
				///docker ps -q -f "name=${PROJECT_NAME}" | xargs -r docker stop
		            	///docker ps -a -q -f "name=${PROJECT_NAME}" | xargs -r docker rm
			    	///docker run -d --name ${PROJECT_NAME} -p 8000:8000 -e DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY} ${DOCKER_IMAGE}
				///"""
			}
                }
            }
        }
}
