########################
# Kubernetes Namespace #
########################

resource "kubernetes_namespace" "dc_lottery" {
  metadata {
    name = var.namespace
  }
}

##################
# MySQL Database #
##################

resource "random_password" "mysql_password" {
  length      = 18
  special     = false
  min_lower   = 1
  min_numeric = 1
  min_upper   = 1
}

resource "helm_release" "mysql" {
  depends_on = [
    kubernetes_namespace.dc_lottery,
    random_password.mysql_password,
  ]

  name          = "dc-lottery-mysql"
  namespace     = var.namespace
  chart         = "https://charts.bitnami.com/bitnami/mysql-9.4.5.tgz"
  recreate_pods = true
  max_history   = 3

  set {
    name  = "primary.persistence.size"
    value = "1Gi"
    type  = "string"
  }

  set {
    name  = "secondary.persistence.size"
    value = "1Gi"
    type  = "string"
  }

  set {
    name  = "auth.database"
    value = "dc_lottery"
    type  = "string"
  }

  set_sensitive {
    name  = "auth.rootPassword"
    value = random_password.mysql_password.result
    type  = "string"
  }
}
