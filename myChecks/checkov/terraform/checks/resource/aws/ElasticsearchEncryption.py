from myChecks.checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck
from myChecks.checkov.common.models.enums import CheckCategories


class ElasticsearchEncryption(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure all data stored in the Elasticsearch is securely encrypted at rest"
        id = "CKV_AWS_5"
        supported_resources = ['aws_elasticsearch_domain']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return "encrypt_at_rest/[0]/enabled"


check = ElasticsearchEncryption()
