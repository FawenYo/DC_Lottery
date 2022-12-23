resource "helm_release" "app" {
  name          = "dc-lottery-app"
  namespace     = var.namespace
  chart         = "${path.module}/charts"
  recreate_pods = true
  max_history   = 3

  set {
    name  = "ACR_PREFIX"
    value = var.acr_prefix
  }

  set {
    name  = "APP_IMAGE"
    value = var.app_images.dc_lottery
  }

  set {
    name  = "HELPER_FQDN"
    value = var.helper_fqdn
  }

  set {
    name  = "MYSQL_HOST"
    value = var.mysql.endpoint
    type  = "string"
  }

  set_sensitive {
    name  = "MYSQL_PASSWORD"
    value = var.mysql.password
    type  = "string"
  }

  set_sensitive {
    name  = "TLS_SIDECAR_CRT"
    value = var.tls_crt_key.crt
    type  = "string"
  }

  set_sensitive {
    name  = "TLS_SIDECAR_KEY"
    value = var.tls_crt_key.key
    type  = "string"
  }
}
