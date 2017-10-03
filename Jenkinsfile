node {
    try {
        stage('Checkout repository') {
            checkout scm
        }

        stage('Run tests') {
            sh "echo 'snake oil'"
        }

        stage('Build container') {
            sh "docker-compose build production"
            sh "docker-compose down production"
            sh "docker-compose up production"
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
