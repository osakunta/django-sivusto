node {
    try {
        checkout scm

        stage('Run tests') {
            sh "echo 'snake oil'"
        }

        stage('Build container') {
            if (env.BRANCH_NAME == "master") {
                sh "echo ''"
            } else {
                sh "echo 'Skipping as branch was ${env.BRANCH_NAME} instead of master'"
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
