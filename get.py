from kubernetes import client
from kubernetes.client import ApiClient

def __get_kubernetes_client(bearer_token,api_server_endpoint):
    try:
        configuration = client.Configuration()
        configuration.host = api_server_endpoint
        configuration.verify_ssl = False
        configuration.api_key = {"authorization": "Bearer " + bearer_token}
        client.Configuration.set_default(configuration)
        client_api = client.AdmissionregistrationV1Api()
        return client_api
    except Exception as e:
        print("Error getting kubernetes client \n{}".format(e))
        return None
def __format_data_for_validating_webhook_configuration(client_output):
        temp_dict={}
        temp_list=[]
        
        json_data=ApiClient().sanitize_for_serialization(client_output)
        if len(json_data["items"]) != 0:
            for webhook in json_data["items"]:
                temp_dict={
                    "webhook": webhook["metadata"]["name"],
                    "namespace": webhook["metadata"]["namespace"],
                }
                temp_list.append(temp_dict)
        return temp_list

def get_validating_webhook_configuration(cluster_details):
        client_api= __get_kubernetes_client(
            bearer_token=cluster_details["bearer_token"],
            api_server_endpoint=cluster_details["api_server_endpoint"],
        )
       
        webhook_list = client_api.list_validating_webhook_configuration()
        data=__format_data_for_validating_webhook_configuration(webhook_list)
        print (data)



if __name__ == "__main__":
    cluster_details={
        "bearer_token":"<YOUR_BEARER_TOKEN>",
        "api_server_endpoint":"<YOUR_API_SERVER_ENDPOINT>"

    }
get_validating_webhook_configuration(cluster_details)