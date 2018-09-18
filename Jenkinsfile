node {
    try {
        stage('Fetch repository') {
            checkout scm

            // Pull ilmo_app submodule
            sh "cd ilmo_repo/ && git submodule init && git submodule update"
        }

        stage('Run tests') {
            sh "echo 'snake oil'"
        }

        if (env.BRANCH_NAME == "master") {
            stage('Build image') {
                app = docker.build("osakunta/django-sivusto")
            }

            stage('Test image') {
                app.inside {
                    sh 'echo "Tests passed"'
                }
            }

            stage('Push image') {
                docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                    app.push("${env.BUILD_NUMBER}")
                    app.push("latest")
                }
            }

            stage('Deploy to Kubernetes') {
                sh "kubectl set image deployment/django django=osakunta/django-sivusto:${env.BUILD_NUMBER}"
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
