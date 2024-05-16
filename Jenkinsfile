pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository from GitHub
                git 'https://github.com/ApurwaK/Hello.git'
            }
        }
        stage('Validate JSON') {
            steps {
                script {
                    try {
                        // Run Python script to validate JSON files
                        sh 'python pp.py'
                    } catch (Exception e) {
                        echo "Error: ${e}"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
    }
}
