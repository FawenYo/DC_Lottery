variable "acr_prefix" {
  type = string
}

variable "helper_fqdn" {
  type        = string
  description = "FQDN for the app"
}

variable "app_images" {
  type = object({
    dc_lottery = string
  })
}

variable "tls_crt_key" {
  type = object({
    crt = string
    key = string
  })
}
