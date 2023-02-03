## How to run manually
- Please setup your own Google account and sigup in Google console.
- Note - I tested all of these and tear down my environment not to get any billing :)
- change `project_id` from your account in [terraform.tfvars](./terraform.tfvars)
- Aussume that you already connected your Google account through `google-cloud-sdk` and check you have `~/google_application_creedentials.json`
- `terraform init`
- `terraform apply`
- Note:
  - Used generic way (simlar to test lab) to create GKE
  - left detaulf working one with quick lab
  - TODO - should do IAM and other stuff for GKE API 

## Clean your cluster
- `terraform destroy`
- *** Don't forgot ***

## Test I have done
- Created cluster over github action
- made small change no of nodes 1 to 2 to trigger pipeline
- Note:
  - I removed all the secrets from github after testing
- expect error on creating VPC sometimes it's due to not the resouce cached and loaded. This can be resolved by destroy the cluster and create from scratch. It's acceptable as long as we able to deploy our worksload and all of the state-less.
- waring are ignorable, since there few update on github Action api which need to correct by looking correct version
- You may see this error
  - Error: error creating NodePool: googleapi: Error 403: Insufficient regional quota to satisfy request: resource "SSD_TOTAL_GB": request requires '600.0' and is short '100.0'. project has a quota of '500.0' with '500.0' available. View and manage quotas at https://console.cloud.google.com/iam-admin/quotas?usage=USED&project=silent-oxygen-376712., forbidden
  - It's becaue of Quota in selected Region/Zone, just switching to another zone solves most of the time. Since it's free account.
