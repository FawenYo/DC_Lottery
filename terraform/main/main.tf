terraform {
  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = "=2.7.1"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.16.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "=3.4.3"
    }
  }
}

/*
module "ingress-nginx" {
  source = "../ingress"
}
*/

module "mysql" {
  source = "../mysql"
}

module "dc_lottery" {
  depends_on = [
    #module.ingress-nginx,
    module.mysql
  ]

  source      = "../dc_lottery"
  acr_prefix  = var.acr_prefix
  helper_fqdn = var.helper_fqdn
  app_images  = var.app_images
  mysql       = module.mysql.mysql
  tls_crt_key = var.tls_crt_key
}
