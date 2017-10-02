def DEPLOY_ENV = 'test'

if (env.BRANCH_NAME == 'master') {
    EPLOY_ENV = 'production'
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
