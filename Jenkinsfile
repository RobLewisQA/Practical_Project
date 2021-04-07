pipeline{
        agent any
        stages{
            stage('Test'){
                sh 'pytest --cov=application --cov-report=term-missing'
            }
            stage('Build'){
                sh 'docker-compose build'
            }
            stage('Push'){
                sh 'docker-compose push'
            }
            stage('Configure Swarm'){
                sh 'ansible-playbook -i inventory.yaml playbook.yaml'
            }
            stage('Deploy'){
                sh 'docker stack deploy'
            }   
        }
}