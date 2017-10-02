node {
    try {
        stage('Checkout repository') {
            checkout scm
        }

        stage('Run tests') {
            sh "echo 'snake oil'"
        }

        if (env.BRANCH_NAME == 'master') {
            stage('Upgrade production container') {
                sh "docker-compose build production"
            }
        }

        stage('Build container') {
            sh "docker-compose build production"
        }

    } catch (err) {
        echo "${err}"
        throw err
    } finally {
        stage('Shutdown') {
        }
    }
}
