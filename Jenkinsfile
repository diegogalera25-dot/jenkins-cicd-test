pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && python3 -m pytest --verbose'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Despliegue simulado exitosamente en entorno de staging"'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completado con exito'
        }
        failure {
            echo 'El pipeline ha fallado'
        }
    }
}
