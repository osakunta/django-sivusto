if (env.BRANCH_NAME == 'master') {
    def DEPLOY_ENV = 'production'
} else {
    def DEPLOY_ENV = 'test'
}

node {
    try {
        stage('Checkout repository') {
            checkout scm
        }

        stage('Run tests') {
            sh "echo 'snake oil'"
        }

        stage('Build container') {
            sh "docker-compose build ${DEPLOY_ENV}"
        }

    } catch (err) {
        echo "${err}"
        throw err
    } finally {
        stage('Shutdown') {
        }
    }
}
