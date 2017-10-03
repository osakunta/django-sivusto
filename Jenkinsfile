node {
    try {
        checkout scm

        stage('Run tests') {
            sh "echo 'snake oil'"
        }

        stage('Build container') {
            sh "docker-compose build production"

            try {
                sh "docker-compose down production"
            } catch (err) {
                echo "Container was not up"
            } finally {
                sh "docker-compose up production"
            }

        }

    } catch (err) {
        echo "${err}"
        throw err
    } finally {
        stage('Shutdown') {
            sh "echo 'Shutdown'"
        }
    }
}
