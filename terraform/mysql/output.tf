output "mysql" {
  value = {
    endpoint = "${helm_release.mysql.name}.${helm_release.mysql.namespace}.svc.cluster.local"
    password = random_password.mysql_password.result
  }
}