from myChecks.checkov.common.models.enums import CheckResult, CheckCategories
from myChecks.checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck

class MyChecksAccID(BaseResourceCheck):
    def __init__(self):
        name = "Ensure rotation for customer created CMKs is enabled"
        id = "CKV_AWS_myChecks_1"
        supported_resources = ['aws_kms_key']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        print(conf)
        if 'storage_encrypted' in conf.keys():
            key = conf['storage_encrypted'][0]
            if key:
                return CheckResult.PASSED
        return CheckResult.FAILED


check = MyChecksAccID()