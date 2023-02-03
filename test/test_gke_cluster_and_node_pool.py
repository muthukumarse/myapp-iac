# Test for Google Container Cluster and Node Pool

# Test for the Google Container Cluster resource
def test_google_container_cluster(resource):
  assert resource.name == "${var.project_id}-gke"
  assert resource.location == var.region
  assert resource.remove_default_node_pool == true
  assert resource.initial_node_count == 1
  assert resource.network == google_compute_network.vpc.name
  assert resource.subnetwork == google_compute_subnetwork.subnet.name

# Test for the Google Container Node Pool resource
def test_google_container_node_pool(resource):
  assert resource.name == google_container_cluster.primary.name
  assert resource.location == var.region
  assert resource.cluster == google_container_cluster.primary.name
  assert resource.node_count == var.gke_num_nodes

  node_config = resource.node_config
  assert node_config.oauth_scopes == [
    "https://www.googleapis.com/auth/logging.write",
    "https://www.googleapis.com/auth/monitoring",
  ]
  assert node_config.labels == {
    "env": var.project_id
  }
  assert node_config.machine_type == "t2d-standard-1"
  assert node_config.tags == ["gke-node", "${var.project_id}-gke"]
  assert node_config.metadata == {
    "disable-legacy-endpoints": "true"
  }
