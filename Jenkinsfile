pipeline {
    agent{
    label "master"
    }

    stages {
         stage ('Git clone') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/jenkins-testing"]],
                    extensions: [[$class: 'WipeWorkspace']],
                    userRemoteConfigs: [
                        [
                            url: 'https://github.com/Andersen-soft/Andersen-portal-automation',
                            credentialsId: 'jenk2github'
                        ]
                    ]
                ])
            }
        }
         stage('Build and run test'){
        
            steps{
                sh '''sed -i 's/--rm -it -v $PWD/--rm -v $PWD/g' package.json'''
                sh '''npm install'''
                sh '''npm run cypress:docker:run'''
            }
        }
        
        
    }
     post {
        always {
            archiveArtifacts artifacts: 'cypress/screenshots/**/*.png, cypress/actual/**/*.*, cypress/diffs/**/*.* ', fingerprint: true
            cleanWs()
        }
    }
}
