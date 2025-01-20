pipeline {
    agent any

    environment {
    	DOCKER_IMAGE = "vladfire.ru:latest"
		PROJECT_NAME = "vladfire.ru"
		//DJANGO_SECRET_KEY = credentials('DJANGO_SECRET_KEY')
        TELEGRAM_CHAT_ID = '7631506759'
        TELEGRAM_TOKEN = credentials('telegram-token')
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
					withCredentials([string(credentialsId: 'DJANGO_SECRET_KEY', variable: 'DJANGO_SECRET')]) {
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
								docker run -d --name ${PROJECT_NAME} -p 8000:8000 -e DJANGO_SECRET_KEY="${DJANGO_SECRET}" ${DOCKER_IMAGE}
							"""
							///sh """
								///docker ps -q -f "name=${PROJECT_NAME}" | xargs -r docker stop
								///docker ps -a -q -f "name=${PROJECT_NAME}" | xargs -r docker rm
								///docker run -d --name ${PROJECT_NAME} -p 8000:8000 -e DJANGO_SECRET_KEY=${env.DJANGO_SECRET} ${DOCKER_IMAGE}
							///"""
					}
				}
            }
        }
    }
	post {
        success {
            script {
                sendTelegramMessage("✅ Build succeeded: ${env.JOB_NAME} #${env.BUILD_NUMBER}", env.BRANCH_NAME, env.BUILD_URL)
            }
        }
        failure {
            script {
                sendTelegramMessage("❌ Build failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}", env.BRANCH_NAME, env.BUILD_URL)
            }
        }
        unstable {
            script {
                sendTelegramMessage("⚠️ Build unstable: ${env.JOB_NAME} #${env.BUILD_NUMBER}", env.BRANCH_NAME, env.BUILD_URL)
            }
        }
        always {
            echo "Build completed"
        }
    }
}
def sendTelegramMessage(String message, String branch, String buildUrl) {
    sh """
        curl -s -X POST https://api.telegram.org/bot${env.TELEGRAM_TOKEN}/sendMessage \
        -d chat_id=${env.TELEGRAM_CHAT_ID} \
        --data-urlencode text="${message}\nBranch: ${branch}\nURL: ${buildUrl}"
    """
}
