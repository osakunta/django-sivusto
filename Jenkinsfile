node {
    try {
        stage('Fetch repository') {
            checkout scm

            // Pull ilmo_app submodule
            sh "git submodule sync && git submodule update --init --recursive"
        }

        stage('Build image') {
            def app = docker.build("osakunta/django-sivusto")
        }

        stage('Test image') {
            app.inside {
                sh "python manage.py test"
            }
        }

        if (env.BRANCH_NAME == "master") {
            stage('Push image') {
                docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                    app.push("${env.BUILD_NUMBER}")
                    app.push("latest")
                }
            }

            stage('Deploy to Kubernetes') {
                withKubeConfig([credentialsId: 'jenkins-deployer-credentials', serverUrl: 'localhost:8001']) {
                    //sh "kubectl proxy &"
                    //sh "kubectl set image deployment/django django=osakunta/django-sivusto:${env.BUILD_NUMBER}"
                }
            }
        }

    } catch (err) {
        echo "${err}"
        throw err
    } finally {
        stage('Clean Workspace') {
            cleanWs()
        }
    }
}
