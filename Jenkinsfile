node {
    try {
        checkout scm

        stage('Run tests') {
            sh "echo 'snake oil'"
        }

        stage('Build container') {
            when {
                branch "master"
            }
            steps {
                sh "docker-compose up --build -d production"
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
