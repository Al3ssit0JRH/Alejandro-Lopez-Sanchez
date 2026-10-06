pipeline {
    agent any
    stages {
        stage('Clonar Código') {
            steps {
                checkout scm
            }
        }
        stage('Ejecutar Pruebas Python') {
            steps {
                sh 'docker run --rm -v jenkins_home:/var/jenkins_home -w "$WORKSPACE" python:3.11-slim python -m unittest test_app.py'
            }
        }
    }
}
