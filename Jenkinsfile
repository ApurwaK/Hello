pipeline {
    agent any

    stages {
        stage('Execute Python Script') {
            steps {
                echo 'Executing Python script...'
                sh 'python pp.py'
                echo 'Python script execution completed.'
            }
        }
    }
}
