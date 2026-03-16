pipeline {
    agent any
    
    stages {
        
        stage('Récupérer le code') {
            steps {
                echo 'Récupération du code depuis GitHub...'
            }
        }
        
        stage('Builder Docker') {
            steps {
                echo 'Construction de l image Docker...'
                sh 'docker build -t umissa/mon-api .'
            }
        }
        
        stage('Pousser sur Docker Hub') {
            steps {
                echo 'Push sur Docker Hub...'
                sh 'docker push umissa/mon-api'
            }
        }
        
        stage('Déployer sur Kubernetes') {
            steps {
                echo 'Déploiement sur Kubernetes...'
                sh 'kubectl apply -f webapp.yaml'
            }
        }
        
    }
}