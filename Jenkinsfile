node {
    try {
        checkout scm

        stage('Run tests') {
            sh "echo 'snake oil'"
        }

        stage('Build container') {
            sh "docker-compose up --build --no-deps -d production"
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
