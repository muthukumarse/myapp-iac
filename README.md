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
- setup `GOOGLE_CREDENTIALS` in github action to run pipeline
- Run the pipline manually after clean up all test.
- made small change no of nodes 1 to 2 to trigger pipeline
- Will run automatically and update the environment
- Finally cleaned up everythign manually.
- Note:
  - expect error on creating VPC sometimes it's due to not the resouce cached and loaded. This can be resolved by destroy the cluster and create from scratch. It's acceptable as long as we able to deploy our worksload and all of the state-less.
  - waring are ignorable, since there few update on github Action api which need to correct by looking correct version
  - You may see this error as well
    - Insufficient regional quota to satisfy request: resource "SSD_TOTAL_GB"
    - It's becaue of Quota in selected Region/Zone, just switching to another zone solves most of the time. Since it's free account.
  - if you struck in between of creating resouces half way, no choice we have to clean that and retry.
  - once the pipeline run successfully then we have state so it will be easier to update further.