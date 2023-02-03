## How to run manually
- Please setup your own Google account and sigup in Google console.
- Note - I tested all of these and tear down my environment not to get any billing :)
- change `project_id` in [terraform.tfvars](./terraform.tfvars)
- Aussume that you already connected your Google account through `google-cloud-sdk` and check you have `~/google_application_creedentials.json`
- `terraform init`
- `terraform apply`
- Note:
  - Used generic way (simlar to test lab) to create GKE
  - left detaulf working one with quick lab
  - TODO - should do IAM and other stuff for GKE API 

## Connect GKE to deploy helm chart manually
- Assume that, you have kubectl CLI installed
- get the kubeconfig standard way
  - `gcloud container clusters get-credentials $(terraform output -raw kubernetes_cluster_name) --region $(terraform output -raw region)`
- Check you able to run below command to check the nodes created above
  - `kubectl get nodes`
  - `kubectl get pods -A`

## Clean your cluster
- `terraform destroy`
- *** Don't forgot ***

## Test I have done
- Created cluster over github action
- made small change no of nodes 1 to 2 to trigger pipeline
- Note:
  - I removed all the secrets from github after testing
