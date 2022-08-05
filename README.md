### Install Kubernetes Python Client:

`git clone --recursive https://github.com/kubernetes-client/python.git cd`

`cd python`

`python setup.py install`

### Installation from pip:

`pip install kubernetes`

### validating Webhook Configuration

ValidatingWebhookConfiguration describes the configuration of and admission webhook that accept or reject and object without changing it.

For Validating Webhook Configurations, we use AdmissionregistrationV1Api class from client module.

For listing Validating Webhook Configurations on local cluster e.g minikube we use following command:

`config.load_kube_config()`

### Authentication to the Kubernetes Python Client in other cluster is done by: 

`configuration.api_key = {"authorization": "Bearer" + bearer_token}`

We will use here the Bearer Token which enable requests to authenticate using an access key.

In get.py file we have to provide our cluster details for listing Validating Webhook Configurations:


Give your cluster details:
```
cluster_details={
        "bearer_token":"Your_cluster_bearer_token",
        "api_server_endpoint":"Your_cluster_IP"
    }
```

### Running the File:
```
python3 get.py
```

You will get the list of validating webhook configurations.